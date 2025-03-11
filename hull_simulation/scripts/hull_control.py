import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from teleop_twist_keyboard import get_key

class HullController(Node):

    def __init__(self):
        super().__init__('hull_controller')
        self.publisher = self.create_publisher(Twist, 'cmd_vel', 10)
        self.get_logger().info("Hull controller ready")

    def control_hull(self):
        while True:
            key = get_key()
            twist = Twist()
            if key == 'w':
                twist.linear.x = 1.0  # Move forward
            elif key == 's':
                twist.linear.x = -1.0  # Move backward
            elif key == 'a':
                twist.angular.z = 1.0  # Turn left
            elif key == 'd':
                twist.angular.z = -1.0  # Turn right
            else:
                twist.linear.x = 0.0  # Stop
                twist.angular.z = 0.0

            self.publisher.publish(twist)

def main(args=None):
    rclpy.init(args=args)
    controller = HullController()
    controller.control_hull()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
