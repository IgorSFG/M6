import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry
from tf_transformations import euler_from_quaternion

class BurguerController(Node):

    def __init__(self):
        super().__init__('burguer_controller')
        self.publisher = self.create_publisher(
            msg_type=Twist,
            topic='/cmd_vel',
            qos_profile=10)
        
        self.subscription = self.create_subscription(
            msg_type=Odometry,
            topic='/odom',
            callback=self.odom_callback,
            qos_profile=10)
        
        self.subscription.enabled = True
        self.odom_data = None

        timer_period = 0.1  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)

    def odom_callback(self, msg):
        self.odom_data = msg

    def timer_callback(self):
        if self.odom_data is not None:
            x = self.odom_data.pose.pose.position.x
            y = self.odom_data.pose.pose.position.y
            z = self.odom_data.pose.pose.position.z
            ang = self.odom_data.pose.pose.orientation
            _, _, theta = euler_from_quaternion([ang.x, ang.y, ang.z, ang.w])
            self.get_logger().info(f"x={x}, y={y}, z={z}, theta={theta}")

        cmd = Twist()
        cmd.linear.x = 0.1
        self.publisher.publish(cmd)

def main(args=None):
    rclpy.init(args=args)
    burguer = BurguerController()
    rclpy.spin(burguer)
    burguer.destroy_node()
    rclpy.shutdown()