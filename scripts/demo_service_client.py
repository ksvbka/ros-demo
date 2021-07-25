#! /bin/python3
import rospy
from mastering_ros_demo_pkg.srv import demo_srv, demo_srvRequest

def demo_service_client():
    rospy.init_node('demo_service_client')
    rospy.wait_for_service('demo_service')

    try:
        demo_service = rospy.ServiceProxy('demo_service', demo_srv)
        # simplified style
        res1 = demo_service('Sending from Here - simplified style')
        # formal style
        res2 = demo_service.call(demo_srvRequest('Sending from Here - formal style'))

        rospy.loginfo('Server says [%s]' % res1)
        rospy.loginfo('Server says [%s]' % res2)
    except rospy.ServiceException as e:
        rospy.loginfo('Service call failed: %s' % e)

if __name__ == '__main__':
    try:
        demo_service_client()
    except rospy.ROSInterruptException:
        pass
