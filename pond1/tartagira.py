#!/usr/bin/env python3

# Importa as bibliotecas necessárias
import rclpy
import time
from rclpy.node import Node
from geometry_msgs.msg import Twist

# Classe que controla o movimento do turtlesim
class TurtleController(Node):
    def __init__(self):
        super().__init__('turtle_controller') # Inicializa o nó
        self.publisher = self.create_publisher(Twist, 'turtle1/cmd_vel', 10) # Cria o publisher
        self.twist = Twist() # Cria a mensagem Twist

    # Função que converte graus para radianos
    def angle_degrees_to_rads(self, angle):
        return angle * 3.14 / 180.0

    # Função que move o turtlesim para frente
    def move_forward(self , distance):
        self.twist.linear.x = 1.0 # Velocidade da tartaruga
        self.twist.angular.z = 0.0 # Velocidade de rotação da tartaruga
        self.time = abs(distance / self.twist.linear.x) # Calcula o tempo de movimento
        self.publisher.publish(self.twist) # Publica a mensagem
        print("Moving forward for " + str(self.time) + " seconds")
        time.sleep(self.time) # Espera o tempo de movimento

    # Função que vira o turtlesim para a esquerda
    def turn_left(self, angle):
        self.twist.linear.x = 0.0 # Velocidade da tartaruga
        self.twist.angular.z = 1.0 # Velocidade de rotação da tartaruga
        angle = self.angle_degrees_to_rads(angle) # Converte o ângulo para radianos
        self.time = abs(angle / self.twist.angular.z) # Calcula o tempo de movimento
        self.publisher.publish(self.twist) # Publica a mensagem
        print("Turning left for " + str(self.time) + " seconds")
        time.sleep(self.time) # Espera o tempo de movimento

    # Função que vira o turtlesim para a direita
    def turn_right(self, angle):
        self.twist.linear.x = 0.0 # Velocidade da tartaruga
        self.twist.angular.z = -1.0 # Velocidade de rotação da tartaruga
        angle = self.angle_degrees_to_rads(angle) # Converte o ângulo para radianos
        self.time = abs(angle / self.twist.angular.z) # Calcula o tempo de movimento
        self.publisher.publish(self.twist) # Publica a mensagem
        print("Turning right for " + str(self.time) + " seconds")
        time.sleep(self.time) # Espera o tempo de movimento

def main(args=None):
    rclpy.init(args=args) # Inicializa o ROS
    turtle = TurtleController() # Cria o objeto turtle

    # Começa a desenho
    print("Drawing Tartagira...")
    time.sleep(2.0)
    
    # draw the body
    turtle.move_forward(0.5)
    turtle.turn_left(45.0)
    turtle.turn_left(45.0)
    turtle.move_forward(0.5)
    turtle.turn_right(45.0)
    turtle.move_forward(0.25)
    turtle.turn_left(45.0)
    turtle.move_forward(2.0)
    turtle.move_forward(2.0)
    print("Body drawn")
    
    # draw the cylinder
    turtle.turn_right(45.0)
    turtle.turn_right(45.0)
    turtle.turn_right(45.0)
    turtle.move_forward(0.5)
    turtle.turn_right(45.0)
    turtle.move_forward(2.0)
    turtle.turn_right(45.0)
    turtle.move_forward(0.5)
    turtle.turn_right(45.0)
    turtle.turn_right(45.0)
    turtle.turn_right(45.0)
    turtle.move_forward(2.0)
    turtle.move_forward(1.0)
    print("Cylinder drawn")

    # draw the head
    turtle.turn_left(45.0)
    turtle.move_forward(0.5)
    turtle.turn_left(45.0)
    turtle.move_forward(1.0)
    turtle.turn_left(45.0)
    turtle.move_forward(0.5)
    turtle.turn_left(45.0)
    turtle.move_forward(0.5)
    print("Head drawn")

    # draw the helmet
    turtle.move_forward(0.75)
    turtle.turn_left(45.0)
    turtle.turn_left(45.0)
    turtle.move_forward(1.5)
    turtle.turn_left(45.0)
    turtle.turn_left(45.0)
    turtle.move_forward(0.75)
    turtle.turn_left(45.0)
    turtle.turn_left(45.0)
    turtle.move_forward(1.5)
    turtle.turn_left(45.0)
    turtle.turn_left(45.0)
    turtle.move_forward(0.75)
    turtle.move_forward(2.0)
    print("Helmet drawn")

    #draw the legs
    turtle.move_forward(0.5)
    turtle.turn_left(45.0)
    turtle.turn_left(45.0)
    turtle.move_forward(0.5)
    turtle.turn_left(45.0)
    turtle.turn_left(45.0)
    turtle.move_forward(0.5)
    turtle.turn_right(45.0)
    turtle.turn_right(45.0)
    turtle.move_forward(0.5)
    turtle.turn_right(45.0)
    turtle.turn_right(45.0)
    turtle.move_forward(0.5)
    print("Legs drawn")

    turtle.destroy_node()
    rclpy.shutdown()


# Roda a função main quando o arquivo é executado
if __name__ == '__main__':
    main()
