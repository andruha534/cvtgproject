<template>
    <div class="cv-wrapper">
        <div class="main-title-section">
            <div class="main-title">
                <p>Computer Vision</p>
            </div>
            <div class="try-now-container">
                <div class="container">
                    <button class="button" @click="showCamera">Try now</button>
                </div>
            </div>
        </div>

        <!-- Плавный переход при появлении контейнера камеры -->
        <transition name="fade">
            <div v-if="isCameraActive" id="camera-container">
                <div id="camera">
                    <video ref="video" width="640" height="480" autoplay></video>
                    <button id="capture" @click="captureImage">Capture</button>
                    <canvas ref="canvas" style="display: none;"></canvas>
                </div>
                <div id="result">
                    <div v-if="prediction">
                        <img :src="'data:image/jpeg;base64,' + prediction.image" alt="Processed Image" />
                        <div v-if="prediction.emotions && prediction.emotions.length > 0">
                            <h3>Detected Emotions:</h3>
                            <ul>
                                <li v-for="(emotion, index) in prediction.emotions" :key="index">
                                    {{ emotion.emotion }}: {{ emotion.confidence }}
                                </li>
                            </ul>
                        </div>
                        <div v-else>
                            <p>No emotions detected.</p>
                        </div>
                    </div>
                </div>
            </div>
        </transition>
    </div>
</template>

<script setup>
import { ref, onUnmounted } from 'vue'

// Реактивная переменная для управления видимостью камеры
const isCameraActive = ref(false)

// Ссылки на элементы video и canvas
const video = ref(null)
const canvas = ref(null)

// Реактивная переменная для хранения результатов предсказания
const prediction = ref(null)

let stream = null

// Функция для отображения камеры
const showCamera = () => {
    isCameraActive.value = true
    console.log('Camera active:', isCameraActive.value)
    startCamera()
}

// Функция для запуска камеры
const startCamera = async () => {
    try {
        stream = await navigator.mediaDevices.getUserMedia({ video: true })
        if (video.value) {
            video.value.srcObject = stream
        }
    } catch (err) {
        console.error('Ошибка доступа к камере:', err)
    }
}

// Функция для остановки камеры
const stopCamera = () => {
    if (stream) {
        stream.getTracks().forEach(track => track.stop())
    }
}

// Останавливаем камеру при размонтировании компонента
onUnmounted(() => {
    stopCamera()
})

// Функция для захвата изображения с камеры и отправки на бэкенд
const captureImage = async () => {
    if (canvas.value && video.value) {
        const context = canvas.value.getContext('2d')
        canvas.value.width = video.value.videoWidth
        canvas.value.height = video.value.videoHeight
        context.drawImage(video.value, 0, 0, canvas.value.width, canvas.value.height)
        const imageData = canvas.value.toDataURL('image/jpeg')
        console.log('Captured Image:', imageData)

        try {
            const response = await fetch('http://127.0.0.1:5001/predict', { // Замените URL на ваш бэкенд
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ image: imageData })
            })
            const data = await response.json()
            if (data.error) {
                console.error('Error from server:', data.error)
                return
            }

            prediction.value = data
            console.log('Prediction Result:', data)
        } catch (error) {
            console.error('Error:', error)
        }
    }
}
</script>

<style scoped>
/* design */
.cv-wrapper {
    margin: 0;
    background-image: url('@/assets/images/bg-cv.png');
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
    color: #ffffff;
}

/*computer vision section*/
.main-title-section {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    height: 100vh;
    width: 100%;
    gap: 20px;
}

/*animation fade in computer vision*/
@keyframes fadeInUp {
    0% {
        opacity: 0;
        transform: translateY(50px);
    }

    100% {
        opacity: 1;
        transform: translateY(0);
    }
}

/*computer vision title*/
.main-title {
    text-align: center;
    animation: fadeInUp 2s ease-out;
}

.main-title p {
    font-size: 6vw;
    margin: 0;
    font-weight: 500;
}

/*computer vision animation*/
@keyframes fadeIn {
    0% {
        opacity: 0;
        transform: scale(0.9);
    }

    100% {
        opacity: 1;
        transform: scale(1);
    }
}

/*camera section */
#camera-container {
    gap: 20px;
    opacity: 1;
    transition: opacity 1s ease, transform 1s ease;
    padding: 20px;
    border-radius: 15px;
    background: rgba(0, 0, 0, 0.6);
    box-shadow: 0 8px 15px rgba(0, 0, 0, 0.3);
    margin-bottom: 50px;
    display: flex; 
    animation: fadeIn 1s ease;
}

/*camera section right*/
#camera,
#result {
    border: 1px solid #ddd;
    border-radius: 15px;
    overflow: hidden;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
    background: #ffffff;
}

#video {
    border-radius: 15px 15px 0 0;
}

#result {
    width: 640px;
    height: 480px;
    background: #f0f0f0;
    position: relative;
}

#capture {
    display: none;
    width: 100%;
    padding: 15px;
    background-color: #03a9f4;
    color: #fff;
    border: none;
    cursor: pointer;
    font-size: 1.2em;
    text-align: center;
    transition: background-color 0.3s ease;
    border-radius: 0 0 15px 15px;
}

#capture:hover {
    background-color: #0288d1;
}

/* Показываем кнопку capture, когда камера активна */
#camera-container #capture {
    display: block;
}

.try-now-container {
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 10px;
}

.button {
    font-size: 1.4em;
    padding: 0.6em 0.8em;
    border-radius: 0.5em;
    border: none;
    background-color: #000;
    color: #fff;
    cursor: pointer;
    box-shadow: 2px 2px 3px #000000b4;
}

.container {
    position: relative;
    padding: 3px;
    background: linear-gradient(90deg, #03a9f4, #f441a5);
    border-radius: 0.9em;
    transition: all 0.4s ease;
    animation: fadeInUp 2s ease-out;
}

.container::before {
    content: "";
    position: absolute;
    inset: 0;
    margin: auto;
    border-radius: 0.9em;
    z-index: -10;
    filter: blur(0);
    transition: filter 0.4s ease;
}

.container:hover::before {
    background: linear-gradient(90deg, #03a9f4, #f441a5);
    filter: blur(1.2em);
}

.container:active::before {
    filter: blur(0.2em);
}

/* transitions */
.fade-enter-active, .fade-leave-active {
    transition: opacity 1s;
}

.fade-enter-from, .fade-leave-to {
    opacity: 0;
}
</style>
