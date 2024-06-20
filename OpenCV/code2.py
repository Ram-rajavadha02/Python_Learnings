import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2

def image_callback(msg):
    bridge = CvBridge()

    # Convert the ROS Image message to an OpenCV image
    try:
        cv_image = bridge.imgmsg_to_cv2(msg, desired_encoding="bgr8")
    except CvBridgeError as e:
        print(e)
        return

    # Display the image
    cv2.imshow("Received Image", cv_image)
    cv2.waitKey(1)

def main():
    rospy.init_node('webcam_subscriber', anonymous=True)

    # Create a subscriber to the "image_topic" topic
    rospy.Subscriber("image_topic", Image, image_callback)

    rospy.spin()

if __name__ == '__main__':
    main()

