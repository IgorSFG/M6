import rclpy
from rclpy.node import Node

from turtlesim.msg import Pose
from geometry_msgs.msg import Twist

class TurtleSubscriber(Node):
    def __init__(self):
        super().__init__("turtle_subscriber")
        self.create_subscription(
            msg_type=Pose,
            topic="turtle1/pose",
            callback=self.timer_call,
            qos_profile=10
            )
        self.get_logger().info("subscriber is started")

    def timer_call(self,msg):
        self.get_logger().info("Turtle pose: x:%f, y:%f, theta:%f, linear_velocity:%f, angular_velocity:%f"%(msg.x,msg.y,msg.theta,msg.linear_velocity,msg.angular_velocity))

class TurtlePublisher(Node):
    def __init__(self):
        super().__init__("turtle_publisher")
        self.create_publisher(
            msg_type=Twist,
            topic="turtle1/cmd_vel",
            qos_profile=10
            )
        self.get_logger().info("publisher is started")
        self.timer = self.create_timer(timer_period_sec=0.5,timer_callback=self.publish_call)
        self.i = 0

    def publish_call(self):
        msg = Twist()
        msg.linear.x = 1.0
        msg.angular.z = 1.0
        self.get_logger().info("publishing: linear.x:%f, angular.z:%f"%(msg.linear.x,msg.angular.z))
        self.publisher_.publish(msg)

    def pose_callback(self,msg):
        self.get_logger().info("Turtle pose: x:%f, y:%f, theta:%f, linear_velocity:%f, angular_velocity:%f"%(msg.x,msg.y,msg.theta,msg.linear_velocity,msg.angular_velocity))


def main(args=None):
    rclpy.init(args=args)
    node = TurtleSubscriber()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__main__":
    main()