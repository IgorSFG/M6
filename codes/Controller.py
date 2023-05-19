#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Joy
from geometry_msgs.msg import Twist

class MyRobotController(Node):
    def __init__(self):
        super().__init__('my_robot_controller')
        print("Starting up...")
        self.sub = self.create_subscription(
            msg_type=Joy,
            topic='/joy',
            callback=self.joy_callback,
            qos_profile=10)
        
        self.pub = self.create_publisher(
            msg_type=Twist,
            topic='/cmd_vel',
            qos_profile=10)

    def joy_callback(self, data):
        axes = data.axes

        # Map joystick axes to robot velocity
        linear_velocity = axes[1] * 2.0  # Forward/backward motion
        angular_velocity = axes[0] * 2.0  # Turn left/right

        self.get_logger().info(str(linear_velocity) + ", " + str(angular_velocity))

        # Create a Twist message to send to the robot
        cmd_vel = Twist()
        cmd_vel.linear.x = linear_velocity
        cmd_vel.angular.z = angular_velocity

        # Publish the Twist message to control the robot
        self.pub.publish(cmd_vel)

def main(args=None):
    rclpy.init(args=args)
    my_robot_controller = MyRobotController()
    rclpy.spin(my_robot_controller)
    my_robot_controller.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
