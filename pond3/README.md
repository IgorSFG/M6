# Projeto Crack
O nome em português pode soar estranho, mas em inglês, crack siguinifica rachadura, e por isso teve seu nome associado ao projeto, que tem justamente, a função de detectá-las. O projeto crack se baseia em um modelo de IA, que ao ser treinado com um conjunto de dados específicos, pode identificar rachaduras no ambiente.

# Como o Crack foi feito?
- Para a criação de um modelo de IA capaz de identificar rachaduras, foi usada a biblioteca ultralytics para a utilização do algorítimo YOLO, mais específicamente, a versão pré treinada da yolov8n.
- Para o treinamento detalhado, validação e teste do algorítimo, foi utilizado o [dataset personalizado](https://universe.roboflow.com/university-bswxt/crack-bphdr/dataset/2) desenvolvido pela Roboflow. O arquivo [data.yaml](data.yaml) é responsável por guiar o programa ao dataset para a realização de comandos.
- Finalizado o treinamento, o programa lista as imagens a serem testadas e o algorítimo tenta detectar as rachaduras presentes nelas, salvando o resultado quando concluído.

# Crack em Ação!
Para ver o Crack em funcionamento, basta executar o arquivo python com:
```
python3 crack.py
```
Após o treinamento, o resultado são as imagens com as rachaduras acentuadas salvas :D

[RESULTADO](resultado.mp4)
