# widget_paint.py

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

import cv2
import numpy as np

class widget_paint(QWidget):
    def __init__(self, parent = None):
        QWidget.__init__(self, parent) 

        # setting geometry
        self.setGeometry(20, 20, 400, 400)
        
        # creating image object
        self.image = QImage(self.size(), QImage.Format_RGB32)

        # making image color to white
        self.image.fill(Qt.white)
        # variables
        # drawing flag
        self.drawing = False
        
        # default brush size
        self.brushSize = 40
        
        # default color
        self.brushColor = Qt.black
        
        # QPoint object to trace the point
        self.lastPoint = QPoint()

    # method for checking mouse cicks
    def mousePressEvent(self, event):
        # if left mouse button is pressed
        if event.button() == Qt.LeftButton:
            # make drawing flag true
            self.drawing = True
            # make last point to the point of cursor
            self.lastPoint = event.pos()

    # method for tracking mouse activity
    def mouseMoveEvent(self, event):		
        # checking if left button is pressed and drawing flag is true
        if (event.buttons() & Qt.LeftButton) & self.drawing:
            # creating painter object
            painter = QPainter(self.image)
			
            # set the pen of the painter
            painter.setPen(QPen(self.brushColor, self.brushSize,\
 		Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin))
			
            # draw line from the last point of cursor to the current point
	   # this will draw only one step
            painter.drawLine(self.lastPoint, event.pos())
			
	   # change the last point
            self.lastPoint = event.pos()
            # update
            self.update()    

    # method for mouse left button release
    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            # make drawing flag false
            self.drawing = False

    # paint event
    def paintEvent(self, event):
        # create a canvas
        canvasPainter = QPainter(self)
		
        # draw rectangle on the canvas
        canvasPainter.drawImage(self.rect(), self.image, \
            self.image.rect())

    def return_image(self):
        cv2.imwrite('test.png', self.QImageToCvMat(self.image))
    
    # method for clearing every thing on canvas
    def clear(self):
        # make the whole canvas white
        self.image.fill(Qt.white)
        # update
        self.update()
    
    # method for saving canvas
    def save(self):
        filePath, _ = QFileDialog.getSaveFileName(self, \
            "Save Image", "",\
            "PNG(*.png);;JPEG(*.jpg *.jpeg);;All Files(*.*) ")
        if filePath == "":
            return
        self.image.save(filePath)

    def QImageToCvMat(self,incomingImage):
        '''  Converts a QImage into an opencv MAT format  '''

        incomingImage = \
           incomingImage.convertToFormat(QImage.Format.Format_RGBA8888)

        width = incomingImage.width()
        height = incomingImage.height()

        ptr = incomingImage.bits()
        ptr.setsize(height * width * 4)
        arr = np.frombuffer(ptr, np.uint8).reshape((height, width, 4))
        return arr