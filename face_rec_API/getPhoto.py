import numpy as np
import cv2
import time

def get_time():
	t=time.gmtime()
	day=str(t.tm_yday)
	hour=str(t.tm_hour)
	minute=str(t.tm_min)
	second=str(t.tm_sec)
	return day+hour+minute+second

def getPhoto():
	cap = cv2.VideoCapture(0)

	while(True):
	    # Capture frame-by-frame
	    ret, frame = cap.read()

	    # Our operations on the frame come here
	    #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

	    # Display the resulting frame
	    cv2.imshow('frame',frame)
	    if cv2.waitKey(1) & 0xFF == ord('c'):
	        ans=frame
	        break

	# When everything done, release the capture
	cap.release()
	cv2.destroyAllWindows()
	save_path='./data/temp/'+get_time()+'.jpg'
	cv2.imwrite(save_path, frame)
	return ans, save_path

def main():
	im,comp_path=getPhoto()


if __name__=='__main__':
	main()