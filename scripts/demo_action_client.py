#! /bin/python3

import rospy
import actionlib
import sys
from mastering_ros_demo_pkg.msg import Demo_actionAction, Demo_actionGoal

def DemoActionClient():
    client = actionlib.SimpleActionClient('demo_action', Demo_actionAction)
    client.wait_for_server()

    rospy.loginfo('Action server started, sending goal.')
    # Creates a goal and send to the action server.
    goal = Demo_actionGoal(count=20)
    client.send_goal(goal)

    # Waits for the server to finish performing the action.
    client.wait_for_result()

    # Prints out the result of executing the action
    return client.get_result()

if __name__ == '__main__':
    try:
        rospy.init_node('DemoActionClient_py')
        result = DemoActionClient()
        print("Result:", result.final_count)
    except rospy.ROSInterruptException:
        print("program interrupted before completion", file=sys.stderr)
