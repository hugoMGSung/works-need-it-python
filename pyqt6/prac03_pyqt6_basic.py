import sys
from PyQt6.QtWidgets import QWidget, QPushButton, QApplication

class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):

        qbtn = QPushButton('Exit', self)
        qbtn.clicked.connect(QApplication.instance().quit)
        qbtn.setToolTip('This is a <b>QPushButton</b> widget. If you click, It\'ll be exit the program.')
        qbtn.resize(qbtn.sizeHint())
        qbtn.move(50, 50)

        self.setGeometry(300, 300, 350, 250)
        self.setWindowTitle('Exit example')
        self.show()

def main():

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()