import cv2 as cv
import numpy as np

haarCascade=cv.CascadeClassifier('haarFace.xml')
people = ['Ben Afflek', 'Elton John', 'Jerry Seinfield', 'Madonna', 'Mindy Kaling']
# np.load('features.npy',allow_pickle=True)
# np.load('labels.npy')


faceRecognizer= cv.face.LBPHFaceRecognizer_create()
faceRecognizer.read('faceTrained.yml')


# img=cv.imread(r'F:\Mission Learning\OpenCV\Faces\val\jerry_seinfeld\3.jpg')
img=cv.imread('aa.jpg')
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Person',gray)

#Detect the face in the image

facesRectangle=haarCascade.detectMultiScale(gray, 1.1,4)


# for (x,y,w,h) in facesRectangle:
#     facesROI=gray[y:y+h, x:x+w] #region of interest

#     #label,confidence=faceRecognizer.predict(facesROI)
#     label, confidence = faceRecognizer.predict(facesROI)
#     print(f'label={label} with cofidence of {confidence}')

#     cv.putText(img,str(people[label]),(20,20),cv.FONT_HERSHEY_COMPLEX,1.0,(0,255,0),thickness=2)
#     cv.rectangle(img,(x,y),(x+w,y+h),(0,255,0),thickness=2)

for (x,y,w,h) in facesRectangle:
    faces_roi = gray[y:y+h,x:x+w]
    label, confidence = faceRecognizer.predict(faces_roi)
    print(f'Label = {people[label]} with a confidence of {confidence}')

    cv.putText(img, str(people[label]), (20,20), cv.FONT_HERSHEY_COMPLEX, 1.0, (0,255,0), thickness=2)
    cv.rectangle(img, (x,y), (x+w,y+h), (0,255,0), thickness=2)

cv.imshow('Detected Face',img)

cv.waitKey(0)
