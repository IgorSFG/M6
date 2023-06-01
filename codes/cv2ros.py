import cv2
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from cv_bridge import CvBridge

class ImageSuper(Node):
    def __init__(self):
        super().__init__("image_super")
        
        self.publisher = self.create_publisher(
            msg_type=Image,
            topic="image",
            qos_profile=10
            )
        
        self.subscription = self.create_subscription(
            msg_type=Image,
            topic="image",
            callback=self.image_callback,
            qos_profile=10
            )
        
        self.timer = self.create_timer(0.1, self.timer_callback)
        self.bridge = CvBridge()
        self.capture = cv2.VideoCapture(0)

    def image_callback(self, msg):
        self.get_logger().info("Receiving an image")
        frame = self.bridge.imgmsg_to_cv2(msg)
        cv2.imshow("Video", frame)
        cv2.waitKey(25)
        if cv2.waitKey(1) == ord('q'):
            exit(0)

    def timer_callback(self):
        ret, frame = self.capture.read()
        if not ret:
            self.get_logger().error("Can't receive frame (stream end?). Exiting ...")
            exit(1)
        
        msg = self.bridge.cv2_to_imgmsg(frame)
        self.publisher.publish(msg)
        self.get_logger().info("Image published")

def main(args=None):
    rclpy.init(args=args)
    img_s = ImageSuper()
    rclpy.spin(img_s)
    img_s.destroy_node()
    rclpy.shutdown()