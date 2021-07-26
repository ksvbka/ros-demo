#! /bin/python3

import rospy
import actionlib
from mastering_ros_demo_pkg.msg import Demo_actionAction, Demo_actionFeedback, Demo_actionResult

class DemoActionServer(object):
    def __init__(self, name):
        self._action_name = name
        self._result = Demo_actionResult()
        self._feedback = Demo_actionFeedback()

        self._as = actionlib.SimpleActionServer(self._action_name, Demo_actionAction, execute_cb=self.execute_cb, auto_start = False)
        self._as.start()

    def execute_cb(self, goal):       
        rate = rospy.Rate(5)
        success = True
        rospy.loginfo("%s is processing the goal %s" %(self._action_name, goal.count))

        if not self._as.is_active() or self._as.is_preempt_requested():
            return

        for i in range(1, goal.count):
            if self._as.is_preempt_requested():
                self._as.set_preempted()
                success = False
                break

            self._feedback.current_number = i
            self._as.publish_feedback(self._feedback)
            rate.sleep()
          
        if success:
            self._result.final_count = self._feedback.current_number + 1
            rospy.loginfo('%s: Succeeded' % self._action_name)
            self._as.set_succeeded(self._result)


if __name__ == '__main__':
    rospy.init_node('demo_action')
    server = DemoActionServer(rospy.get_name())
    rospy.spin()
