# Subscribe to PyShine Youtube channel for the upcoming educational videos
# PyShine presents Matplotlib integration with Open CV to output the frame rate
# Lets write the face detection code
# This code has two parts: 1) Face.py 2) Plot.py
# Face.py will open Webcam and detect face in video stream
# Also it will generate a csv file which will have the current frame rate
# Plot.py will read the csv file and update the plot of frame rate
# The Face.py will run the Plot.py in a thread
# So lets start the code, by importing the required libraries
import cv2
import time
import imutils
import _thread
import numpy as np
import os
import random

# Put the .xml file in the current folder together with Face.py and Plot.py
# faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
# # Initiate the Webcam device with default id of 0
# video_capture = cv2.VideoCapture(0)
# Generate the 'file.csv' with labels time, FPS: Frame Per Second
# print('time,FPS',  file=open('file.csv', 'w'))
# This function will run camera 
def camRun(frame,faceCascade):
# def camRun():
	# A counter to count the frames
	cnt=0
	# Number of frames to count after which the frame rate is obtained
	frames_to_count = 20
	# So we will count 20 frames and also note the time duration for these 20 frames 
	# And then simply divide frames by the duration in seconds to get frame rate
	st=0 # Start time st  = 0 seconds
	i=0 # This is a counter for the time samples for each FPS value
	# while True:
	# 	ret, frame = video_capture.read() # Get the frame 
	# Resize it to 320 width , its optional
	frame = imutils.resize(frame, width=320)
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # RGB to Gray Matrix
	faces = faceCascade.detectMultiScale(
            gray,
            scaleFactor=1.15,
            minNeighbors=7,
            minSize=(80, 80),
            flags=cv2.CASCADE_SCALE_IMAGE
        )
	for (x, y, w, h) in faces:
		cv2.rectangle(frame, (x, y), (x + w, y + h), (214, 169, 33),
               4)  # Here we put rectangle on a frame
	return random.choice(quotes)
	# return len(faces)
	# print(frame)
	# return frame
		# cv2.imshow('FaceDetection', frame) # Display the frame in a window named FaceDetection
		# k = cv2.waitKey(1) 
		# if k == 27: # If click on video frame and press Esc, it will quit
		# 	break
		# Frame rate calculation
		# if cnt == frames_to_count:
		# 	try: # To avoid divide by 0 we put it in try except
		# 		print(frames_to_count/(time.time()-st),'FPS') 
		# 		fps = frames_to_count/(time.time()-st) 
		# 		print(str(i)+',' +str(fps),  file=open('file.csv','a')) 
		# 		st = time.time()
		# 		cnt=0
		# 	except:
		# 		pass
		# Counters are incremented here
		# cnt+=1
		# i+=1
# Lets call the Plot.py in a function plot


quotes =["Quando inizia il film?","Mi scusi","Dov'è la fermata dell'autobus 132?","Ho fame","Ho sete","Dov'è l'ospedale?",
"Piove oggi?","Grazie","Che ore sono?"]
# Start the thread for the plot function
# _thread.start_new_thread(plot,())
# Now run the camRun() function to generate the file.csv 
# camRun()
# # Relase the capture and windows
# video_capture.release()
# cv2.destroyAllWindows() 
# Please comment to provide feedback, if you have questions please ask, and
# Share and like , do subscribe to PyShine Youtube Channel.
