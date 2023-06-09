from rclpy.node import Node
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry
from tf_transformations import euler_from_quaternion
from supabase import create_client, Client
from Pose import Pose
import rclpy
import os
import random

# Credenciais do Supabase
url: str = "https://etxrmfvkgcrpyzdpvvrn.supabase.co"
key: str = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImV0eHJtZnZrZ2NycHl6ZHB2dnJuIiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTY4NjY4MDk4MCwiZXhwIjoyMDAyMjU2OTgwfQ.BosLYjeNsyNMhs88FlV_PNzH9QRBqeBgAUJJU4SzlQw"
supabase: Client = create_client(url, key)


# Define a classe BotController, que representa o nó de controle do robô
class BotController(Node):
    # Inicializa o nó com período de controle de 0.05s e uma fila vazia
    def __init__(self, control_period=2.0):
        super().__init__("bot_controller")

        # Cria um assinante para receber a pose do robô
        self.subscription = self.create_subscription(
            msg_type=Odometry,
            topic="odom",
            callback=self.odom_callback,
            qos_profile=10
        )

        self.odom_data = None

        self.timer = self.create_timer(control_period, self.timer_callback)

        # Função que recebe os dados de odometria do robô burguer
    def odom_callback(self, msg):
        self.odom_data = msg

    # Callback para receber pose atual
    def timer_callback(self):
        if self.odom_data is not None:

            # Decompõe a mensagem de pose em x, y, z e theta
            x = self.odom_data.pose.pose.position.x
            y = self.odom_data.pose.pose.position.y
            z = self.odom_data.pose.pose.position.z
            ang = self.odom_data.pose.pose.orientation
            _, _, theta = euler_from_quaternion([ang.x, ang.y, ang.z, ang.w])

            # Atualiza a pose e rotação atuais
            self.current_pose = Pose(x=x, y=y, theta=theta)

            x = round(y, 2)
            y = round(x, 2)
            theta = round(theta, 2)
            id = random.randint(0, 2**16)

            try:
                data, count = supabase.table('Coordinates').insert({"x": x, "y": y, "theta": theta, "id": id}).execute()
                print("Dados inseridos no banco de dados.")
            except Exception:
                print("Erro ao inserir dados no banco de dados.")


rclpy.init()
tc = BotController()
rclpy.spin(tc)