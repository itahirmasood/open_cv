import cv2 as cv

# import matplotlib.pyplot as plt  #Inverse of openCV, it has RGB colors instead of BGR
# plt.imshow(img)
img=cv.imread('bhola.jpg')
cv.imshow('MachoMan',img)


#BGR to Grayscale
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Gray',gray)

#BGR to HSV
hsv=cv.cvtColor(img,cv.COLOR_BGR2HSV)
cv.imshow('Hsv',hsv)

# BGR to L.a.b
lab=cv.cvtColor(img,cv.COLOR_BGR2LAB)
cv.imshow('lab',lab)

#BGR to RGB
rgb=cv.cvtColor(img,cv.COLOR_BGR2RGB)
cv.imshow('RGB',rgb)


cv.waitKey(0)