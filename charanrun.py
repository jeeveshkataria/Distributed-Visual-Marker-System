#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ReadMe:
How to run this program?
We need following files in our current working directory
1.charanfunctions.pt
2.classifier.pickle
3.train.pickle
4.test.pickle
5.train_labels.pickle
6.text_labels.pickle
7.facenet_keras.h5

plase check the relative path according to your systems

"""



import charanfunctions
# charan functions is an other python file,which is imported here

import numpy as np
import cv2
from PIL import Image
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import Normalizer
from sklearn.neighbors import KNeighborsClassifier
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from numpy import asarray
from mtcnn.mtcnn import MTCNN
import os
from os.path import isdir
from os import listdir
from numpy import asarray
from matplotlib import pyplot
from mtcnn.mtcnn import MTCNN
from numpy import load
from numpy import expand_dims
from numpy import asarray
from numpy import savez_compressed
from keras.models import load_model
import pickle



# set path to load files

kerasPath           = "./facenet_keras.h5"
trainPath           ="./train.pickle"
testPath            ="./test.pickle"
trainLabelPath      ="./train_labels.pickle"
testLabelPath       ="./test_labels.pickle"
classifierPath      ="./classifier.pickle"







from keras.models import load_model
# load the model
model = load_model(kerasPath,compile=False)


print("model loaded")


with open(trainPath, 'rb') as f:
  traincharan = pickle.load(f)

print("traincharan loaded")


with open(testPath, 'rb') as f:
  testcharan = pickle.load(f)

print("testcharan loaded")



with open(trainLabelPath, 'rb') as f:
  train_labels = pickle.load(f)

print("train_labels loaded")


with open(testLabelPath, 'rb') as f:
  test_labels = pickle.load(f)

print("test_labels loaded")



with open(classifierPath, 'rb') as f:
  classifier = pickle.load(f)


print("classifier loaded")








cap = cv2.VideoCapture(0)


while(True):
    ret,frame = cap.read()
    
    #frame = cv2.imread(random)
    
    frame = cv2.cvtColor( frame , cv2.COLOR_BGR2RGB )
    
    #function to detect faces in image
    #it should return value in faces 
    #faces is list
    #faces = face_cascade.detectMultiScale( gray , scaleFactor=1.5 , minNeighbors  = 5)
    
    face_array,x1_frame,y1_frame,x2_frame,y2_frame = charanfunctions.try_extract_face_webcam(frame)
    
    if len(face_array) == 0:
        print("No face Detected")
        continue
    
    for face in range(len(face_array)):
        predict = charanfunctions.try_performTestcharan(model,traincharan,face_array[face],classifier)
        
        
        if (len(predict)) == 0:
            print(" face Not Recognized")
            continue
        
        print(predict)
        color =  (0 , 0, 255)
        #width of rectangle shown in display
        stroke = 5
        #dram rectangle
        cv2.rectangle(frame , (x1_frame[face],y1_frame[face]) ,(x2_frame[face],y2_frame[face]),color,stroke)
    
    
    
    

    
    
    
    
    
    
    
    
    
    
    
    
    
#    predict,x1,y1,x2,y2 = charanfunctions.performTestcharan(model,traincharan,train_labels,frame,classifier)
    
    
    
#    if (len(predict)) == 0:
#        print("No face found")
#        continue
    
  
#    print(predict)
        
    
    #color of rectangle shown in display
#    color =  (0 , 0, 255)
    #width of rectangle shown in display
#    stroke = 5
    #dram rectangle
#    cv2.rectangle(frame , (x1,y1) ,(x2,y2),color,stroke)
        
        
        
        
    
    
    
    
    cv2.imshow('frame',frame)
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()