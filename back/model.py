import torch
from torch import nn
import os


class Classifier(nn.Module):
    def __init__(self, input_shape, hidden_layers, output_shape):
        super().__init__()
        self.block_1 = nn.Sequential(
            nn.Conv2d(in_channels=input_shape, out_channels=hidden_layers, kernel_size=3, stride=1, padding=1),
            nn.BatchNorm2d(hidden_layers),
            nn.ReLU(),
            nn.Conv2d(in_channels=hidden_layers, out_channels=hidden_layers, kernel_size=3, stride=1, padding=1),
            nn.BatchNorm2d(hidden_layers),
            nn.ReLU(),
            nn.MaxPool2d(kernel_size=2, stride=2),
            nn.Dropout(0.25)
        )

        self.block_2 = nn.Sequential(
            nn.Conv2d(in_channels=hidden_layers, out_channels=hidden_layers, kernel_size=3, stride=1, padding=1),
            nn.BatchNorm2d(hidden_layers),
            nn.ReLU(),
            nn.Conv2d(in_channels=hidden_layers, out_channels=hidden_layers, kernel_size=3, stride=1, padding=1),
            nn.BatchNorm2d(hidden_layers),
            nn.ReLU(),
            nn.MaxPool2d(kernel_size=2, stride=2),
            nn.Dropout(0.25)
        )

        self.block_3 = nn.Sequential(
            nn.Conv2d(in_channels=hidden_layers, out_channels=hidden_layers, kernel_size=3, stride=1, padding=1),
            nn.BatchNorm2d(hidden_layers),
            nn.ReLU(),
            nn.Conv2d(in_channels=hidden_layers, out_channels=hidden_layers, kernel_size=3, stride=1, padding=1),
            nn.BatchNorm2d(hidden_layers),
            nn.ReLU(),
            nn.MaxPool2d(kernel_size=2, stride=2),
            nn.Dropout(0.25)
        )

        self.classifier = nn.Sequential(
            nn.Flatten(),
            nn.Linear(in_features=hidden_layers * 6 * 6, out_features=output_shape)
        )

    def forward(self, x):
        x = self.block_1(x)
        x = self.block_2(x)
        x = self.block_3(x)
        x = self.classifier(x)
        return x

model = Classifier(3, 64, 7)

model_path = os.path.join(os.path.dirname(__file__), 'model6266_best.pth')
model.load_state_dict(torch.load(model_path))
# 130 epochs - 60.95
#170 epochs - 61.90
#264 epochs - 62.66 accuracy on FER2013 dataset.

# 3 blocks each containing 2 batch norm 2 conv 1 maxpool and 1 dropout layers. hidden states with 64 neurons
# 203335 parameters in total. 1 block - 38976 , 2 block - 74112 , 3 block - 74112 , classifier - 16135