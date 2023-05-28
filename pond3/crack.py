from ultralytics import YOLO
import cv2

# build a new model from YAML
model = YOLO('yolov8n.pt')

# Train the model
model.train(data='data.yaml', epochs=2, imgsz=416)
model.val()

img1 = cv2.imread("datasets/test/images/1616.rf.c868709931a671796794fdbb95352c5a.jpg")
img2 = cv2.imread("datasets/test/images/1675.rf.e3aa3f8d28d0247ef0284dd46dacc29f.jpg")
img3 = cv2.imread("datasets/test/images/1686.rf.809fb1b51c607e5cf787e44ef4ddd7b8.jpg")
img4 = cv2.imread("datasets/test/images/1706.rf.011d213c21ec78896c36728dcbc156f5.jpg")
images = [img1, img2, img3, img4]

model.predict(source=images, conf=0.25, save=True)