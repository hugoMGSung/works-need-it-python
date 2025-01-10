#identify_digit.py
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.uic import loadUi
from PyQt5 import uic
from matplotlib.backends.backend_qt5agg import (NavigationToolbar2QT as NavigationToolbar)
from widget_paint import widget_paint
from PIL import ImageGrab, Image
import numpy as np
from tensorflow.keras.models import load_model

import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.datasets import mnist
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, Flatten
from tensorflow.keras.layers import Conv2D, MaxPooling2D
from tensorflow.keras import backend as K

import cv2
import imutils
import scipy
from imutils.perspective import four_point_transform
from scipy import ndimage

form_class = uic.loadUiType('./py03_advanced/pyqt5/predict_mnist.ui')[0]

class IdentifyDigit(QMainWindow, form_class):   
    def __init__(self):       
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('Predicting Digits with CNN')
        self.setFixedSize(QSize(880, 540))

        self.pbTrain.clicked.connect(self.load_train)
        self.pbClear.clicked.connect(self.clear_canvas)
        self.pbSave.clicked.connect(self.save_canvas)

        self.pbPredict.clicked.connect(self.classify_handwriting)

        self.clear_canvas()

    # method for clearing every thing on canvas
    def clear_canvas(self):
        self.widgetDigit = widget_paint(self)
        self.widgetDigit.clear()
        self.widgetDigit.show()

    # method for saving image on canvas
    def save_canvas(self):
        self.widgetDigit.save()

    def load_train(self):
        #Loads data and trains model
        # the data, split between train and test sets
        (x_train, y_train), (x_test, y_test) = mnist.load_data()
        print(x_train.shape, y_train.shape)

        #Preprocesses the data
        x_train = x_train.reshape(x_train.shape[0], 28, 28, 1)
        x_test = x_test.reshape(x_test.shape[0], 28, 28, 1)
        input_shape = (28, 28, 1)

        # convert class vectors to binary class matrices
        y_train = keras.utils.to_categorical(y_train, num_classes=None)
        y_test = keras.utils.to_categorical(y_test, num_classes=None)
        x_train = x_train.astype('float32')
        x_test = x_test.astype('float32')
        x_train /= 255
        x_test /= 255
        print('x_train shape:', x_train.shape)
        print(x_train.shape[0], 'train samples')
        print(x_test.shape[0], 'test samples')

        #Creates the model
        batch_size = 128
        num_classes = 10
        epochs = 10

        model = Sequential()
        model.add(Conv2D(32, kernel_size=(3, 3),\
            activation='relu',input_shape=input_shape))
        model.add(Conv2D(64, (3, 3), activation='relu'))
        model.add(MaxPooling2D(pool_size=(2, 2)))
        model.add(Dropout(0.25))
        model.add(Flatten())
        model.add(Dense(256, activation='relu'))
        model.add(Dropout(0.5))
        model.add(Dense(num_classes, activation='softmax'))

        model.compile(loss=keras.losses.categorical_crossentropy,\
            optimizer=keras.optimizers.Adadelta(),metrics=['accuracy'])

        #Trains the model
        hist = model.fit(x_train, y_train,\
            batch_size=batch_size,epochs=epochs,verbose=1,\
            validation_data=(x_test, y_test))
        print("The model has successfully trained")

        model.save('mnist.h5')
        print("Saving the model as mnist.h5")

        #Evaluates the model
        score = model.evaluate(x_test, y_test, verbose=0)
        print('Test loss:', score[0])
        print('Test accuracy:', score[1])
            
        self.pbTrain.setEnabled(False)
    
    ## 첫번째 작업업
    # def predict_digit(self, img):
    #     model = load_model('mnist.h5')

    #     #resize image to 28x28 pixels
    #     img = img.resize((28,28))
        
    #     #convert rgb to grayscale
    #     img = img.convert('L')
    #     img = np.array(img)
        
    #     #reshaping to support our model input and normalizing
    #     img = img.reshape(1,28,28,1)
    #     img = img/255.0        
            
    #     #predicting the class
    #     res = model.predict([img])[0]
    #     return np.argmax(res), max(res)

    def predict_digit(self, img):  
        model = load_model('mnist.h5')
            
        #Normalize image to range [0 1]
        img = cv2.normalize(img, None, alpha=0, beta=1, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_32F)

        #Reshapes image
        img = img.reshape(1,28,28,1)       
            
        #predicting the class
        res = model.predict([img])[0]
        return np.argmax(res), max(res)   
    
    def classify_handwriting(self):
        self.widgetDigit.return_image()        
        #im = Image.open("test.png")
        im = self.imageprepare('test.png')
        digit, acc = self.predict_digit(im)
        self.lblPredict1.setText('Predicted= '+str(digit))
        self.lblPredict2.setText('Accuracy= '+ str(int(acc*100)))

    # 이미지 개선
    def imageprepare(self,fileName):       
        image = cv2.imread(fileName)
        #Invert image to get whie digit on black background
        image = cv2.bitwise_not(image)
        #Converts image to grayscale
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        #resizes image to be 28x28
        (thresh, gray) = cv2.threshold(gray, 128, 255, \
            cv2.THRESH_BINARY | cv2.THRESH_OTSU)
        
        #First you need to fit the images into this 20x20 pixel box. 
        #Therefore you need to remove every row and column at the sides 
        #of the image which are completely black.
        while np.sum(gray[0]) == 0:
            gray = gray[1:]

        while np.sum(gray[:, 0]) == 0:
            gray = np.delete(gray, 0, 1)

        while np.sum(gray[-1]) == 0:
            gray = gray[:-1]

        while np.sum(gray[:, -1]) == 0:
            gray = np.delete(gray, -1, 1)

        rows, cols = gray.shape

        #Now you can resize our outer box to fit it into a 20x20 box. 
        #You need a resize factor for this.
        if rows > cols:
            factor = 20.0 / rows
            rows = 20
            cols = int(round(cols * factor))
            gray = cv2.resize(gray, (cols, rows))

        else:
            factor = 20.0 / cols
            cols = 20
            rows = int(round(rows * factor))
            gray = cv2.resize(gray, (cols, rows))

        #At the end ye need a 28x28 pixel image so we add the missing 
        #black rows and columns 
        #using the np.lib.pad function which adds 0s to the sides.
        colsPadding = (int(np.math.ceil((28 - cols) / 2.0)), \
            int(np.math.ceil((28 - cols) / 2.0)))
        rowsPadding = (int(np.math.ceil((28 - rows) / 2.0)), \
            int(np.math.ceil((28 - rows) / 2.0)))
        gray = np.lib.pad(gray, (rowsPadding, colsPadding), 'constant')
        #gray = np.lib.pad(gray, 2, 'constant',constant_values=255)
            
        shiftx, shifty = self.getBestShift(gray)
        shifted = self.shift(gray, shiftx, shifty)
        gray = shifted 
        gray = cv2.resize(gray, (28, 28))
        cv2.imwrite("result.png", gray)
        return gray       
            
    def getBestShift(self,img):
        cy, cx = ndimage.measurements.center_of_mass(img)

        rows, cols = img.shape
        shiftx = np.round(cols / 2.0 - cx).astype(int)
        shifty = np.round(rows / 2.0 - cy).astype(int)

        return shiftx, shifty

    def shift(self,img, sx, sy):
        rows, cols = img.shape
        M = np.float32([[1, 0, sx], [0, 1, sy]])
        shifted = cv2.warpAffine(img, M, (cols, rows))
        return shifted


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    ex = IdentifyDigit()
    ex.show()
    app.exec_()