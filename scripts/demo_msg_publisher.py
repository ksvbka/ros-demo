#! /bin/python3

import rospy
from mastering_ros_demo_pkg.msg import demo_msg # Auto gen from demo.msg 

def demo_msg_publisher():
    # Initializing ROS node with a name of demo_msg_publisher
    rospy.init_node('demo_msg_publisher', anonymous=True)
    # Created a publisher object
    pub = rospy.Publisher('numbers_msg', demo_msg, queue_size=10)
    # Created a rate object
    rate = rospy.Rate(10)
    count = 0

    while not rospy.is_shutdown():
        msg = demo_msg()
        msg.greeting = "hello world "
        msg.number = count
        rospy.loginfo(msg)
    
        pub.publish(msg)
        rate.sleep()
        count = count + 1

if __name__ == '__main__':
    try:
        demo_msg_publisher()
    except rospy.ROSInterruptException:
        pass