import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

def thresh(img , thresh_type , min_value):
	img = cv.medianBlur(img,5)
	if thresh_type == "Binary threshold":
		ret,thresh1 = cv.threshold(img,min_value,255,cv.THRESH_BINARY)
	if thresh_type == "Binary threshold_inv":
		ret,thresh1 = cv.threshold(img,min_value,255,cv.THRESH_BINARY_INV)
	if thresh_type == "Trunc threshold":
		ret,thresh1 = cv.threshold(img,min_value,255,cv.THRESH_TRUNC)
	if thresh_type == "Trunc threshold_tozero":

		ret,thresh1 = cv.threshold(img,min_value,255,cv.THRESH_TOZERO)
	if thresh_type == "Trunc threshold_tozero_inv":

		ret,thresh1 = cv.threshold(img,min_value,255,cv.THRESH_TOZERO_INV)

	if thresh_type == "Adaptive_meanc":
		thresh1 = cv.adaptiveThreshold(img,255,cv.ADAPTIVE_THRESH_MEAN_C,\
		            cv.THRESH_BINARY,11,2)
	if thresh_type == "Adaptive_mean_gussian_c":
		thresh1 = cv.adaptiveThreshold(img,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,\
		            cv.THRESH_BINARY,11,2)
	final_thresh = thresh1
	cv.imshow("threshold" , final_thresh)
	cv.waitKey(0)
	
	return thresh1
