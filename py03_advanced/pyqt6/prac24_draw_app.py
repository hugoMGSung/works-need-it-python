import sys
from PyQt6.QtCore import Qt, QPoint
from PyQt6.QtGui import QPainter, QColor, QPen, QImage
from PyQt6.QtWidgets import QApplication, QMainWindow, QGraphicsView, QGraphicsScene, QVBoxLayout, QLabel, QWidget, QPushButton

class PaintWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(280, 280)  # 고정 크기 설정
        self.drawing = False
        self.lastPoint = QPoint()
        self.image = QImage(280, 280, QImage.Format.Format_RGB888)
        self.image.fill(QColor(255, 255, 255))  # 배경을 흰색으로 설정

    def mousePressEvent(self, event):
        # 마우스를 눌렀을 때 그리기 시작
        if event.button() == Qt.MouseButton.LeftButton:
            self.drawing = True
            self.lastPoint = event.pos()

    def mouseMoveEvent(self, event):
        # 마우스를 이동할 때 그리기
        if self.drawing:
            painter = QPainter(self.image)
            painter.setPen(QPen(Qt.GlobalColor.black, 10))  # 펜 색상과 두께
            painter.drawLine(self.lastPoint, event.pos())
            self.lastPoint = event.pos()
            self.update()  # 화면을 갱신

    def mouseReleaseEvent(self, event):
        # 마우스를 뗄 때 그리기 종료
        if event.button() == Qt.MouseButton.LeftButton:
            self.drawing = False

    def clear(self):
        # 그린 내용을 지우기
        self.image.fill(QColor(255, 255, 255))  # 배경을 다시 흰색으로 채움
        self.update()

    def paintEvent(self, event):
        # 화면에 그린 이미지를 그리기
        painter = QPainter(self)
        painter.drawImage(0, 0, self.image)  # 이미지를 그린 위치

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Draw Numbers")

        self.paintWidget = PaintWidget()
        self.resultLabel = QLabel("Draw a number...")
        self.clearButton = QPushButton("Clear")

        layout = QVBoxLayout()
        layout.addWidget(self.paintWidget)
        layout.addWidget(self.resultLabel)
        layout.addWidget(self.clearButton)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        self.clearButton.clicked.connect(self.clearDrawing)

    def clearDrawing(self):
        self.paintWidget.clear()
        self.resultLabel.setText("Draw a number...")

app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec())