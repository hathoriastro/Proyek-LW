#!/usr/bin/env python3
import rospy
from std_msgs.msg import String
from geometry_msgs.msg import Twist

def callback(data):
    rospy.loginfo(f"Received: {data.data}")
    pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    twist = Twist()

    #Maju twist.linear.x = 2.0
    #Mundur twist.linear.x = -2.0
    #Kiri twist.angular.z = 2.0
    #Kanan twist.angular.z = -2.0
    pub.publish(twist)

def listener():
    # Menggunakan topik  "/turtle_commands"
    rospy.spin()

if __name__ == '__main__':
    try:
        listener()
    except rospy.ROSInterruptException:
        pass
