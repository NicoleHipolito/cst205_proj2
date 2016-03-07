import numpy as np
import cv2

frontFaceCascade = cv2.CascadeClassifier('Cascades/haarcascade_frontalface_default.xml')
altFrontFaceCascade = cv2.CascadeClassifier('Cascades/haarcascade_frontalface_alt.xml')
eyeCascade = cv2.CascadeClassifier('Cascades/haarcascade_eye.xml')
rightEyeCascade = cv2.CascadeClassifier('Cascades/haarcascade_mcs_righteye.xml')
leftEyeCascade = cv2.CascadeClassifier('Cascades/haarcascade_mcs_lefteye.xml')
noseCascade = cv2.CascadeClassifier('Cascades/haarcascade_mcs_nose.xml')
rightEarCascade = cv2.CascadeClassifier('Cascades/haarcascade_mcs_rightear.xml') 
leftEarCascade = cv2.CascadeClassifier('Cascades/haarcascade_mcs_leftear.xml')`
mouthCascade = cv2.CascadeClassifier('Cascades/haarcascade_mcs_maouth.xml')
smileCascade = cv2.CascadeClassifier('Cascades/haarcascade_smile.xml')


img = cv2.imread('cringe.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = frontFaceCascade.detectMultiScale(gray, 1.3, 5)
nose = noseCascade.detectMultiScale(gray, 1.3, 5)

"""
cv.Rectangle(img, pt1, pt2, color, thickness=1, lineType=8, shift=0) None
Parameters:	
img - Image
pt1 - Vertex of the rectangle.
pt2 - Vertex of the rectangle opposite to pt1 .
rec - Alternative specification of the drawn rectangle.
color - Rectangle color or brightness (grayscale image).
thickness - Thickness of lines that make up the rectangle. Negative values, like CV_FILLED , mean that the function has to draw a filled rectangle.
lineType - Type of the line. See the line() description.
shift - Number of fractional bits in the point coordinates.
"""
for(x, y, w, h) in faces:
	cv2.rectangle(img, (x, y), (x+w, y+h), (225, 0, 0), 2)
	reColor = img[y:y+h, x:x+w]
for(x, y, w, h) in nose: 
	cv2.rectangle(img, (x+5, y-50), ((x+10)+(w-5), (y-22)+h), (225, 0, 0), 2)
	reColor = img[y:y+h, x:x+w]

#Do research on: how to insert a matrix data into another matrix.

cv2.imwrite("newImage.jpg", img)
