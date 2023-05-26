from ultralytics import YOLO

# build a new model from YAML
model = YOLO('yolov8n.pt')

# Train the model
model.train(data='data.yaml', epochs=2, imgsz=416)

inp1 = "datasets/test/images/1616.rf.c868709931a671796794fdbb95352c5a.jpg"
inp2 = "datasets/test/images/1675.rf.e3aa3f8d28d0247ef0284dd46dacc29f.jpg"
inp3 = "datasets/test/images/1686.rf.809fb1b51c607e5cf787e44ef4ddd7b8.jpg"
inputs = [inp1, inp2, inp3]

model.val()
for inp in inputs:
    model.predict(source=inp)
