#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from turtlesim.msg import Pose

class Pose(Node):
    def __init__(self):
        super().__init__("pose")
        self.get_logger().info("POSING....")
        self.poser=self.create_subscription(Pose, "/turtle1/pose", self.poseback, 10)
    
    def poseback(self, msg: Pose):
        self.get_logger().info(str(msg))

def main(args=None):
    rclpy.init(args=args)
    posenode= Pose()
    rclpy.spin(posenode)
    rclpy.shutdown()

if __name__=="__main__":
    main()