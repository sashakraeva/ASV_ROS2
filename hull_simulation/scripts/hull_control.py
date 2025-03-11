#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

class HullTeleop(Node):
    def __init__(self):
        super().__init__('hull_teleop')
        self.publisher = self.create_publisher(Twist, 'cmd_vel', 10)
        self.get_logger().info("HullTeleop Node Started!")

def main(args=None):
    rclpy.init(args=args)
    node = HullTeleop()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
