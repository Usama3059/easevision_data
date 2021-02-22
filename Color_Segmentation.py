import cv2 as cv 
import numpy as np



def hsv_color(img , h1,s1,v1 , h2 , s2 , v2):
	frame = img.copy()
	hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
	lower_blue = np.array([h1,s1,v1])
	upper_blue = np.array([h2,s2,v2])
	mask = cv.inRange(hsv, lower_blue, upper_blue)
	res = cv.bitwise_and(frame,frame, mask= mask)
	return res