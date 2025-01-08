import sys
import torch
from PyQt6.QtCore import Qt, QPoint
from PyQt6.QtGui import QPainter, QColor, QPen, QImage
from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QLabel, QWidget, QPushButton
import numpy as np
import torchvision.transforms as transforms
from torchvision import datasets

# PyTorch 모델 정의 (훈련된 모델 로드)
class Net(torch.nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        self.conv1 = torch.nn.Conv2d(1, 32, kernel_size=3, stride=1, padding=1)
        self.conv2 = torch.nn.Conv2d(32, 64, kernel_size=3, stride=1, padding=1)
        self.fc1 = torch.nn.Linear(7*7*64, 1000)
        self.fc2 = torch.nn.Linear(1000, 10)

    def forward(self, x):
        x = torch.relu(self.conv1(x))
        x = torch.relu(self.conv2(x))
        x = x.view(-1, 7*7*64)  # Flatten
        x = torch.relu(self.fc1(x))
        x = self.fc2(x)
        return x

# 모델 로드
model = Net()
model.load_state_dict(torch.load('./pyqt6/mnist_model.pt'))
model.eval()  # 모델을 평가 모드로 설정

# PyQt6 드로잉 위젯
class PaintWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(280, 280)  # 고정 크기 설정
        self.drawing = False
        self.lastPoint = QPoint()
        self.image = QImage(280, 280, QImage.Format.Format_RGB888)
        self.image.fill(QColor(255, 255, 255))  # 배경을 흰색으로 설정

    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self.drawing = True
            self.lastPoint = event.pos()

    def mouseMoveEvent(self, event):
        if self.drawing:
            painter = QPainter(self.image)
            painter.setPen(QPen(Qt.GlobalColor.black, 10))  # 펜 색상과 두께
            painter.drawLine(self.lastPoint, event.pos())
            self.lastPoint = event.pos()
            self.update()  # 화면을 갱신

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self.drawing = False

    def clear(self):
        self.image.fill(QColor(255, 255, 255))  # 배경을 다시 흰색으로 채움
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.drawImage(0, 0, self.image)  # 이미지를 그린 위치

    def getImage(self):
        return self.image

# PyQt6 메인 윈도우
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Draw Numbers")

        self.paintWidget = PaintWidget()
        self.resultLabel = QLabel("Draw a number...")
        self.clearButton = QPushButton("Clear")
        self.predictButton = QPushButton("Predict Number")

        layout = QVBoxLayout()
        layout.addWidget(self.paintWidget)
        layout.addWidget(self.resultLabel)
        layout.addWidget(self.predictButton)
        layout.addWidget(self.clearButton)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        self.clearButton.clicked.connect(self.clearDrawing)
        self.predictButton.clicked.connect(self.predict)

    def clearDrawing(self):
        self.paintWidget.clear()
        self.resultLabel.setText("Draw a number...")

    def predict(self):
        # 그린 이미지를 처리하고 예측
        image = self.paintWidget.getImage()
        image = image.convertToFormat(QImage.Format.Format_Grayscale8)
        
        # QImage의 bits()는 1D 배열로 반환되므로, 이를 적절히 2D 배열로 변환
        img_array = np.array(image.bits()).reshape((28, 28))
        
        # 이미지를 반전시켜서 검정 배경에 흰색 숫자처럼 만들기
        img_array = 255 - img_array

        # 0-1 범위로 정규화
        img_array = img_array.astype(np.float32) / 255.0
        
        # 배치 차원 추가 (배치 차원은 1, 채널 차원은 1)
        img_array = np.expand_dims(img_array, axis=0)  # (1, 28, 28)
        img_array = np.expand_dims(img_array, axis=-1)  # (1, 28, 28, 1)

        # NumPy 배열을 PyTorch 텐서로 변환
        img_tensor = torch.from_numpy(img_array)

        # 예측
        with torch.no_grad():
            output = model(img_tensor)
            pred = output.argmax(dim=1, keepdim=True)
            self.resultLabel.setText(f"Predicted Digit: {pred.item()}")

app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec())
