#! /usr/bin/env python

import rospy

from sensor_msgs.msg import Image
from cv_bridge import CvBridge

import cv2

def pub_webcam_img():
    pub = rospy.Publisher('vid_frame', Image, queue_size=10)
    rospy.init_node('video_publisher', anonymous=True)
    rate = rospy.Rate(10)
    cap = cv2.VideoCapture(0)
    br = CvBridge()

    while not rospy.is_shutdown():
        ret, frame = cap.read()
        if ret == True:
            rospy.loginfo('publishing video frame')
            pub.publish(br.cv2_to_imgmsg(frame))
        rate.sleep()

if __name__ == '__main__':
    try:
        pub_webcam_img()
    except rospy.ROSInterruptException:
        pass


