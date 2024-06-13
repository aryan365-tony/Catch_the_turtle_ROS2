#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
from turtlesim.srv import Spawn,TeleportAbsolute
from functools import partial
import random
import math

class Control(Node):
    def __init__(self):
        super().__init__("control")
        self.get_logger().info("STARTING TURTLE CONTROL...")
        self.isTurtle=False
        self.pub=self.create_publisher(Twist,"/turtle1/cmd_vel",10)
        self.sub=self.create_subscription(Pose, "/turtle1/pose", self.feedback, 10)

    def feedback(self, msg: Pose):
        if not self.isTurtle:
            self.x1=random.uniform(0.0,11.1)
            self.y1=random.uniform(0.0,11.1)
            self.spawnTurtle(self.x1,self.y1)
        self.get_logger().info("("+str(msg.x)+","+str(msg.y)+")")
        dist=(((msg.x-self.x1)**2)+((msg.y-self.y1)**2))**0.5
        pLinear=2
        pAngular=5
        msg2=Twist()
        if dist>0.5:
            msg2.linear.x=pLinear*dist
            ang=math.atan2((self.y1-msg.y), (self.x1-msg.x))
            diff=ang-msg.theta
            if diff>(22/7):
                diff-=44/7
            elif diff<(-22/7):
                diff+=44/7
            msg2.angular.z=pAngular*diff

        if dist<=0.5:
            self.x1=random.uniform(0.0,11.1)
            self.y1=random.uniform(0.0,11.1)
            self.teleport(self.x1,self.y1)
        self.pub.publish(msg2)
        
    def teleport(self,x,y):
        client=self.create_client(TeleportAbsolute,"/t2/teleport_absolute")
        while not client.wait_for_service(1.0):
            self.get_logger().warn("Waiting for Service")
        req=TeleportAbsolute.Request()
        req.x,req.y,req.theta=x,y,0.0
        callback=client.call_async(req)
        callback.add_done_callback(partial(self.spFeedback))


    def spawnTurtle(self, x, y):
        client=self.create_client(Spawn,"/spawn")
        while not client.wait_for_service(1.0):
            self.get_logger().warn("Waiting for Service")
        req=Spawn.Request()
        req.x,req.y,req.theta=x,y,0.0
        req.name="t2"

        callback=client.call_async(req)
        callback.add_done_callback(partial(self.spFeedback))

    def spFeedback(self,callback):
        try:
            result = callback.result()
            self.isTurtle=True
        except Exception as e:
            self.get_logger().error("Failed to Spawn/Move")

        

def main(args=None):
    rclpy.init(args=args)
    node=Control()
    rclpy.spin(node)
    rclpy.shutdown()


if __name__=="__main":
    main()