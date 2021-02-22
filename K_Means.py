import cv2 
import numpy as np 

def k_means(img , K,max_iter , epsilon):
	Z = img.reshape((-1,3))
	# convert to np.float32
	Z = np.float32(Z)
	
	# define criteria, number of clusters(K) and apply kmeans()
	criteria = (cv.TERM_CRITERIA_EPS + cv.TERM_CRITERIA_MAX_ITER, max_iter, epsilon)
	
	ret,label,center=cv.kmeans(Z,K,None,criteria,10,cv.KMEANS_RANDOM_CENTERS)
	# Now convert back into uint8, and make original image
	center = np.uint8(center)
	res = center[label.flatten()]
	res2 = res.reshape((img.shape))
	cv2.imshow("K_means" , res2 )
	cv2.waitKey(0)

	return res2