#!/usr/bin/env python3
import cv2

def open_camera():
    camera = cv2.VideoCapture(0)  # 0 represents the default camera device
    
    if not camera.isOpened():
        print("Failed to open camera")
        return
    
    while True:
        # Read a frame from the camera
        ret, frame = camera.read()
        
        if not ret:
            print("Failed to capture frame")
            break
        
        # Flip the frame vertically (inverted image)
        frame = cv2.flip(frame, 180)
        
        # Display the inverted frame
        cv2.imshow("Camera", frame)
        
        # Exit the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    # Release the camera device and close the window
    camera.release()
    cv2.destroyAllWindows()

# Call the open_camera function
open_camera()
