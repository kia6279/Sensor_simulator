import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32



class SensorSubscriber(Node):

    def __init__(self):
        super().__init__('sense_subscriber')
        self.subscription = self.create_subscription(Float32,'distance',self.listener_callback,10)
        self.subscription  # prevent unused variable warning

    def listener_callback(self, msg):
        self.get_logger().info('I see: "%s"' % msg.data)


def main(args=None):
    rclpy.init(args=args)

    sense_subscriber = SensorSubscriber()

    rclpy.spin(sense_subscriber)
    
    sense_subscriber.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
