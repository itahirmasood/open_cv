import cv2 as cv

img=cv.imread('bhola.jpg')
cv.imshow('bhola',img)

#Converting to grayscale
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Gray',gray)

#blur
blur=cv.GaussianBlur(img,(3,3),cv.BORDER_DEFAULT) #kernel size should be in odd number (3,3)
cv.imshow('Blur',blur)


#edge cascade
canny=cv.Canny(img,125,175)  #Edge will be decrease by sending a Blur img
cv.imshow('canny edges',canny)


#dilating the image
dilated=cv.dilate(canny,(3,3),iterations=1)
cv.imshow('Dilated',dilated)


#eroding
eroded=cv.erode(dilated,(3,3),iterations=1)
cv.imshow('Eroded',eroded)


#Resize
resized=cv.resize(img,(500,500),interpolation=cv.INTER_CUBIC) #shrinking to smaller than original use INTER_AREA---& if you want enlarge the img then use INTER_LINEAR or INTER_CUBIC... cubic is better but slow
cv.imshow('Resized',resized) 


#Cropping
cropped=img[50:200,200:400] # Square bracket; not round
cv.imshow('Cropped',cropped)

cv.waitKey(0)