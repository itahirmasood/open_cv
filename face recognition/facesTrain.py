

import os
import cv2 as cv
import numpy as np

people = ['Ben Afflek', 'Elton John', 'Jerry Seinfield', 'Madonna', 'Mindy Kaling']
DIR = r'F:\Mission Learning\OpenCV\Faces\train'

haar_cascade = cv.CascadeClassifier('haarFace.xml')

features = []
labels = []

def create_train():
    for person in people:
        path = os.path.join(DIR, person)
        label = people.index(person)

        for img in os.listdir(path):
            imgPath = os.path.join(path,img)

            imgArray = cv.imread(imgPath)
            if imgArray is None:
                continue 
                
            gray = cv.cvtColor(imgArray, cv.COLOR_BGR2GRAY)

            faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=4)

            for (x,y,w,h) in faces_rect:
                faces_roi = gray[y:y+h, x:x+w]
                features.append(faces_roi)
                labels.append(label)

create_train()
print('Training Completed')

features = np.array(features, dtype='object')
labels = np.array(labels)

faceRecognizer = cv.face.LBPHFaceRecognizer_create()

# Train the Recognizer on the features list and the labels list
faceRecognizer.train(features,labels)

faceRecognizer.save('faceTrained.yml')
np.save('features.npy', features)
np.save('labels.npy', labels)

cv.waitKey(0)