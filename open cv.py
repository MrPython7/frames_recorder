 
# saving an operated video 

 
import numpy as np 
import cv2 

 
cap = cv2.VideoCapture(0) 

 
fourcc = cv2.VideoWriter_fourcc(*'XVID') 
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480)) 

 
while(True): 
	 
	 
	ret, frame = cap.read() 
	hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV) 
	
	out.write(hsv) 
	
    
	cv2.imshow('Original', frame) 

	 
	cv2.imshow('frame', hsv) 

	if cv2.waitKey(1) & 0xFF == ord('a'): 
		break

# Close the window 
cap.release() 
 
out.release() 
 
cv2.destroyAllWindows() 
