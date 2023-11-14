import time
import rclpy
from rclpy.node import Node

from std_msgs.msg import Header
from builtin_interfaces.msg import Time
from can_msgs.msg import Frame

class CANPublisher(Node):
    def __init__(self):
        super().__init__('can_publiser')
        self.publisher_ = self.create_publisher(
            Frame,
            'to_can_bus',
            1)

def main(args=None):
    rclpy.init(args=args)

    can_publisher = CANPublisher()

    while True:
        msg = Frame()
        msg.header.stamp = can_publisher.get_clock().now().to_msg()
        msg.header.frame_id = "can"
        msg.id = 0x555
        msg.is_rtr = False
        msg.is_extended = False
        msg.is_error = False
        msg.dlc = 8
        msg.data = [64, 32, 18, 19, 20, 21, 22, 23]
        can_publisher.publisher_.publish(msg)

        time.sleep(1)

    rclpy.spin(can_publiser)
    minimal_publisher.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
