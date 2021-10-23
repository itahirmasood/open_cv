import cv2 as cv
import numpy as np
img=cv.imread('bhola.jpg')
cv.imshow('MachoMan',img)

gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('gray',gray)

#Laplocian
lap=cv.Laplacian(gray,cv.CV_64F)
lap=np.uint8(np.absolute(lap))
cv.imshow('Laplacian',lap)


# Sobel 
sobelx = cv.Sobel(gray, cv.CV_64F, 1, 0) #compute gradient along x axis
sobely = cv.Sobel(gray, cv.CV_64F, 0, 1) #gradient along y axis
combined_sobel = cv.bitwise_or(sobelx, sobely)

cv.imshow('Sobel X', sobelx)
cv.imshow('Sobel Y', sobely)
cv.imshow('Combined Sobel', combined_sobel)

#to compare wih canny
canny = cv.Canny(gray, 150, 175)
cv.imshow('Canny', canny)

cv.waitKey(0)