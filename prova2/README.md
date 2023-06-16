# Visão Geral do Read Face
Read Face consiste em um projeto para a detecção de rostos em um vídeo.

# Como o Read Face funciona?
Ele utiliza a biblioteca cv2, capaz de fazer leitura e a análise de imagens e vídeos. Para esse projeto, o cv2 faz uma varredura frame a frame em busca de rostos, e desenha um retângulo onde ele encontra, com a função cv2.rectangle.