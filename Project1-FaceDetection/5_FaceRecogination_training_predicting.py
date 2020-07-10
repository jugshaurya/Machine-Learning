'''
    We already have collected Data in 4_FaceRecogination_datacollection.py
    Aim: - 
    0. Read a video stream using opencv
    1. load the training data(we collected in 4th file(data collection)).
            X - being the images
            Y - being the label or human name or file name
    3. Train our Algorithm(KNN) over the training data .
    4. Predict over the testing face now and display who the human is ?  

'''
import cv2
import numpy as np
import os # to work with disk files/directoriess

'''
==========================================
            KNN CODE
==========================================
'''
def distance(v1,v2):
    return np.sqrt(np.sum((v1-v2)**2))

def KNN(X,Y,queryPoint,k=10):
    
    distance_li = []
    for i in range(X.shape[0]): 
        d = distance(X[i],queryPoint) 
        distance_li.append((d,Y[i]))

    sorted_li = sorted(distance_li) 
    sorted_li = np.array(sorted_li[:k]) # getting k-nearest points label
    labels = sorted_li[:, 1]
    
    values, count = np.unique(labels, return_counts=True) # returns array of values with its count.
    max_index = np.argmax(count)
    return int(values[max_index])

'''
==========================================
        X and Y Data-Preparation
==========================================
'''

def data_prep():
    X = []
    Y = [] 
    class_id = 0 # to give numerical indexing to person 
    mapping = []

    data_path = './Captured_face_data_for_training/' # ./ is for curent folder
    for file in os.listdir(data_path):
        if file.endswith('.npy'):
            # Adding X(data)

            data = np.load(data_path + file) # data is of size n * 10000 
            X.append(data)
            # Adding Y(target)
            samples = data.shape[0]
            target = class_id * np.ones(samples)
            Y.append(target)
            mapping.append(file[:-4]) # appending name of person with class_id
            class_id += 1

    X = np.concatenate(X)
    Y = np.concatenate(Y)

    return X,Y,mapping

'''
==============================================
    Inputting Face and Querying or Predicting
==============================================
'''

camera = cv2.VideoCapture(0)
face_detector = cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')

# Step 0
while True:

    sucess,frame = camera.read()
    if not sucess:
        continue

    cords = face_detector.detectMultiScale(frame,1.3,6) 

    for x,y,w,h in cords:

        cv2.rectangle(frame, (x,y), (x+w,y+h), (255,0,255), 3)
        padding = 10
        face_section = frame[y-padding:y+h+padding, x-padding:x+padding+w]
        face_section = cv2.resize(face_section, (100,100))

        # Prepare data - Step 1
        X,Y,mapping = data_prep()
        
        # train over KNN - Step 2
        queryFace = np.array(face_section.flatten())
        prediction = KNN(X,Y,queryFace)
        
        # put text over frame - Step 3
        human_pred = mapping[prediction]
        cv2.putText(frame, human_pred, (x-padding,y-padding), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,0,0), 2, cv2.LINE_AA)


    cv2.imshow('Prediction ', frame)
    key_pressed = cv2.waitKey(1)
    if key_pressed==ord('q') or key_pressed==ord('Q'):
        break

camera.release()
cv2.destroyAllWindows()