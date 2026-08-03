import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist


class CmdVelPublisher(Node):

    def __init__(self):
        super().__init__('cmd_vel_publisher')

        self.publisher_ = self.create_publisher(
            Twist,
            'cmd_vel',
            10
        )

        self.timer = self.create_timer(
            1.0,
            self.publish_velocity
        )

        self.linear_speed = 0.0
        self.angular_speed = 0.0

    def publish_velocity(self):
        message = Twist()

        self.linear_speed += 0.1
        self.angular_speed = 0.2

        message.linear.x = self.linear_speed
        message.angular.z = self.angular_speed

        self.publisher_.publish(message)

        self.get_logger().info(
            f'Linear: {message.linear.x:.2f} m/s, '
            f'Angular: {message.angular.z:.2f} rad/s'
        )


def main(args=None):
    rclpy.init(args=args)

    node = CmdVelPublisher()
    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()