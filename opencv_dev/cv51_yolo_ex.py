### 수정요
import cv2
import numpy as np

# Load YOLO network
net = cv2.dnn.readNet("./data/yolov3.weights", "./data/yolov3.cfg")
classes = [] 
with open("./data/coco.names", "r") as f: 
    classes = [line.strip() for line in f.readlines()] 
layer_names = net.getLayerNames() 
output_layers = [layer_names[i[0] - 1] for i in net.getUnconnectedOutLayers()] 
colors = np.random.uniform(0, 255, size=(len(classes), 3))

# Loading image 
img = cv2.imread("room_ser.jpg") 
img = cv2.resize(img, None, fx=0.4, fy=0.4) 
height, width, channels = img.shape