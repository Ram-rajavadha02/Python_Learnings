#!/usr/bin/env python3
import cv2
import time

def capture_images(time_interval, num_images):
    camera = cv2.VideoCapture(0)  # 0 represents the default camera device
    
    if not camera.isOpened():
        print("Failed to open camera")
        return
    
    for i in range(num_images):
        # Read a frame from the camera
        ret, frame = camera.read()
        
        if not ret:
            print("Failed to capture frame")
            break
        
        # Save the captured image
        cv2.imwrite(f"captured_image_{i}.jpg", frame)
        print(f"Image {i+1} captured and saved as captured_image_{i}.jpg")
        
        # Delay for the specified time interval (in seconds)
        time.sleep(time_interval)
    
    # Release the camera device
    camera.release()

# Set the time interval between captures (in seconds)
time_interval = 5

# Set the number of images to capture
num_images = 3

# Call the capture_images function
capture_images(time_interval, num_images)
    