import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2

def process_image(ros_image):
    # Convert the ROS image message to an OpenCV image
    bridge = CvBridge()
    cv_image = bridge.imgmsg_to_cv2(ros_image, desired_encoding="bgr8")

    # Process the image (e.g., apply image processing operations)
    # ...

    # Display the processed image
    cv2.imshow("Processed Image", cv_image)
    cv2.waitKey(1)

def image_subscriber():
    # Initialize ROS node
    rospy.init_node('image_subscriber_node', anonymous=True)

    # Create a subscriber for the image topic
    rospy.Subscriber('captured_image_topic', Image, process_image)

    # Spin to keep the node running
    rospy.spin()

# Call the image_subscriber function
image_subscriber()

