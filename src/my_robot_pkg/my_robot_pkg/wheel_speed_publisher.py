import rclpy
from rclpy.node import Node
from std_msgs.msg import Float64


class WheelSpeedPublisher(Node):

    def __init__(self):
        super().__init__('wheel_speed_publisher')

        self.publisher_ = self.create_publisher(
            Float64,
            'wheel_speed',
            10
        )

        self.timer = self.create_timer(
            1.0,
            self.publish_wheel_speed
        )

        self.wheel_speed = 0.0

    def publish_wheel_speed(self):
        message = Float64()

        self.wheel_speed += 0.5
        message.data = self.wheel_speed

        self.publisher_.publish(message)

        self.get_logger().info(
            f'Publishing wheel speed: {message.data:.2f} rad/s'
        )


def main(args=None):
    rclpy.init(args=args)

    node = WheelSpeedPublisher()
    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()