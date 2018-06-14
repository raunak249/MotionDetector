import cv2 #For using the webcam and getting the frames
from datetime import datetime # To get the time stamp of the image

def diffImg(t0,t1,t2): #This will calculate the difference between the frames and return the new frame 
   d1 = cv2.absdiff(t2,t1)
   d2 = cv2.absdiff(t1,t0)
   return cv2.bitwise_and(d1,d2)

threshold = 150000 # This denotes the sensitivity of the detector. If it is less, the sensitivity will be more
cam = cv2.VideoCapture(0) # WebCam capture
t0 = cv2.cvtColor(cam.read()[1], cv2.COLOR_RGB2GRAY)
t1 = cv2.cvtColor(cam.read()[1], cv2.COLOR_RGB2GRAY)
t2 = cv2.cvtColor(cam.read()[1], cv2.COLOR_RGB2GRAY)
timestamp = datetime.now().strftime('%Ss')
while True:
   if cv2.countNonZero(diffImg(t0,t1,t2)) > threshold and timestamp != datetime.now().strftime('%Ss'):
       dimg = cam.read()[1]
       cv2.imwrite(datetime.now().strftime('%Y%m%d_%Hh%Mm%Ss%f') + '.jpg',dimg) # Writing the image to the directory
       timestamp = datetime.now().strftime('%Ss')
   t0 = t1
   t1 = t2
   t2 = cv2.cvtColor(cam.read()[1], cv2.COLOR_RGB2GRAY)
   cv2.imshow("Detection",diffImg(t0,t1,t2))
   key = cv2.waitKey(10)
   if key == 27:
      cv2.destroyWindow("Detection") # webcam closes with Esc key
      break;

print("GoodBye")
