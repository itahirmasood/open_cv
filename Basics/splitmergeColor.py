import cv2 as cv
import numpy as np


img=cv.imread('bhola.jpg')
cv.imshow('MachoMan',img)

blank=np.zeros(img.shape[:2],dtype='uint8')



b,g,r=cv.split(img)

#to see colors of each color sepately
blue=cv.merge([b,blank,blank])
green=cv.merge([blank,g,blank])
red=cv.merge([blank,blank,r])

cv.imshow('Blue',blue)
cv.imshow('Green',green)
cv.imshow('Red',red)

#it will show in grayscale
# cv.imshow('Blue',b)
# cv.imshow('Green',g)
# cv.imshow('Red',r)

print(img.shape)
print(b.shape)
print(g.shape)
print(r.shape)

#merge back to original 
merged=cv.merge([b,g,r])
cv.imshow('merged',merged)


cv.waitKey(0)