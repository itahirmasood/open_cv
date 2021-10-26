import cv2 as cv

img=cv.imread('crew.jpg')  #image path
cv.imshow('Crew',img)

gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('gray',gray)

haarCascade=cv.CascadeClassifier('haarFace.xml')

facesRectangle=haarCascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=1)

print(f'Number of Faces found={len(facesRectangle)}')

for (x,y,w,h) in facesRectangle:
    cv.rectangle(img,(x,y),(x+w,y+h),(0,255,0),thickness=2)

cv.imshow('Detected Faces',img)

cv.waitKey(0)