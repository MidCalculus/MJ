import cv2
import os
print(os.getcwd())

face_cascade = cv2.CascadeClassifier('./projects/face_detection/face_detector.xml')

img = cv2.imread('./projects/face_detection/1.jpg')

faces = face_cascade.detectMultiScale(img, 1.1, 4)

for (x, y, w, h) in faces: 
  cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
cv2.imwrite("./projects/face_detection/face_detected.png", img) 
print('Successfully saved')

import numpy as np
import pandas as pd

data = pd.read_csv("Seattle2014.csv")
print(data.head())

rainfall = data["PRCP"].values
inches = rainfall/254
print(inches.shape)

import matplotlib.pyplot as plt
import seaborn
seaborn.set()
plt.hist(inches, 40)
plt.show()
