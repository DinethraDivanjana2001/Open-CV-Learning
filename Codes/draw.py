import cv2 as cv
import numpy as np

blank = np.zeros((500, 500, 3), dtype='uint8')
cv.imshow('Blank', blank)

# #1.paint the image circtain color                       
# blank[200:300,300:400] = 0,0,255
# cv.imshow('Green', blank) 

#2.Draw a rectangle 
# cv.rectangle(blank, (0,0), (250,250),(0,255,0),thickness = cv.FILLED)
#cv.rectangle(blank, (0,0), (250,250),(0,255,0),thickness = 2)
#cv.rectangle(blank, (0,0), (500,250),(0,255,0),thickness = 2)
# cv.rectangle(blank, (0,0), (250,250),(0,255,0),thickness = -1)
cv.rectangle(blank, (0,0), (blank.shape[1]//2,blank.shape[0]//2),(0,255,0),thickness = -1)

#Draw a circle


cv.imshow('Rectangle',  blank) 


cv.waitKey(0)                       