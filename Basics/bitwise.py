import cv2 as cv
import numpy as np
# img=cv.imread('bhola.jpg')
# cv.imshow('MachoMan',img)

blank=np.zeros((400,400),dtype='uint8')

rectangle=cv.rectangle(blank.copy(),(30,30),(370,370),255,-1)
circle=cv.circle(blank.copy(),(200,200),200,255,-1)

cv.imshow('Rectangle',rectangle)
cv.imshow('Circle',circle)

# bitwise AND  -->>intersecting regions
bitwiseAND=cv.bitwise_and(rectangle,circle)
cv.imshow('AND',bitwiseAND)

# bitwise OR  -->both intersecting & non-intersecting
bitwiseOR=cv.bitwise_or(rectangle,circle)
cv.imshow('OR',bitwiseOR)

# bitwise XOR -->non intersecting region
bitwiseXOR=cv.bitwise_xor(rectangle,circle)
cv.imshow('XOR',bitwiseXOR)


# bitwise NOT
bitwiseNOT=cv.bitwise_not(rectangle)
cv.imshow('NOT Rectangle',bitwiseNOT)
cv.waitKey(0)


# bitwise NOT--> inverse
bitwiseNOT=cv.bitwise_not(circle)
cv.imshow('NOT Circle',bitwiseNOT)
cv.waitKey(0)