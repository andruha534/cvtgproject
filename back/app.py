from flask import Flask, request, jsonify
from flask_cors import CORS
import cv2
import numpy as np
from PIL import Image
from io import BytesIO
import base64
import model
import torch
import os



app = Flask(__name__)
CORS(app)  

model_path = os.path.join(os.path.dirname(__file__), 'model6266_best.pth')

face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)
model6190 = model.Classifier(3, 64, 7)
model6190.load_state_dict(torch.load(model_path, map_location=torch.device("cpu")))
model6190.eval()

emotion_labels = ['Angry', 'Disgust', 'Fear', 'Happy', 'Neutral', 'Sad', 'Surprise']

@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.get_json()
        image_data = data["image"].split(",")[1]  
        image = Image.open(BytesIO(base64.b64decode(image_data)))
        image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)

        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(
            gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30)
        )

        emotions_detected = []
        for (x, y, w, h) in faces:
            face_roi = image[y:y + h, x:x + w]
            face_resized = cv2.resize(face_roi, (48, 48))
            face_gray = cv2.cvtColor(face_resized, cv2.COLOR_BGR2GRAY)
            face_rgb = np.stack((face_gray,) * 3, axis=-1)

            face_tensor = torch.from_numpy(face_rgb).float()
            face_tensor = face_tensor.permute(2, 0, 1) / 255.0 
            face_tensor = face_tensor.unsqueeze(0) 

            with torch.no_grad():
                output = model6190(face_tensor)
                probabilities = torch.nn.functional.softmax(output, dim=1)
                _, predicted = torch.max(output, 1)
                predicted_prob = probabilities[0, predicted.item()].item()
                emotion = emotion_labels[predicted.item()]

            emotions_detected.append({
                "emotion": emotion,
                "confidence": round(predicted_prob, 2),
                "box": [int(x), int(y), int(w), int(h)] 
            })


            cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 2)
            cv2.putText(
                image,
                f"{emotion}: {predicted_prob:.2f}",
                (x, y - 10),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.9,
                (255, 0, 0),
                2
            )

        _, buffer = cv2.imencode('.jpg', image)
        image_result = base64.b64encode(buffer).decode('utf-8')

        return jsonify({"emotions": emotions_detected, "image": image_result})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True, port=5001)
