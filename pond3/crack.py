from ultralytics import YOLO
from PIL import Image
import cv2

# build a new model from YAML
model = YOLO('yolov8n.pt')

# Train the model
model.train(data='data.yaml', epochs=2, imgsz=416)
model.val()

img1 = Image.open("datasets/test/images/1616.rf.c868709931a671796794fdbb95352c5a.jpg")
img2 = Image.open("datasets/test/images/1675.rf.e3aa3f8d28d0247ef0284dd46dacc29f.jpg")
img3 = Image.open("datasets/test/images/1686.rf.809fb1b51c607e5cf787e44ef4ddd7b8.jpg")
inputs = [img1, img2, img3]

model.predict(source=inputs, imgsz=416, conf=0.25, show=True, save=True)
