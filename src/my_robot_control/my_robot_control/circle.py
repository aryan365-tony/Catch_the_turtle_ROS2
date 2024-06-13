#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

class Circle(Node):
    def __init__(self):
        super().__init__("Circle")
        self.get_logger().info("Hello From MARK 1")
        self.pub=self.create_publisher(Twist,"/turtle1/cmd_vel",10)
        self.time=self.create_timer(0.3,self.circle)
    def circle(self):
        data=Twist()
        data.linear.x=-2.0
        data.angular.z=1.0
        self.pub.publish(data)


def main(args=None):
    rclpy.init(args=args)
    node=Circle()
    rclpy.spin(node=node)
    rclpy.shutdown()

if __name__=='__main__':
    main()