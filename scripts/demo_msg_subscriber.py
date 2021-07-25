#! /bin/python3

import rospy
from mastering_ros_demo_pkg.msg import demo_msg # Auto gen from demo.msg 

def callback(msg):
    rospy.loginfo('Recieved greeting [%s]' % msg.greeting)
    rospy.loginfo('Recieved [%s]' % msg.number)

def demo_msg_subscriber():
    # Initializing ROS node with a name of demo_msg_subscriber
    rospy.init_node('demo_msg_subscriber', anonymous=True)
    # Create a publisher object
    rospy.Subscriber('numbers_msg', demo_msg, callback)
    rospy.spin()

if __name__ == '__main__':
    try:
        demo_msg_subscriber()
    except rospy.ROSInterruptException:
        pass