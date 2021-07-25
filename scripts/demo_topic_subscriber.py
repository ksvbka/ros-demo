#! /bin/python3

import rospy
from std_msgs.msg import Int32

def callback(msg):
    rospy.loginfo('Recieved [%s]' % msg.data)

def demo_topic_subscriber():
    rospy.init_node('demo_topic_subscriber', anonymous=True)
    rospy.Subscriber('numbers', Int32, callback)

    # Spinning the node
    rospy.spin()

if __name__ == '__main__':
    try:
        demo_topic_subscriber()
    except rospy.ROSInterruptException:
        pass