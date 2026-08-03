import rclpy
from rclpy.node import Node
from std_msgs.msg import String


class MyPublisher(Node):

    def __init__(self):
        super().__init__('my_publisher')

        self.publisher_ = self.create_publisher(
            String,
            'robot_message',
            10
        )

        self.timer = self.create_timer(
            1.0,
            self.publish_message
        )

        self.counter = 0

    def publish_message(self):
        message = String()
        message.data = f'Hello from my robot: {self.counter}'

        self.publisher_.publish(message)
        self.get_logger().info(f'Publishing: "{message.data}"')

        self.counter += 1


def main(args=None):
    rclpy.init(args=args)

    node = MyPublisher()

    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
