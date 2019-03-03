'''
Face detection is different from Face recognition. 
Face detection detects merely the presence of faces in an image 
while facial recognition involves identifying whose face it is.
'''

'''
Steps for Face Recoginization _training example
1. start the camera , capture frame and detect face , then store it in a file(numpy file .npy) with a label being of (human name).
2. train over various images of many human beings (in the disk) and store all of them
'''

import cv2
import numpy as np

#camera start
camera = cv2.VideoCapture(0)

face_detector = cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')

nth_frame = 1 # which frame we are curerntly looking at
face_data = [] # storing face_data
store_path = './captured_face_data/' # ./ is for curent folder
human = input('Enter the name of the person  : ')
while True:

	# read or capture frame
	success, frame = camera.read()
	if not success:
		continue

	# detect face - one person in frame at a time 
	face_cord = face_detector.detectMultiScale(frame,1.3,6) 
	for x,y,w,h  in face_cord:
		cv2.rectangle(frame, (x,y), (x+w,y+h), (255,0,255), 3)

		gray_frame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY) # so that data stored is less in size as color images have more bits/pixels
		
		# capture face by cropping frame for face with some padding in frame as well
		padding = 10
		face_section = gray_frame[y-padding:y+h+padding, x-padding:x+padding+w]	# cropping the gray_frame
		face_section = cv2.resize(face_section, (100,100))	# storing the section as 100 X 100 images so that wvery image is of same pixels so to be operated by numpy
		
		if nth_frame % 10 == 0:
			face_data.append(face_section) # adding 10th frame
			print(f'Stored {len(face_data)} Image')	
			cv2.imshow('Captured Gray Section', face_section)  # showing what are we storing exactly	

	nth_frame += 1
	cv2.imshow('Recording' , frame)

	key_pressed  = cv2.waitKey(1)
	if key_pressed == ord('q') or key_pressed == ord('Q'):
		break


# for reshaping and saving
face_data = np.array(face_data)
face_data = face_data.reshape((face_data.shape[0], -1)) # storing into 100*100 columns per image.
np.save(store_path+human+'.npy',face_data)
print('Data Saved Succesfully as ' + human + '.npy')

# Switching off Stuffs
camera.release()
cv2.destroyAllWindows()