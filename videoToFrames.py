# Importing all necessary libraries 
import cv2 
import os 

class Frame(object):

# Read the video from specified path 
   cam = cv2.VideoCapture("/home/jarvis/Desktop/testYellow.mp4") 

   try: 
	
	# creating a folder named redflower 
	 if not os.path.exists('/home/jarvis/Desktop/yellowFlower'): 
		os.makedirs('/home/jarvis/Desktop/yellowFlower') 

# if not created then raise error 
    except OSError: 
	  print ('Error: Creating directory of yellowFlower') 

# frame 
   currentframe = 0

  while(True): 
	
	# reading from frame 
	ret,frame = cam.read() 

	if ret: 
		# if video is still left continue creating images 
		name = '/home/jarvis/Desktop/yellowFlower/frame' + str(currentframe) + '.jpg'
		print ('Creating...' + name) 

		# writing the extracted images 
		cv2.imwrite(name, frame) 

		# increasing counter so that it will 
		# show how many frames are created 
		currentframe += 1
	else: 
		break

# Release all space and windows once done 
   cam.release() 
   cv2.destroyAllWindows() 
