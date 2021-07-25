#include "ros/ros.h" /* roscpp Core header  */
#include "std_msgs/Int32.h" /* Header of Int32 standard message */

int main(int argc, char **argv)
{
    /* Initializing ROS node with a name of demo_topic_publisher */
    ros::init(argc, argv,"demo_topic_publisher");
    /* Created a node handle object */
    ros::NodeHandle nh;
    /* Created a publisher object */
    ros::Publisher number_publisher = nh.advertise<std_msgs::Int32>("/numbers",10);
    /* Created a rate object */
    ros::Rate loop_rate(10);
    int number_count = 0;

    /* While loop for incrementing number and publishing to topic /numbers */
    while (ros::ok())
    {
        /* Created a Int32 message and insert data to message */
        std_msgs::Int32 msg;
        msg.data = number_count;
        ROS_INFO("%d",msg.data);

        /* Publishing the topic  */
        number_publisher.publish(msg);

        /* Spinning once for doing the  all operation once */
        ros::spinOnce();

        /* Sleeping for sometime */
        loop_rate.sleep();

        /* Incrementing the count */
        ++number_count;
    }
    
    return 0;
}

