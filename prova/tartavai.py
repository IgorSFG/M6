# Importa as bibliotecas necessárias
import rclpy
import time
from rclpy.node import Node
from geometry_msgs.msg import Twist

class Fila():
    def __init__(self, route):
        self.route = route
        self.size = len(route)

    def get(self):
        if self.size > 0:
            self.outvalue = self.route[0]
            self.route = self.route[1:]
            self.size -= 1
            print(self.route)
            return self.outvalue
        else: return 0.0

class Pilha():
    def __init__(self, route):
        self.route = route
        self.size = len(route)

    def get(self):
        if self.size > 0:
            self.outvalue = self.route[-1]
            self.route = self.route[:-1]
            self.size -= 1
            print(self.route)
            return self.outvalue
        else: return 0.0
    

# Classe que controla o movimento do turtlesim
class TurtleController(Node):
    def __init__(self):
        super().__init__('turtle_controller') # Inicializa o nó
        self.publisher = self.create_publisher(Twist, 'turtle1/cmd_vel', 10) # Cria o publisher
        self.twist = Twist() # Cria a mensagem Twist

        self.route = [[0.0, 0.5], [0.5, 0.0], [0.0, 0.5], [0.5, 0.0], [0.0, 1.0], [1.0, 0.0]]
        self.fila = Fila(self.route)
        self.pilha = Pilha(self.route)

        self.speed = 1.0

    def Go(self):
        self.go = self.fila.get()
        self.x = float(self.go[0])
        self.y = float(self.go[1])

        self.twist.linear.x = self.speed
        self.time = abs(self.x / self.twist.linear.x) # Calcula o tempo de movimento
        self.publisher.publish(self.twist) # Publica a mensagem
        print("Go X for " + str(self.time) + " seconds")
        time.sleep(self.time) # Espera o tempo de movimento
        self.twist.linear.x = 0.0
        self.publisher.publish(self.twist)

        self.twist.linear.y = self.speed
        self.time = abs(self.y / self.twist.linear.y) # Calcula o tempo de movimento
        self.publisher.publish(self.twist) # Publica a mensagem
        print("Go Y for " + str(self.time) + " seconds")
        time.sleep(self.time) # Espera o tempo de movimento
        self.twist.linear.y = 0.0
        self.publisher.publish(self.twist)

        self.Stop()

    def Back(self):
        self.back = self.pilha.get()
        self.x = float(self.back[0])
        self.y = float(self.back[1])

        self.twist.linear.x = -self.speed
        self.time = abs(self.x / self.twist.linear.x) # Calcula o tempo de movimento
        self.publisher.publish(self.twist) # Publica a mensagem
        print("Back X for " + str(self.time) + " seconds")
        time.sleep(self.time) # Espera o tempo de movimento
        self.twist.linear.x = 0.0
        self.publisher.publish(self.twist)

        self.twist.linear.y = -self.speed
        self.time = abs(self.y / self.twist.linear.y) # Calcula o tempo de movimento
        self.publisher.publish(self.twist) # Publica a mensagem
        print("Back Y for " + str(self.time) + " seconds")
        time.sleep(self.time) # Espera o tempo de movimento
        self.twist.linear.y = 0.0
        self.publisher.publish(self.twist)

        self.Stop()

    def Stop(self):
        self.twist.linear.x = 0.0
        self.twist.linear.y = 0.0
        self.publisher.publish(self.twist)
        if self.fila.size > 0: self.Go()
        elif self.pilha.size > 0: self.Back()


def main(args=None):
    rclpy.init(args=args) # Inicializa o ROS
    turtle = TurtleController() # Cria o objeto turtle

    print("Tartavai...")
    time.sleep(1.0)

    turtle.Go()

    turtle.destroy_node()
    rclpy.shutdown()


# Roda a função main quando o arquivo é executado
if __name__ == '__main__':
    main()
