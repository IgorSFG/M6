# Visão Geral do Burguer!
O projeto Burguer consiste em um pacote em ROS capaz de movimentar um robô no ambiente de simulação do Gazebo de maneira controlada ao mesmo tempo que possibilita a visualização de seus dados de odometria.

# Como o Burguer foi feito?
Primeiramente, foi feita a criação de um pacote em ROS, com um script capaz de enviar e receber dados do ambiente de simulção Gazebo. Esse script possuí as seguintes bibliotecas:
- rclpy e Node, responsáveis por instanciar o cliente ROS e a classe de nó.
- Twist de geometry_msgs.msg, que define o tipo de mensagem como Twist para a realização do movimento do robô.
- Odometry de nav_msgs.msg, que define o tipo de extração de tipo odometria.
- euler_from_quaternion de tf_transformations, que possibilita o cálculo para a obtenção da posição de rotação do robô.
- Line de ElementLine, que é um arquivo pythom criado em sala de aula para servir de estrutura de dados, nesse caso, uma lista encadeada de tipo fila.

Definido as bibliotecas, foi criada a classe que herdaria o nó chamado de BurguerController. Nela foram instanciadas o construtor da classe do nó, definindo como 'burguer_controller', o editor que pública mensagens do tipo Twist no tópico '/cmd_vel' e também o subscriber que recebe mensagens de odometria no tópico /odom.

Para a movimentação do robô burguer, foram idealizadas 4 funções:

- Route tem o papel de adicionar os valores desejados para a movimentação do burguer na lista encadeada importada. Ela consegue receber valores númericos que determinam o quanto o robô irá para frente ou pra trás, e também o ângulo que ele rotacionará, sendo distinguido a partir do prefixo "ang" na frente do número.

- angle_degrees foi criado para possibilitar a utlização de graus no envio de dados de rotação do robô burguer. Ela converte o valor fornecido para radianos automáticamente.

- odom_callback é a função que recebe os dados de osometria, ela é responsável por armazenar tais valores.

- timer_callback roda a cada 0.1 segundo, ela é responsável por toda a movimentação do robô burguer. Primeiramente, é certificado que o robô já conseguiu se localizar através de seus dados de osometria, e com tais dados, graças a biblioteca de euler_from_quaternion, é possível também determinar o ângulo de rotação que o robô está submetido. Após todos os dados estarem completos, começa o processo de movimentação do robô. Primeiramente, é feito a distinção se o valor recebido é um ângulo a ser rotacionado ou uma distância a ser percorrida, depois, com base na posição atual no robô, será determinado a posição final dele com base no valor recebido, desse modo ele saberá aonde deve parar com uma pequena margem de erro. O programa é inteligente o suficiente para ajustar o sentido da velocidade para se aproximar da posição desejada da melhor forma possível, e quando isso ocorre, ele descarta o alvo atual da lista encadeada e irá para o próximo, se não houver, é porque a rota já está finalizada!

- a função "main", como o nome diz, é a princípal do script, ela é responsável por inicializar o ROS, o objeto da classe BurguerController, que ao ser finalizado, encerra o nó e o programa ROS.

# Burguer em Ação!
Inicializando o nó do gazebo em um terminal com:
```
 ros2 launch turtlebot3_gazebo empty_world.launch.py
```

No diretório ros2_ws, é necessário compilar o pacote ROS com:
```
colcon build --packages-select BurguerPack
```

E então compilá-lo:
```
source install/setup.bash
```

Após tudo isso, basta rodar o pacote e seu executável:
```
ros2 run BurguerPack Burguer
```
O resultado é o Burguer indo de lá pra cá :D
[Vídeo do Burguer](https://drive.google.com/file/d/1VPINDHlSIXMBFsLTGfJrXGOgv9BmI5S_/view?usp=sharing)