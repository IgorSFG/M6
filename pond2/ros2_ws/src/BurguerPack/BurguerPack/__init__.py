# Importa as bibliotecas necessárias
import time
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry
from tf_transformations import euler_from_quaternion
from .ElementLine import Line

# Função que define a rota percorrida pelo robô burguer
def Route():
    route = Line()
    route.push(1.0)
    route.push("ang45")
    route.push(-1.0)
    route.push(2.0)
    return route

# Classe que controla o movimento do robô burguer
class BurguerController(Node):
    def __init__(self, timer_period=0.2):
        super().__init__('burguer_controller')
        
        # Cria o publisher de tipo Twist no tópico /cmd_vel
        self.publisher = self.create_publisher(
            msg_type=Twist,
            topic='/cmd_vel',
            qos_profile=10)
        
        # Cria o subscriber de tipo Odometry no tópico /odom
        self.subscription = self.create_subscription(
            msg_type=Odometry,
            topic='/odom',
            callback=self.odom_callback,
            qos_profile=10)
        
        self.twist = Twist() # Cria a mensagem Twist
        self.subscription.enabled = True # Habilita o subscriber
        self.odom_data = None # Inicializa a variável odom_data
        self.target = None # Inicializa a variável target
        self.linear_speed = 0.2 # Velocidade linear do robô burguer
        self.angular_speed = 0.2 # Velocidade angular do robô burguer

        self.route = Route() # Cria a rota do robô burguer

        self.get_logger().info("Burguer Controller has been started with route: "+ str(self.route)) # Informa que o Burguer Controller foi iniciado

        time.sleep(2) # Espera 1 segundo

        self.timer = self.create_timer(timer_period, self.timer_callback) # Cria o timer com o período definido

    # Função que recebe os dados de odometria do robô burguer
    def odom_callback(self, msg):
        self.odom_data = msg

    # Função que converte graus para radianos
    def angle_degrees_to_rads(self, angle):
        return angle * 3.14 / 180.0

    # Função que controla o movimento do robô burguer a cada período de tempo
    def timer_callback(self):
        # Define os valores de posição e orientação do robô burguer
        if self.odom_data is not None:
            x = self.odom_data.pose.pose.position.x
            y = self.odom_data.pose.pose.position.y
            z = self.odom_data.pose.pose.position.z
            ang = self.odom_data.pose.pose.orientation
            _, _, theta = euler_from_quaternion([ang.x, ang.y, ang.z, ang.w])
            self.get_logger().info("x={:.4f}, y={:.4f}, z={:.4f}, theta={:.4f}".format(x, y, z, theta))

            # Verifica se há um alvo a ser atingido, se não houver, o robô burguer para
            if self.route.head is None:
                self.get_logger().info("Route finished")
                self.twist.linear.x = 0.0
                self.twist.angular.z = 0.0
                self.publisher.publish(self.twist)
            
            # Verifica se o alvo é um ângulo, se for, o robô burguer gira até atingir a margem de erro prevista
            elif isinstance(self.route.head.value, str):
                self.route_target = float(self.route.head.value[3:])
                self.route_target = self.angle_degrees_to_rads(self.route_target)
                if self.target is None: self.target = theta + self.route_target
                if abs(theta - self.target) > 0.3:
                    self.twist.angular.z = self.angular_speed if self.target > theta else -self.angular_speed
                    self.publisher.publish(self.twist)
                else:
                    self.twist.angular.z = 0.0
                    self.publisher.publish(self.twist)
                    self.route.pop()
                    self.target = None
                    self.get_logger().info("Route: "+ str(self.route))
                    
                    

            # Verifica se o alvo é uma distância, se for, o robô burguer anda até atingir a margem de erro prevista
            elif isinstance(self.route.head.value, float):
                self.route_target = self.route.head.value
                if self.target is None: self.target = x + self.route_target
                if abs(x - self.target) > 0.3:
                    self.twist.linear.x = self.linear_speed if self.target > x else -self.linear_speed
                    self.publisher.publish(self.twist)
                else:
                    self.twist.linear.x = 0.0
                    self.publisher.publish(self.twist)
                    self.route.pop()
                    self.target = None
                    self.get_logger().info("Route: "+ str(self.route))

def main(args=None):
    rclpy.init(args=args) # Inicia o ROS
    burguer = BurguerController()  # Cria o Burguer Controller
    rclpy.spin(burguer) # Mantém o Burguer Controller ativo
    burguer.destroy_node() # Destroi o Burguer Controller
    rclpy.shutdown() # Encerra o ROS