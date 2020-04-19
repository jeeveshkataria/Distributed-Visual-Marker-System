#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 01:56:18 2020

@author: jeevesh


step 1: enter course ID
step 2: load ta roll numbers and instructor of that course
step 3: enter ta roll number
step 4: match the TA roll number with the loaded rollnumber 
step 5: if (match) else close system send security message
step 6 :load all student roll number 
step 7 : loop
step 8 :take picture 
step 9 :predict picture
step 10: if (match) else ignore 
step 11 : mark attendance of that student  

"""
import sys
from termcolor import colored,cprint

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


class virtualAttendance:
    Model               =   None
    kerasPath           =   "./facenet_keras.h5"
    trainPath           =   "./train.pickle"
    testPath            =   "./test.pickle"
    trainLabelPath      =   "./train_labels.pickle"
    testLabelPath       =   "./test_labels.pickle"
    classifierPath      =    "./classifier.pickle"
    traincharan         =    None
    testcharan          =    None
    train_labels        =    None
    traincharan         =    None
    test_labels         =    None
    classifier          =    None
    studentID={}
    
    
    
    def verifyCourseIDandPassKey(self,courseID,PassKey):
        #check if courseID is in database course 
        #if(courseId is inside database)
        
                
        
               #load pass key
               
                #now take compare pass key
                #if(pass key match):
                    #return 1
                
                #else
                    #print("invalid TA credentials")
                    #return 0
            
            #else:
                #print("invalid course id")
                #return 0

                
    
        #else:
        #print("invalid course id")
        return 0
        
    
    def loadStudent(self,courseID):
        #load each studentID from database 
        #corresponding to that courseID
        #inside map [self.studentID] declared inside class
        
        #return studentID
        #we should return a dictionary which is having all 
        #students of that class
        
        return 0
    
    
    
    
    def markAttendance(self,predict):
        for student in predict:
            #check is student present in [StudentID] map or not
            #if present
            #load table 
            #mark present in that student
            
            
            
            #else
            #print("student not recognised")
        return 0
    
    
    
    
    
    
    
    def startAttendance(self,courseID,taID):
        cap = cv2.VideoCapture(0)
        while(True):
            ret,frame = cap.read()
            frame = cv2.cvtColor( frame , cv2.COLOR_BGR2RGB )
            face_array,x1_frame,y1_frame,x2_frame,y2_frame = charanfunctions.try_extract_face_webcam(frame)
            
            if len(face_array) == 0:
                print("No face Detected")
                continue
            for face in range(len(face_array)):
                predict = charanfunctions.try_performTestcharan(self.model,self.traincharan,face_array[face],self.classifier)
                
                if (len(predict)) == 0:
                    print(" face Not Recognized")
                    continue
                
                
                
                self.markAttendance(predict)
                
                print(predict)
                color =  (0 , 0, 255)
                stroke = 5
                cv2.rectangle(frame , (x1_frame[face],y1_frame[face]) ,(x2_frame[face],y2_frame[face]),color,stroke)
    
            cv2.imshow('frame',frame)
            if cv2.waitKey(20) & 0xFF == ord('q'):
                break

        cap.release()
        cv2.destroyAllWindows()
    
    
    def loadModule(self):
        self.model = load_model(self.kerasPath,compile=False)
        print("model loaded")
        
        with open(self.trainPath, 'rb') as f:
            self.traincharan = pickle.load(f)
        print("traincharan loaded")

        with open(self.testPath, 'rb') as f:
            self.testcharan = pickle.load(f)
        print("testcharan loaded")

        with open(self.trainLabelPath, 'rb') as f:
            self.train_labels = pickle.load(f)
        print("train_labels loaded")

        with open(self.testLabelPath, 'rb') as f:
            self.test_labels = pickle.load(f)
        print("test_labels loaded")

        with open(self.classifierPath, 'rb') as f:
            self.classifier = pickle.load(f)
        print("classifier loaded")

        
        

    
    
    
    
    
    
    
    
    
    
    
    
cprint("Attendance System Initiated", 'green', attrs=['reverse', 'bold'])
courseID   =    input("Enter Course ID : ")
PassKey       =    input("Enter pass key for user : ") 
virtualAtt  =    virtualAttendance()

if ( virtualAtt.verifyCourseIDandPassKey(courseID,PassKey) ):
    
    if ( virtualAtt.loadStudent(courseID) ):
        
        if( virtualAtt.loadModule() ):
            
            if ( virtualAtt.startAttendance() ):
                print("Attendance Completed")
                exit()
            else:
                cprint("Some Internal Error occurs with the module,please re-start again" ,'red', attrs=['reverse', 'bold'])
                exit()
                
        
        
        
        else:
            cprint("Some Internal Error occurs with the module,please re-start again" ,'red', attrs=['reverse', 'bold'])
            exit()
        
        
    else:
        cprint("Problem In Loading Student,Contact DataBase Administrator", 'red', attrs=['reverse', 'blink'])
        exit()
        
    
else:
    cprint("Input Values is not valid,Start the Module again", 'red', attrs=['reverse', 'blink'])
    exit()