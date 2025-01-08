import sys

from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import *

import numpy as np
import tensorflow as tf

class Unmanned_store(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.predictList = {
            0 : ['티셔츠', 5000],
            1 : ['트라우저 진', 30000],
            2 : ['스웨터', 15000],
            3 : ['드레스', 50000],
            4 : ['코트', 150000],
            5 : ['샌들', 10000],
            6 : ['셔츠', 15000],
            7 : ['스니커즈', 25000],
            8 : ['가방', 67000],
            9 : ['앵클부츠', 45000],
        }
    
        self.store_name = QLabel('Unmanned Store v1.0', self)
        self.store_name.setFont(QFont('Decorative', 20))
        self.store_name.adjustSize()
        self.store_name.move(180, 30)

        self.image = QLabel(self)
        self.image.move(170, 100)

        self.guide = QLabel('File을 눌러 모델을 추가 후 이미지 삽입하여 인식', self)
        self.guide.move(150, 500)
        self.guide.adjustSize()

        self.imgUpload = QPushButton('이미지 업로드', self)
        self.imgUpload.move(170, 430)
        self.imgUpload.setEnabled(False)
        self.imgUpload.clicked.connect(self.loadImage)

        self.predictModel = None

        menuBar = self.menuBar()
        menuBar.setNativeMenuBar(False)
        fileMenu = menuBar.addMenu('File')
        loadModelMenu = QAction('모델 불러오기', self)
        loadModelMenu.setShortcut('Ctrl + L')
        loadModelMenu.triggered.connect(self.loadModel)
        fileMenu.addAction(loadModelMenu)

        self.setWindowTitle('Unmanned Store v1.0')
        self.setGeometry(300, 300, 600, 600)
        self.show()

    def loadModel(self):
        try:   
            modelFile, _ = QFileDialog.getOpenFileName(self, '모델 추가', '')
            

            if modelFile:
                self.predictModel = tf.keras.models.load_model(modelFile)
                self.guide.setText('모델 추가 완료!')

            self.imgUpload.setEnabled(True)
        except:
            self.guide.setText('모델 파일이 아닙니다.')
    
    def loadImage(self):
        imgName = QFileDialog.getOpenFileName(self, 'Open File', './')
        imgFile = QPixmap(imgName[0]).scaled(300, 300, aspectRatioMode=Qt.KeepAspectRatio)
        self.image.setPixmap(imgFile)
        self.image.adjustSize()

        if imgFile:
            mtrx = np.zeros((28, 28))
            for r in range(28):
                for c in range(28):
                    mtrx[c, r] = 1 - QImage(QPixmap(imgName[0]))\
                                    .scaled(28,28).pixelColor(r, c).getRgb()[0] / 255.0
                    # 이미지 압축 
            mtrx = mtrx.reshape(-1, 28, 28)

            pred = self.predictModel.predict(mtrx)[0]
            result = np.argmax(pred)

            self.guide.setText(f'선택 제품 - {self.predictList.get(result)[0]} / 가격 - {self.predictList.get(result)[1]}원 ')

            self.guide.adjustSize()
            self.guide.move(150, 500)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    inst = Unmanned_store()
    app.exec()