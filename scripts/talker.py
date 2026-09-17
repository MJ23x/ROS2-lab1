#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from ackermann_msgs.msg import AckermannDriveStamped

class Talker(Node):
    def __init__(self):
        super().__init__('talker')

        # Declare parameters
        self.declare_parameter('v', 0.0)
        self.declare_parameter('d', 0.0)

        #Create publisher
        self.publisher_ = self.create_publisher(AckermannDriveStamped, 'drive', 10)

        #Publish as fast as possible 0.001s in this case
        self.timer = self.create_timer(0.001, self.timer_callback)

    def timer_callback(self):

        #Fetch the most recent parameters
        v = self.get_parameter('v').get_parameter_value().double_value
        d = self.get_parameter('d').get_parameter_value().double_value

        #msg construction
        msg = AckermannDriveStamped()
        msg.drive.speed = float(v)
        msg.drive.steering_angle = float(d)

        # Finally publish to the topic
        self.publisher_.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    node = Talker()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

