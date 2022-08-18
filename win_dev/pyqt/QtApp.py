'''
PyQt5 예제 소스
1. 필요라이브러리 설치
pip install PyQt5 [--no-warn-script-location]
'''
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QMessageBox, QAction, qApp
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QCoreApplication

class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.iniUI()
    def iniUI(self):
        exitAction = QAction(QIcon('logout.png'), 'Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit Application')
        exitAction.triggered.connect(self.btn_clicked)

        menubar = self.menuBar()
        #menubar.setNativeMenuBar(False)
        filemenu = menubar.addMenu('&File')
        filemenu.addAction(exitAction)

        button = QPushButton('Quit', self)
        button.move(50, 50)
        button.resize(button.sizeHint())
        button.clicked.connect(self.btn_clicked)

        self.setWindowTitle('My Qt App')
        self.setWindowIcon(QIcon('box.png'))
        self.setGeometry(100, 100, 640, 400)
        self.show()
    def btn_clicked(self):
        sys.exit(0)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    exit(app.exec_())