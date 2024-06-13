#!/usr/bin/env python3
import rclpy
from rclpy.node import Node

class Node1(Node):
    def __init__(self):
        super().__init__("Node_1")
        self.count=0
        self.get_logger().info("Hello From MARK 1")
        self.create_timer(1.0,self.repeater)
    def repeater(self):
        self.get_logger().info("Working..."+str(self.count))
        self.count+=1

def main(args=None):
    rclpy.init(args=args)
    node=Node1()
    rclpy.spin(node=node)
    rclpy.shutdown()

if __name__=='__main__':
    main()