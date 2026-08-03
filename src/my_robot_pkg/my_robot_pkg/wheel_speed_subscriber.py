import rclpy
from rclpy.node import Node
from std_msgs.msg import Float64


class WheelSpeedSubscriber(Node):

    def __init__(self):
        super().__init__('wheel_speed_subscriber')

        self.subscription = self.create_subscription(
            Float64,
            'wheel_speed',
            self.listener_callback,
            10
        )

    def listener_callback(self, message):
        self.get_logger().info(
            f'Received wheel speed: {message.data:.2f} rad/s'
        )


def main(args=None):
    rclpy.init(args=args)

    node = WheelSpeedSubscriber()
    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()