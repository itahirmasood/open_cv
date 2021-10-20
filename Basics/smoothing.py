import cv2 as cv

img=cv.imread('bhola.jpg')
cv.imshow('MachoMan',img)

#averaging by surrounding pixels
average=cv.blur(img,(3,3))
cv.imshow('Average Blur',average)


#Guassian Blurr- more natural than blur
gauss=cv.GaussianBlur(img,(3,3),0)
cv.imshow('Guassian',gauss)

#Median Blurr
median=cv.medianBlur(img,3)
cv.imshow('Median',median)


#Bilateral Blur
bilateral=cv.bilateralFilter(img,10,35,25)
cv.imshow('Bilateral',bilateral)



cv.waitKey(0)