import rclpy
from rclpy.node import Node
from geometry_msgs.msg import TransformStamped
from tf2_msgs.msg import TFMessage
import tf2_ros

class ModelPositionSubscriber(Node):

    def __init__(self):
        super().__init__('model_position_subscriber')
        self.tf_buffer = tf2_ros.Buffer()
        self.tf_listener = tf2_ros.TransformListener(self.tf_buffer, self)

        self.subscription = self.create_subscription(TFMessage, '/tf', self.tf_callback, 10)

    def tf_callback(self, msg):
        for transform in msg.transforms:
            if transform.child_frame_id == 'base_link':  # Replace 'model_name' with the name of your model
                position = transform.transform.translation
                self.get_logger().info(f"Model position: x={position.x}, y={position.y}, z={position.z}")

def main(args=None):
    rclpy.init(args=args)

    model_position_subscriber = ModelPositionSubscriber()
    rclpy.spin(model_position_subscriber)

    model_position_subscriber.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
