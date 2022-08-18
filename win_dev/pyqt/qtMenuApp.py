'''
PyQt5 예제 소스
1. 필요라이브러리 설치
pip install PyQt5 [--no-warn-script-location]
'''
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QDesktopWidget, QPushButton, QToolTip, QMainWindow, QAction, qApp
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtGui import QIcon, QFont

class MyApp(QMainWindow):
   
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        strTooltip = 'This is a <b>QWidget</b> widget'

        exitAction = QAction(QIcon('exit.png'), 'Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(qApp.quit)

        self.statusBar() # .showMessage('Ready')

        self.toolbar = self.addToolBar('Exit')
        self.toolbar.addAction(exitAction)

        menubar = self.menuBar()
        menubar.setNativeMenuBar(False)
        filemenu = menubar.addMenu('&File')
        filemenu.addAction(exitAction)
        editmenu = menubar.addMenu('&Edit')
        viewmenu = menubar.addMenu('&View')
        toolmenu = menubar.addMenu('&Tool')
        helpmenu = menubar.addMenu('&Help')

        QToolTip.setFont(QFont('NanumGothic', 10))
        self.setToolTip('Menubar App')

        btn = QPushButton('Quit', self)
        btn.setToolTip(strTooltip)
        # btn.move(530, 340)
        btn.move(10, 100)
        btn.resize(btn.sizeHint())
        btn.clicked.connect(QCoreApplication.instance().quit)

        self.setWindowTitle('Hugo QtApp')
        self.setWindowIcon(QIcon('earth.png'))
        # self.setGeometry(300, 300, 640, 400)
        self.resize(640, 400)
        self.center()
        self.show()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())