import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32 

class SensorPublisher(Node):
    """
    ROS 2 Node that simulates a distance sensor and publishes data
    at a fixed rate.
    """

    def __init__(self):
        super().__init__('simulated_sensor_publisher')

        self.publisher_ = self.create_publisher(Float32, 'distance', 10)

        self.counter = 0.0

        timer_period = 0.5  
        
        # Create a Timer to call the 'timer_callback' function periodically
        self.timer = self.create_timer(timer_period, self.timer_callback)
        
        self.get_logger().info('Simulated Sensor Publisher Node has started. Publishing at 2 Hz.')

    def timer_callback(self):
        # Create the message object
        msg = Float32()
        msg.data = float(self.counter)
        # Publish the message
        self.publisher_.publish(msg)

        # Log the published data to the console
        self.get_logger().info(f'Publishing distance: {msg.data:.2f} m')
        self.counter += 1


def main(args=None):
    rclpy.init(args=args)
    sensor_publisher = SensorPublisher()

   
    rclpy.spin(sensor_publisher)
    sensor_publisher.destroy_node()

    rclpy.shutdown()

if __name__ == '__main__':
    main()