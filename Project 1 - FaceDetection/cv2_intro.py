import cv2	

# Loading Images
mario_img = cv2.imread('Mario.jpg')
micky_img = cv2.imread('mickey.jpeg')
mario_gray_img = cv2.imread('Mario.jpg',cv2.IMREAD_GRAYSCALE)
micky_gray_img = cv2.imread('mickey.jpeg',cv2.IMREAD_GRAYSCALE)


# Showing Images
cv2.imshow('My Mario Image' , mario_img)
cv2.imshow('My Mickey Image' , micky_img)
# Showing Grayscaled - Images
cv2.imshow('My Gray Mario Image' , mario_gray_img)
cv2.imshow('My Gray Mickey Image' , micky_gray_img)


'''
	Necessery lines to be there to hold on the loaded frames
'''
# waiting for user input
cv2.waitKey(0) # wait for the user keyboard infinitely , when any key is pressed , it close all the opened Windows.
