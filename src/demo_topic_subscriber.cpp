#include <ros/ros.h>
#include <std_msgs/Int32.h>

/* Callback of the topic /numbers */
void number_callback(const std_msgs::Int32::ConstPtr& msg)
{
    ROS_INFO("Recieved  [%d]",msg->data);
}

int main(int argc, char **argv)
{

    /* Initializing ROS node with a name of demo_topic_subscriber */
    ros::init(argc, argv,"demo_topic_subscriber");
    /* Created a nodehandle object */
    ros::NodeHandle nh;
    /* Create a publisher object */
    ros::Subscriber number_subscriber = nh.subscribe("/numbers", 10, number_callback);
    /* Spinning the node */
    ros::spin();
    
    return 0;
}

