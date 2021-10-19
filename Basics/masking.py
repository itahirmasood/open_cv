import cv2 as cv
import numpy as np

img=cv.imread('bhola.jpg')
cv.imshow('MachoMan',img)

#mask size should same as your pixle [:2]
blank=np.zeros(img.shape[:2], dtype='uint8')
cv.imshow('Blank Image',blank)

circle=cv.circle(blank,(img.shape[1]//2,img.shape[0]//2),100,255,-1)
cv.imshow('Mask',circle)


masked=cv.bitwise_and(img,img,mask=circle)
cv.imshow('Masked image',masked)



cv.waitKey(0)