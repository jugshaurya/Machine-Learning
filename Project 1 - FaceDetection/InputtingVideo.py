import cv2

# 1. Capturing the video usig Webcam which has id of 0 
camera = cv2.VideoCapture(0) # 0 is the id of webCam

# Reading a Video Stream Frame by Frame

while True:

	# 2. grab the image
	successful,image =  camera.read() # retruns the tuple (success,frameORimage)

	# if frame is not captured properly
	if successful is False:
		continue

	# (optional Step) converting img to grayscale img
	grayImg = cv2.cvtColor(image ,cv2.COLOR_BGR2GRAY)
	cv2.imshow('Gray-Recording' , grayImg)

	# 3. Display Captured Frame
	cv2.imshow('Recording' , image)

	# wanna Quit (Press `q`or 'Q')
	key_pressed = cv2.waitKey(1)  # wait of 1 millisecond before continuing loop 
	if key_pressed == ord('q') or key_pressed == ord('Q') : # ord function returns 8 bit integers
		break


# 4.Relesing my Camera
camera.release()
cv2.destroyAllWindows()