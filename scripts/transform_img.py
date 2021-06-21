#! /usr/bin/env python

import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2

def callback(data):
    br = CvBridge()
    rospy.loginfo('receiving video frames')
    current_frame = br.imgmsg_to_cv2(data)
    flipped = cv2.flip(current_frame, -1)
    cv2.imshow('camera', flipped)
    cv2.waitKey(1)

def receive_message():
    rospy.init_node('video_subscriber', anonymous=True)
    rospy.Subscriber('vid_frame', Image, callback)
    rospy.spin()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    receive_message()