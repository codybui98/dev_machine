#!/usr/bin/env python3

from dataclasses import dataclass
import math
import time
import rclpy
from rclpy.node import Node
from rclpy.exceptions import ParameterNotDeclaredException
from rcl_interfaces.msg import ParameterType

from tf2_ros import TransformBroadcaster

from std_msgs.msg import String
from geometry_msgs.msg import Twist, Quaternion, TransformStamped
from nav_msgs.msg import Odometry

class OdomNode(Node):
    """Simple node for echoing an incoming message"""
    def __init__(self):
        super().__init__('odom_dev_node')
        self.subscription = self.create_subscription(
            Odometry,
            'odom',
            self.string_callback,
            10
        )
        self.subscription

    
    def string_callback(self, string: Odometry):
        # msg = String()
        self.get_logger().info(f'Received: {string.pose.pose.position.x, string.pose.pose.position.y, string.pose.pose.position.z}')
        # msg.data = f'echo: {string.data}'
    

def main(args=None):
    rclpy.init(args=args)
    odom_node = OdomNode()
    rclpy.spin(odom_node)

    odom_node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()