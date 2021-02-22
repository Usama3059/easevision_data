import cv2 as cv 
import numpy 



def BG_image(img , type_alg):
	if type_alg == 'MOG2':
		backSub = cv.createBackgroundSubtractorMOG2()
	else:
		backSub = cv.createBackgroundSubtractorKNN()
	

	frame = img.copy()

	fgMask = backSub.apply(frame)


	cv.rectangle(frame, (10, 2), (100,20), (255,255,255), -1)
	# cv.putText(frame, , (15, 15),
	#        cv.FONT_HERSHEY_SIMPLEX, 0.5 , (0,0,0))


	return frame


def BG_video(video_path , type_alg):


	if type_alg == 'MOG2':
	    backSub = cv.createBackgroundSubtractorMOG2()
	else:
	    backSub = cv.createBackgroundSubtractorKNN()
	capture = cv.VideoCapture(cv.samples.findFileOrKeep(video_path))
	if not capture.isOpened():
	    st.text("Video is not load")
	while True:
	    ret, frame = capture.read()
	    if frame is None:
	        break
	    
	    fgMask = backSub.apply(frame)
	    
	    
	    cv.rectangle(frame, (10, 2), (100,20), (255,255,255), -1)
	    cv.putText(frame, str(capture.get(cv.CAP_PROP_POS_FRAMES)), (15, 15),
	               cv.FONT_HERSHEY_SIMPLEX, 0.5 , (0,0,0))
	    
	    
	return frame