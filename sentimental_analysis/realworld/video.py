import os
basepath = os.path.dirname(__file__)
from tensorflow.keras.models import model_from_json
import numpy as np
import cv2
import math
import tensorflow as tf
from tensorflow.keras.preprocessing import image
facec = cv2.CascadeClassifier(os.path.join(basepath, 'haarcascade_frontalface_default.xml'))
from matplotlib import pyplot as plt

import shutil
from skimage.metrics import structural_similarity

with open(os.path.join(basepath, "model.json"), "r") as json_file:   #Loading the saved model
    loaded_model_json = json_file.read()
    loaded_model = model_from_json(loaded_model_json)

loaded_model.load_weights(os.path.join(basepath, "model_weights.h5"))
label_to_text = {0:'angry', 1:'disgust', 2:'fear', 3:'happy', 4: 'sad'}

def pred(img_path):  
    label_to_text = {0:'angry', 1:'disgust', 2:'fear', 3:'happy', 4: 'sad'}  
    img=cv2.imread(img_path)									#read Image
    # print(img)
    gray_fr = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)				#covert image to grayscale
    faces_rects = facec.detectMultiScale(gray_fr, scaleFactor = 1.2, minNeighbors = 5)  #opencv's cascade classifier will be used for detecting the face
    if len(faces_rects)!=0:
        for (x, y, w, h) in faces_rects:
            fc = gray_fr[y:y+h, x:x+w]     #extracting only the face part
        roi = cv2.resize(fc, (48, 48))	#resizing it according to the image that are acceptable by our model
        img = image.img_to_array(roi)
        img = img/255
        img = np.expand_dims(img, axis=0)
        return label_to_text[np.argmax(loaded_model.predict(img))],img  #model.predict is used for predicting the emotion
    else:
        return 0,0  #return 0 if the face is not found

def removeout():
    shutil.rmtree(os.path.join(basepath, 'output'))  #remove output folder

def vidframe(vidname):
	if vidname==0:
		cap = cv2.VideoCapture(0)
		# Define the codec and create VideoWriter object
		fourcc = cv2.VideoWriter_fourcc(*'XVID')
		out = cv2.VideoWriter(os.path.join(basepath, 'output.mp4'),fourcc, 20.0, (640,480))

		while(cap.isOpened()):
			ret, frame = cap.read()
		# 	if ret==True:
		# 		out.write(frame)
		# 		cv2.imshow('frame',frame)
		# 		if cv2.waitKey(1) & 0xFF == ord('q'):
		# 			break
		# 	else:
		# 		break

		# # Release everything if job is finished
		cap.release()
		# out.release()
		cv2.destroyAllWindows()
		vidname=os.path.join(basepath, "output.mp4")

	if os.path.exists(os.path.join(basepath, 'output')):      #if output folder is present then delete it
		removeout()						#create Output folder for storing frame
	os.mkdir(os.path.join(basepath, 'output'))
	cap = cv2.VideoCapture(vidname)			#capture  video
	frameRate=cap.get(5)					
	count = 0
	while(cap.isOpened()):					#store the frames in output folder
		frameId = cap.get(1)
		ret, frame = cap.read()
		if (ret != True):
			break
		if (frameId % math.floor(frameRate) == 0):
			filename ="output/frame%d.jpg" % count;count+=1
			filename_1 = os.path.join(basepath, filename)
			cv2.imwrite(filename_1, frame)
	cap.release()
	result=[]							# used for storing emotion
	face=[]								#used for storing face images
	for filename in os.listdir(os.path.join(basepath, "output")): #loop through each frame
		a,b = pred(f"{basepath}/output/"+filename)  #run pred function to get emotion and face images
		result.append(a)
		face.append(b)
	removeout()
	result=[x for x in result if x!=0]        #removing null prediction
	face=[x for x in face if len(str(x))>1]
	return result, face

def ssimscore1(im1,im2):
    im1=im1.reshape(48, 48, 1).astype('float32')   #reshaping the flattened image array
    im2=im2.reshape(48, 48, 1).astype('float32')
    (score, diff) = structural_similarity(im1, im2, full=True,multichannel=True) #comparing the image for finding difference using compare_ssim function 
    return score
    





