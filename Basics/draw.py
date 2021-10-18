import cv2 as cv
import numpy as np


blank=np.zeros((500,500,3),dtype='uint8')
cv.imshow('Blank',blank)



#we will not use this one
#img=cv.imread('bhola.jpg')
#cv.imshow('Bhola',img)


#1 paint img in certain color
#blank[:]=0,255,0
#blank[200:300,300:400]=0,255,0
#cv.imshow('Green',blank)

#2 Draw Rectangle
#cv.rectangle(blank,(0,0),(350,300),(0,255,0),thickness=2) #thickness=FILLED or thickness=-1 will make it filled
 #OR 
cv.rectangle(blank,(0,0),(blank.shape[1]//2,blank.shape[0]//2),(0,255,0),thickness=2) #thickness=FILLED or thickness=-1 will make it filled
cv.imshow('Rectangle',blank)


#3 Draw circle
cv.circle(blank,(blank.shape[1]//2,blank.shape[0]//2),40,(0,255,0),thickness=2)
cv.imshow('Circle',blank)

#4 Draw Line
cv.line(blank,(0,0),(blank.shape[1]//2,blank.shape[0]//2),(255,255,255),thickness=2) #thickness=FILLED or thickness=-1 will make it filled
cv.imshow('Line',blank)

#5 Write Text
cv.putText(blank,'hola',(300,300),cv.FONT_HERSHEY_TRIPLEX,1.5,(0,255,0),thickness=2)
cv.imshow('Text',blank)

cv.waitKey(0)