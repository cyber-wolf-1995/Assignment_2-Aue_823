#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import Twist
import sys


def turtle_circle(r):
	rospy.init_node('turtlesim', anonymous=True)
	pub = rospy.Publisher('/turtle1/cmd_vel',
						Twist, queue_size=10)
	rate = rospy.Rate(100)
	vel = Twist()
	while not rospy.is_shutdown():
		vel.linear.x = r # Linear Velocity = r X w
		vel.linear.y = 0
		vel.linear.z = 0
		vel.angular.x = 0
		vel.angular.y = 0
		vel.angular.z = 1
		pub.publish(vel)
		rate.sleep()


if __name__ == '__main__':
	try:
		r = float(input("Enter Radius of Circle: "))
		turtle_circle(r)
	except rospy.ROSInterruptException:
		pass

# Code Referred From:
# https://www.geeksforgeeks.org/draw-a-circle-using-turtlesim-in-ros-python/
