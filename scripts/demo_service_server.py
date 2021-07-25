#! /bin/python3
import rospy
from mastering_ros_demo_pkg.srv import demo_srv, demo_srvResponse

def demo_service_callback(req):
    res = demo_srvResponse('Received Here')
    rospy.loginfo(req)
    rospy.loginfo(res)
    return res

def demo_service_server():
    rospy.init_node('demo_service_server')
    rospy.Service('demo_service', demo_srv, demo_service_callback)

    rospy.loginfo('Ready to receive from client.')
    rospy.spin()

if __name__ == '__main__':
    try:
        demo_service_server()
    except rospy.ROSInterruptException:
        pass
