#!/usr/bin/env python3
import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2
import time

def capture_and_publish_images(time_interval, num_images):
    # Initialize ROS node
    rospy.init_node('image_publisher_node', anonymous=True)
    
    # Create a publisher for the image topic
    image_pub = rospy.Publisher('captured_image_topic', Image, queue_size=10)
    
    # Create a CvBridge object
    bridge = CvBridge()
    
    camera = cv2.VideoCapture(0)  # 0 represents the default camera device
    
    if not camera.isOpened():
        rospy.logerr("Failed to open camera")
        return
    
    for i in range(num_images):
        # Read a frame from the camera
        ret, frame = camera.read()
        
        if not ret:
            rospy.logerr("Failed to capture frame")
            break
        
        # Convert the OpenCV image to a ROS image message
        ros_image = bridge.cv2_to_imgmsg(frame, encoding="bgr8")
        
        # Publish the ROS image message
        image_pub.publish(ros_image)
        rospy.loginfo("Image captured and published")
        
        # Save the captured image
        cv2.imwrite(f"captured_image_{i}.jpg", frame)
        rospy.loginfo(f"Image {i+1} captured and saved as captured_image_{i}.jpg")
        
        # Delay for the specified time interval (in seconds)
        time.sleep(time_interval)
    
    # Release the camera device
    camera.release()

# Set the time interval between captures (in seconds)
time_interval = 5

# Set the number of images to capture
num_images = 3

# Call the capture_and_publish_images function
capture_and_publish_images(time_interval, num_images)

