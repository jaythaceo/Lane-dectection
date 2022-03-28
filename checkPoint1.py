import cv2 as cv
import numpy as np

cap  = cv.VideoCapture("input.mp4")

while cap.isOpened():
	ret, frame = cap.read()
	if not ret:
		print("Cannot receive frame")
		break

	gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

	cv.imshow('frame', gray)
	if cv.waitKey(1) == ord('q'):
		break

cap.release()
cv.destroyAllWindows()