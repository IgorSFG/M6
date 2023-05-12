import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry
from tf_transformations import euler_from_quaternion
from .ElementLine import Line

def Route():
    route = Line()
    route.push(-1)
    #route.push("ang90")
    route.push(1)
    #route.push("ang90")
    route.push(-1)
    #route.push("ang90")
    route.push(1)
    #route.push("ang90")
    return route

class BurguerController(Node):

    def __init__(self, timer_period=0.1):
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
        
        self.twist = Twist() # Cria a mensagem Twist
        self.subscription.enabled = True
        self.odom_data = None
        self.target = None
        self.linear_speed = 0.1
        self.angular_speed = 0.5

        self.route = Route()

        self.timer = self.create_timer(timer_period, self.timer_callback)

    def odom_callback(self, msg):
        self.odom_data_ = msg

    def timer_callback(self):
        if self.odom_data is not None:
            x = self.odom_data.pose.pose.position.x
            y = self.odom_data.pose.pose.position.y
            z = self.odom_data.pose.pose.position.z
            ang = self.odom_data.pose.pose.orientation
            _, _, theta = euler_from_quaternion([ang.x, ang.y, ang.z, ang.w])
            self.get_logger().info("x={:.4f}, y={:.4f}, z={:.4f}, theta={:.4f}".format(x, y, z, theta))
            
            if isinstance(self.route.head.value, str):
                self.route.head.value = int(self.route.head.value[3:])
                if self.target is None: self.target = theta + self.route.head.value
                if abs(theta - self.route.head.value) > 0.05:
                    self.twist.angular.z = self.angular_speed if self.route.head.value > theta else -self.angular_speed
                    self.publisher.publish(self.twist)
                else:
                    self.route.pop()
                    self.target = None
            
            elif isinstance(self.route.head.value, int):
                if self.target is None: self.target = theta + self.route.head.value
                if abs(x - self.route.head.value) > 0.05:
                    self.twist.linear.x = self.linear_speed if self.route.head.value > x else -self.linear_speed
                    self.publisher.publish(self.twist)
                else:
                    self.route.pop()
                    self.target = None
            
            else: 
                self.get_logger().info("Route finished")
                self.twist.linear.x = 0.0
                self.twist.angular.z = 0.0

# def TravelRoute(route, burguer):
#     while route.size > 0:
#         if isinstance(route.head.value, str):
#             route.head.value = int(route.head.value[3:])
#             if route.head.value <= 0:
#                 burguer.turn_right(route.head.value)
#             else: burguer.turn_left(route.head.value)
#             route.pop()
#         else:
#             if route.head.value <= 0:
#                 burguer.move_backward(route.head.value)
#             else: burguer.move_forward(route.head.value)
#             route.pop()

def main(args=None):
    rclpy.init(args=args)
    burguer = BurguerController()
    rclpy.spin(burguer)
    burguer.destroy_node()
    rclpy.shutdown()