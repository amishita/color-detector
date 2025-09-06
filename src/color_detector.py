import cv2
import numpy as np

# Create a window
cv2.namedWindow("Color Detector")
cv2.resizeWindow("Color Detector", 640, 240)

# Start video capture
cap = cv2.VideoCapture(0) # Use 0 for default camera

while True:
    # Read a frame from the camera
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1) # Flip the frame horizontally
    if not ret: # If frame not read correctly, break the loop
        print("Failed to grab frame")
        break

    # show frame in a window
    cv2.imshow("Color Detector", frame)

    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'): 
        break

# release the camera and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()

