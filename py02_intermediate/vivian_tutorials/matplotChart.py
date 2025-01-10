from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.uic import loadUi
from matplotlib.backends.backend_qt5agg import (NavigationToolbar2QT as NavigationToolbar)

import numpy as np
     
class matplotChart(QMainWindow):   
    def __init__(self):
        
        QMainWindow.__init__(self)
        loadUi('./ui/matplot_ui.ui', self)

        self.setWindowTitle('PyQt & MatplotLib Chart')
        self.pbView.clicked.connect(self.view_chart)
        self.addToolBar(NavigationToolbar(self.wdgChart.canvas, self))
        self.setFixedSize(QSize(630, 450))

    def view_chart(self):
        x = np.arange(0, 10, 0.2)
        y = np.sin(x)
        self.wdgChart.canvas.sumbu1.clear()
        self.wdgChart.canvas.sumbu1.plot(x, y, linewidth=3.0)
        self.wdgChart.canvas.sumbu1.set_ylabel('Y', color='blue')
        self.wdgChart.canvas.sumbu1.set_xlabel('X', color='blue')
        self.wdgChart.canvas.sumbu1.set_title('Simple Sin Chart')
        self.wdgChart.canvas.sumbu1.set_facecolor('xkcd:wheat')
        self.wdgChart.canvas.sumbu1.grid()
        self.wdgChart.canvas.draw()
               
if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    ex = matplotChart()
    ex.show()
    sys.exit(app.exec_())