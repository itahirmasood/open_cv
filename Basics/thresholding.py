import cv2 as cv

img=cv.imread('bhola.jpg')
cv.imshow('MachoMan',img)



gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('gray',gray)

#simple thresholding
threshold,thresh=cv.threshold(gray,150,255,cv.THRESH_BINARY)
cv.imshow('Simple Thresh',thresh)

# thresholding inverse
threshold,threshINV=cv.threshold(gray,150,255,cv.THRESH_BINARY_INV)
cv.imshow('Thresh Inverse',threshINV)

#adaptive Thresholding
adaptiveThresh=cv.adaptiveThreshold(gray,255,cv.ADAPTIVE_THRESH_MEAN_C,cv.THRESH_BINARY,11,3)
cv.imshow('Adaptive Thresh',adaptiveThresh)

cv.waitKey(0)