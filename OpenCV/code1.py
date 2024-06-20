#!/usr/bin/env python3
import cv2
import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge

def main():
    rospy.init_node('webcam_publisher', anonymous=True)
    bridge = CvBridge()

    # Create a publisher to publish the image
    image_pub = rospy.Publisher('image_topic', Image, queue_size=10)

    key = cv2.waitKey(1)
    webcam = cv2.VideoCapture(0)
    while not rospy.is_shutdown():
        try:
            check, frame = webcam.read()
            print(check)  # Prints True as long as the webcam is running
            print(frame)  # Prints matrix values of each frame
            frame = cv2.flip(frame,180)
            # Display the frame in a window called "Capturing"
            cv2.imshow("Capturing", frame)

            key = cv2.waitKey(1)
            if key == ord('s'):
                cv2.imwrite(filename='saved_img.jpg', img=frame)
                webcam.release()

                # Read the saved image and convert it to grayscale
                img_new = cv2.imread('saved_img.jpg', cv2.IMREAD_GRAYSCALE)

                # Display the captured image in a window called "Captured Image"
                cv2.imshow("Captured Image", img_new)
                cv2.waitKey(1650)
                cv2.destroyAllWindows()

                print("Processing image...")
                img_ = cv2.imread('saved_img.jpg', cv2.IMREAD_ANYCOLOR)

                print("Converting RGB image to grayscale...")
                gray = cv2.cvtColor(img_, cv2.COLOR_BGR2GRAY)
                print("Converted RGB image to grayscale...")

                print("Resizing image to 28x28 scale...")
                img_ = cv2.resize(gray, (28, 28))
                print("Resized...")

                img_resized = cv2.imwrite(filename='saved_img-final.jpg', img=img_)
                print("Image saved!")

                # Convert the OpenCV image to a ROS Image message
                ros_image = bridge.cv2_to_imgmsg(img_, encoding="mono8")

                # Publish the ROS Image message
                image_pub.publish(ros_image)

                break
            elif key == ord('q'):
                print("Turning off camera.")
                webcam.release()
                print("Camera off.")
                print("Program ended.")
                cv2.destroyAllWindows()
                break

        except KeyboardInterrupt:
            print("Turning off camera.")
            webcam.release()
            print("Camera off.")
            print("Program ended.")
            cv2.destroyAllWindows()
            break

    rospy.spin()

if __name__ == '__main__':
    main()

