'''
PyQt5 예제 소스
1. 필요라이브러리 설치
pip install PyQt5 [--no-warn-script-location]
'''
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QToolTip, QMainWindow
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtGui import QIcon, QFont

class MyApp(QMainWindow):
   
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):        
        self.statusBar().showMessage('Ready')

        strTooltip = 'This is a <b>QWidget</b> widget'

        QToolTip.setFont(QFont('NanumGothic', 10))
        self.setToolTip('StatusBar App')

        btn = QPushButton('Quit', self)
        btn.setToolTip(strTooltip)
        btn.move(50, 50)
        btn.resize(btn.sizeHint())
        btn.clicked.connect(QCoreApplication.instance().quit)

        self.setWindowTitle('Hugo QtApp')
        self.setWindowIcon(QIcon('earth.png'))
        self.setGeometry(300, 300, 640, 400)
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())