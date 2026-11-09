import cv2
import os
imagestore1=cv2.imread(r'C:\Python\Python\open cv\vibrant image2.jpg')
cv2.imshow('original image',imagestore1)
cv2.waitKey(0)     
print(imagestore1.shape)
shapestore=(imagestore1.shape)
rows=shapestore[0]
colums=shapestore[1]
rotate=cv2.getRotationMatrix2D((rows/2,colums/2),45,1)
rotatestore=cv2.wrapAffine(imagestore1,rotate,(rows,colums))
cv2.imshow('rotated image',rotatestore)
cv2.waitKey(0)