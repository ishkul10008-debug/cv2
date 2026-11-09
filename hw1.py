import cv2
import os
imagestore1=cv2.imread(r'C:\Python\Python\open cv\vibrant image1.jpg')
# cv2.imshow('original image1',imagestore1)
# #cv2.waitKey(0)
gaussian=cv2.GaussianBlur(imagestore1,(5,5),0)
cv2.imshow('gaussian blur image',gaussian)
# cv2.waitKey(0)
# reflectiveborder=cv2.copyMakeBorder(gaussian,20,20,20,20,cv2.BORDER_REFLECT)
# cv2.imshow('reflective borderd  gaussian image image' ,reflectiveborder)
# cv2.waitKey(0)
median=cv2.medianBlur(imagestore1,(5))
cv2.imshow('median blur image',median)
cv2.waitKey(0)