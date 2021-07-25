/*
* This code will subscriber integer values from demo_topic_publisher
*/

#include <sstream>
#include <ros/ros.h>
#include "mastering_ros_demo_pkg/demo_msg.h" /* Auto gen from demo.msg */

void number_callback(const mastering_ros_demo_pkg::demo_msg::ConstPtr& msg)
{
    ROS_INFO("Recieved  greeting [%s]",msg->greeting.c_str());
    ROS_INFO("Recieved  [%d]",msg->number);
}

int main(int argc, char **argv)
{
    /* Initializing ROS node with a name of demo_topic_subscriber */
    ros::init(argc, argv,"demo_msg_subscriber");
    /* Created a nodehandle object */
    ros::NodeHandle nh;
    /* Create a publisher object */
    ros::Subscriber number_subscriber = nh.subscribe("/demo_msg_topic",10,number_callback);

    ros::spin();
    return 0;
}
