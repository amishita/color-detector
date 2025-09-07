import cv2
import numpy as np

# Create a window
cv2.namedWindow("Color Detector")
cv2.resizeWindow("Color Detector", 640, 240)

# Start video capture
cap = cv2.VideoCapture(0) # Use 0 for default camera

ranges = {
    "red1":   ([0, 120, 70],   [10, 255, 255]),
    "red2":   ([170, 120, 70], [180, 255, 255]),   # red wraparound
    "green":  ([36, 100, 100], [86, 255, 255]),
    "blue":   ([94, 80, 2],    [126, 255, 255]),
}


while True:
    # Read a frame from the camera
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1) # Flip the frame horizontally

    if not ret: # If frame not read correctly, break the loop
        break

    # Convert the frame to HSV color space
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    for color, (lower, upper) in ranges.items():
        lower = np.array(lower)
        upper = np.array(upper)

        # Create a mask for the color
        mask = cv2.inRange(hsv, lower, upper)

        # find contours in the mask
        contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        for cnt in contours:
            area = cv2.contourArea(cnt)
            if area > 500:  # filter out noise
                x, y, w, h = cv2.boundingRect(cnt)

                # Choose box color based on label
                if "red" in color: box_color = (0, 0, 255)
                elif color == "green": box_color = (0, 255, 0)
                elif color == "blue": box_color = (255, 0, 0)

                # Draw rectangle + label
                cv2.rectangle(frame, (x, y), (x+w, y+h), box_color, 2)
                cv2.putText(frame, color, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, box_color, 2)

    # show frame in a window
    cv2.imshow("Color Detector", frame)

    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'): 
        break

# release the camera and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()

