import cv2
import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt


def edge_detect(img , lower_thres , upper_thresh ,K , d_iter , e_iter):
	gray = cv2.GaussianBlur(img, (K, K), 0)

	edged = cv2.Canny(gray, lower_thres, upper_thresh)
	edged = cv2.dilate(edged, None, iterations= d_iter)
	edged = cv2.erode(edged, None, iterations= e_iter)


	return edged

"""

You have to Input the edge_detect output image to the Contour Input i.e Edged"""



def Contors(image ,edged, area_size):
	image_list = []

	cnts = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL,
	cv2.CHAIN_APPROX_SIMPLE)
	cnts = imutils.grab_contours(cnts)

	# sort the contours from left-to-right and initialize the
	# 'pixels per metric' calibration variable
	(cnts, _) = contours.sort_contours(cnts)
	


	# loop over the contours individually
	for c in cnts:
		# if the contour is not sufficiently large, ignore it
		if cv2.contourArea(c) < int(area_size):
			continue

		# compute the rotated bounding box of the contour
		orig = image.copy()
		box = cv2.minAreaRect(c)
		box = cv2.cv.BoxPoints(box) if imutils.is_cv2() else cv2.boxPoints(box)
		box = np.array(box, dtype="int")

		# order the points in the contour such that they appear
		# in top-left, top-right, bottom-right, and bottom-left
		# order, then draw the outline of the rotated bounding
		# box
		box = perspective.order_points(box)
		cv2.drawContours(orig, [box.astype("int")], -1, (255, 0, 0), 2)

		# loop over the original points and draw them
		for (x, y) in box:
			cv2.circle(orig, (int(x), int(y)), 5, (0, 255, 0), -1)


		cv2.imshow("Image_Countour" ,orig)
		cv2.waitKey(0)

		image_list.append(orig)	



	return image_list


