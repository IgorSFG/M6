# Bibliotecas necesarias
from ultralytics import YOLO
import cv2

# carregar o modelo
model = YOLO('yolov8n.pt')
# treina o modelo
model.train(data='data.yaml', epochs=2, imgsz=416)
# valida o modelo
model.val()

# agrupa as imagens para teste
img1 = cv2.imread("datasets/test/images/1616.rf.c868709931a671796794fdbb95352c5a.jpg")
img2 = cv2.imread("datasets/test/images/1675.rf.e3aa3f8d28d0247ef0284dd46dacc29f.jpg")
img3 = cv2.imread("datasets/test/images/1686.rf.809fb1b51c607e5cf787e44ef4ddd7b8.jpg")
img4 = cv2.imread("datasets/test/images/1706.rf.011d213c21ec78896c36728dcbc156f5.jpg")
images = [img1, img2, img3, img4]

# testa o modelo com as imagens selecionadas, com confiança de 25% e salva os resultados
model.predict(source=images, conf=0.25, save=True)