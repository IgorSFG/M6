# Visão Geral do Tartagira
O projeto da Tartagira consiste na realização de um desenho através do nó de simulação do turtlesim e envio de mensagens que regram a movimentação da tartaruga princípal, que faz o desenho.

# Como o Tartagira foi feito?
Primeiramente foi determinado o interpretador "#!/usr/bin/env python3" e as bibliotecas "rclpy", "Node" e "Twist" de "geometry_msgs.msg", que servem, respectivamente, para instanciar o cliente ROS, a classe de nó e o tipo de mensagem como Twist para a realização do movimento da tartaruga. 

Após isso, foi definida a classe que herdaria a classe nó chamada de TurtleController. Nela foram instanciadas o construtor da classe do nó, definindo como 'turtle_controller', o editor que pública mensagens do tipo Twist no tópico 'turtle1/cmd_vel', e com tamanho de fila 10.

Para os movimentos da tartaruga, foram pensadas em 4 funções:

- move_forward serve para mover a tartaruga pra frente, ela recebe a distância como argumento que se traduz no tempo em que o turtlesim fica recebendo os dados dessa função, que no caso é a informação da tartaruga se movendo pra frente.
- turn_left e turn_right rotacionam a tartaruga para a direção no qual deseja-se que o move_foward a mande. A função recebe o ângulo como argumento, que nesse caso específico foi preferível a ultização de graus. Para isso então foi criada mais uma função.
- angle_degrees foi justamente criada para possibilitar a utlização de graus como argumento das funções de rotação da tartaruga. Ela converte o valor fornecido para radianos automáticamente.

A função "main", como o nome diz, é a princípal do script, ela roda quando o arquivo é executado. Nela é inicialiado o ROS , o objeto da classe TurtleController é criado e todos os movimentos que a tartaruga precisará fazer estão nela, cada um com seus argumentos específicos para a realização do desenho.

Feito o desenho, a função encerra o nó e o programa ROS.

# Tartagira em Ação!
Inicializado o nó do turtlesim em um terminal com:
```
ros2 run turtlesim turtlesim_node
```
Basta executar o arquivo python:
```
./tartagira.py
```
O resultado é um desenho bem legal:
[Vídeo do desenho](https://drive.google.com/file/d/1IP8-7CgHybe9J5YoDg-3Prv1ej7T2G2e/view?usp=sharing)
