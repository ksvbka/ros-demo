#! /bin/python3

import rospy
from std_msgs.msg import Int32

def demo_topic_publisher():
    # Initializing ROS node with a name of demo_topic_publisher
    rospy.init_node('demo_topic_publisher', anonymous=True)
    # Created a publisher object
    pub = rospy.Publisher('numbers', Int32, queue_size=10)
    # Created a rate object
    rate = rospy.Rate(10)
    count = 0

    while not rospy.is_shutdown():
        rospy.loginfo(count)
        pub.publish(count)
        rate.sleep()
        count = count + 1

if __name__ == '__main__':
    try:
        demo_topic_publisher()
    except rospy.ROSInterruptException:
        pass
