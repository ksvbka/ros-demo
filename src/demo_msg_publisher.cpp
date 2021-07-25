/*
* This code will publish a integers from 0 to n with a delay of 100ms
*/

#include <sstream>
#include <ros/ros.h>
#include <std_msgs/Int32.h>
#include "mastering_ros_demo_pkg/demo_msg.h" /* Auto gen from demo_msg.msg */

int main(int argc, char **argv)
{
    /* Initializing ROS node with a name of demo_topic_publisher */
    ros::init(argc, argv,"demo_msg_publisher");
    /* Created a nodehandle object */
    ros::NodeHandle nh;
    /* Create a publisher object */
    ros::Publisher number_publisher = nh.advertise<mastering_ros_demo_pkg::demo_msg>("/demo_msg_topic",10);
    /* Create a rate object */
    ros::Rate loop_rate(10);
    /* Variable of the number initializing as zero */
    int number_count = 0;

    /* While loop for incrementing number and publishing to topic /numbers */
    while (ros::ok())
    {
        /* Created a Int32 message and inserted data to message header */
        mastering_ros_demo_pkg::demo_msg msg; 
        std::stringstream ss;
        ss << "hello world ";
        msg.greeting = ss.str();
        msg.number = number_count;

        ROS_INFO("%d",msg.number);
        ROS_INFO("%s",msg.greeting.c_str());

        /* Publishing the message */
        number_publisher.publish(msg);
        /* Spining once for doing the  all operation once */
        ros::spinOnce();

        loop_rate.sleep();
        ++number_count;  
    }

    return 0;
}
