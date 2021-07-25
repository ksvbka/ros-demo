/* 
* This code is the ROS service server code which will receive the integer from service client
*/

#include <ros/ros.h>
#include <sstream>
#include "mastering_ros_demo_pkg/demo_srv.h" /* Auto gen from demo_srv.srv */

int main(int argc, char **argv)
{
    ros::init(argc, argv, "demo_service_client");
    ros::NodeHandle n;
    ros::Rate loop_rate(10);

    ros::ServiceClient client = n.serviceClient<mastering_ros_demo_pkg::demo_srv>("demo_service");
    while (ros::ok())
    {
        mastering_ros_demo_pkg::demo_srv srv;
        std::stringstream ss;
        ss << "Sending from Here";
        srv.request.in = ss.str();

        if (client.call(srv))
        {
            ROS_INFO("From Client  [%s], Server says [%s]", srv.request.in.c_str(), srv.response.out.c_str());
        }
        else
        {
            ROS_ERROR("Failed to call service");
            return 1;
        }

        ros::spinOnce();
        loop_rate.sleep();
    }

    return 0;
}
