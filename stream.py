import numpy as np 
import cv2

cap = cv2.VideoCapture(0);
v = ''
r = 0
#if(v == 'w'):
while(True):
	ret, frame = cap.read();
	if (cv2.waitKey(1) & 0xFF == ord('w')):
		v = 'w'
	elif (cv2.waitKey(1) & 0xFF == ord('p')):
		print("pause");
		v = '';
	elif (cv2.waitKey(1) & 0xFF == ord('c')):
		print("radio: ")
		r = int(input())
		v = 'c';
	else:
		pass

	if(v == 'w'):
		gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
		cv2.destroyWindow("frame");
		cv2.imshow("b/w", gray)
	if (v == 'c'):
		circle = cv2.circle(frame, (100, 100), 100, (0, 255, 0), 10)
		cv2.destroyWindow("frame");
		cv2.imshow("circle", circle);
	else:
		cv2.imshow("frame", frame);

	if (cv2.waitKey(1) & 0xFF == ord('q')):
		break

cap.release()
cv2.destroyAllWindows()