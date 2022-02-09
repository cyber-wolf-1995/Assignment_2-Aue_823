#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import Twist


def turtlesim_square_open_loop(): 

    # Starts a new Node
    rospy.init_node('turtlesim_node', anonymous=True) 
    velocity_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    vel_msg = Twist() 
    
    # Set required linear and angular speeds
    lin_speed = 0.2 # m/s
    ang_speed = 0.2 # rad/s
    
    # Set required linear distance and rotation angle
    distance = 2
    angle = 89*3.1415/180
    
    # Initialize message
    vel_msg.linear.x = 0
    vel_msg.linear.y = 0
    vel_msg.linear.z = 0
    vel_msg.angular.x = 0
    vel_msg.angular.y = 0
    vel_msg.angular.z = 0
    
    while not rospy.is_shutdown():
    
        for i in range(0,4):
            # Travel along  positive x 
            vel_msg.linear.x = lin_speed
            t0 = rospy.Time.now().to_sec()
            current_distance = 0 
        
            while(current_distance < distance):
                # publish velocity message
                velocity_publisher.publish(vel_msg)
                t1=rospy.Time.now().to_sec()
                current_distance= lin_speed*(t1-t0)
            
            # Set x-velocity = 0 after completing straight line
            vel_msg.linear.x = 0
            # Publish velocity message
            velocity_publisher.publish(vel_msg) 
        
            # Rotate anti-clockwise about z
            vel_msg.angular.z = ang_speed
            t0 = rospy.Time.now().to_sec()
            current_angle = 0 
        
            while(current_angle < angle):
                # publish velocity message
                velocity_publisher.publish(vel_msg)
                t1=rospy.Time.now().to_sec()
                current_angle = ang_speed*(t1-t0) 
            
            # Set angular velocity = 0 after turning 90 degrees
            vel_msg.angular.z = 0
            # Publish velocity message
            velocity_publisher.publish(vel_msg)
            #rospy.spin() 
        

          
        
if __name__ == '__main__':
    try:
        #Testing our function
        turtlesim_square_open_loop()
       
    except rospy.ROSInterruptException: pass
    
# Code Referred From:
# http://wiki.ros.org/turtlesim/Tutorials/Moving%20in%20a%20Straight%20Line
# http://wiki.ros.org/turtlesim/Tutorials/Rotating%20Left%20and%20Right
