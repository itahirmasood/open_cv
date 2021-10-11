import cv2 as cv
import numpy as np

img=cv.imread('bhola.jpg')
cv.imshow('MachoMan',img)

blank=np.zeros(img.shape,dtype='uint8')
cv.imshow('Blank',blank)
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Gray',gray)

blur=cv.GaussianBlur(gray,(5,5), cv.BORDER_DEFAULT)
cv.imshow('Blur',blur)

canny=cv.Canny(blur,125,175)  #Edge will decrease by sending a blur image
cv.imshow('canny edges',canny)

#another method to find contours
# ret, thresh=cv.threshold(gray,125,255,cv.THRESH_BINARY)
# cv.imshow('Thresh',thresh)

contours,hierarchies=cv.findContours(canny,cv.RETR_LIST,cv.CHAIN_APPROX_SIMPLE) #RETR_EXTERNal returns external contour while TREE or list will return all the contours.  #CHAIN APPROX SIMPLE compress all contour & return one that is simple/
print(f'{len(contours)} countour(s) found')  

#draw the contours on the blank pic
cv.drawContours(blank,contours,-1,(0,0,255),1) #How many contours to draw? -1 for all
cv.imshow('Contours Drawn',blank)

cv.waitKey(0)