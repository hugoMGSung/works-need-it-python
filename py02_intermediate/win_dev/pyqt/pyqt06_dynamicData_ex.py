# QT Designer 연동 소스
from PyQt5 import QtGui, QtWidgets, uic
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys
from naverSearch import *
import os

class MyApp(QWidget):
    btn_num = 0
    rows = 0
    
    def __init__(self):
        super().__init__()
        uic.loadUi('d:/01_Programming/100_HugoBank/Mine/works-need-it-python/win_dev/pyqt/ui/dynDataApp.ui', self)
        
        #ui에 있는 위젯하고 시그널 처리(컨트롤 이벤트처리)
        self.btnAddItem.clicked.connect(self.btnAddItem_Clicked)
        self.button_row = 0
        self.button_column = 0
        
        self.initTable()
        
    def btnAddItem_Clicked(self):       
        self.tblResult.setRowCount(self.rows + 1)
        self.tblResult.setItem(self.rows, 0, QTableWidgetItem("내용 블라블라블라"))
        self.btn_num += 1
        
        self.btn_cell = QPushButton(f'Del {self.btn_num}')
        self.btn_cell.button_row = self.rows
        self.btn_cell.button_column = 1
        self.btn_cell.clicked.connect(self.cellButtonClicked)
        self.tblResult.setCellWidget(self.rows, 1, self.btn_cell)
        self.rows += 1     
        print(self.rows)   
        
    def cellButtonClicked(self):
        button = self.sender()
        if button:
            print(button.button_row)
            print(button.button_column)
        
            row = self.tblResult.indexAt(button.pos()).row()
            self.tblResult.removeRow(row)
            self.rows -= 1
            self.tblResult.setRowCount(self.rows)
        
                    
    def initTable(self):
        self.tblResult.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tblResult.setColumnCount(2)

        self.tblResult.setHorizontalHeaderLabels(['첫번째', '두번째'])
        self.tblResult.setColumnWidth(0, 300)
        self.tblResult.setColumnWidth(1, 60)
    
if __name__ == '__main__':
    # path = os.path.dirname(os.path.abspath(__file__))
    # print(path)
    
    app = QApplication(sys.argv)
    win = MyApp()
    win.show()
    sys.exit(app.exec_())