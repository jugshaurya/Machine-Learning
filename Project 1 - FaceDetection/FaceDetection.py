'''
	Detecting Face using old Method (HaarCascade Classifier), New Being Using CNN's
	
	Haar-Cascade Classifer is a classifer trained already trained on a dataset of frames (some have Faces and some don't)
	to detect where the Face is located in the entire frame DataSet
'''

import cv2

camera = cv2.VideoCapture(0)

# 1. Loading the HaarCascade Classifer strored locally in same Folder as a Xml file
face_detector = cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')
# similarly we have eye detector
eye_detector = cv2.CascadeClassifier('haarcascade_eye.xml')

while True:
	# frame capturing
	successful,frame =  camera.read() # retruns the tuple (success,frameORframe)
	if successful is False:
		continue

	# 2. we need to scale our frame so that it can be passes to classifier
	# we do it using detectMultiScale(frame, scale_factor, minNeighbours)
	cordinates = face_detector.detectMultiScale(frame,1.3,5) # detecting and scalling by 30% with 5 neighbours 
	# and returning the cordinates of faces as Rectangel cords : (x,y,width,height)
	eyes =  eye_detector.detectMultiScale(frame,1.3,6)

	# 3. Drawing a Rectangle(img,pt1,pt2,color,thickness) for each face  in our frame
	for (x,y,w,h) in cordinates:
		cv2.rectangle(frame,(x,y), (x+w,y+h) ,(255,0,0), 4)
	
	for (x,y,w,h) in eyes:
		cv2.rectangle(frame,(x,y), (x+w,y+h) ,(0,255,0), 2)

	# Display the modified frame
	cv2.imshow('Recording' , frame)
		
	key_pressed = cv2.waitKey(1) 
	if key_pressed == ord('q') or key_pressed == ord('Q') : 
		break


camera.release()
cv2.destroyAllWindows()
