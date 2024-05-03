import rclpy
from rclpy.node import Node
from geometry_msgs.msg import WrenchStamped
import matplotlib.pyplot as plt
from collections import deque
from tf2_msgs.msg import TFMessage
import tf2_ros

class ForceTorqueVisualizer(Node):

    def __init__(self):
        super().__init__('force_torque_visualizer')

        self.tf_buffer = tf2_ros.Buffer()
        self.tf_listener = tf2_ros.TransformListener(self.tf_buffer, self)

        self.tfsub = self.create_subscription(TFMessage, '/tf', self.tf_callback, 10)
        self.tfsub
        self.num_joints=2
        
        self.subscription1 = self.create_subscription(WrenchStamped,'/joint_1',self.joint_1_callback,10)
        self.subscription2 = self.create_subscription(WrenchStamped,'/joint_2',self.joint_2_callback,10)
        self.subscription3 = self.create_subscription(WrenchStamped,'/joint_3',self.joint_3_callback,10)
        self.subscription4 = self.create_subscription(WrenchStamped,'/joint_4',self.joint_4_callback,10)
        self.subscription5 = self.create_subscription(WrenchStamped,'/joint_5',self.joint_5_callback,10)
        self.subscription6 = self.create_subscription(WrenchStamped,'/joint_6',self.joint_6_callback,10)
        self.subscription7 = self.create_subscription(WrenchStamped,'/joint_7',self.joint_7_callback,10)
        self.subscription8 = self.create_subscription(WrenchStamped,'/joint_8',self.joint_8_callback,10)
        self.subscription9 = self.create_subscription(WrenchStamped,'/joint_9',self.joint_9_callback,10)
        self.subscription1  # prevent unused variable warning
        self.subscription2
        self.subscription3
        self.subscription4
        self.subscription5
        self.subscription6
        self.subscription7
        self.subscription8
        self.subscription9

        self.declare()
        self.fig, self.axs = plt.subplots(3, 1, figsize=(10, 8))
        self.fig2, self.axs2 = plt.subplots(3, 1, figsize=(10, 8))
        self.fig3, self.axs3 = plt.subplots(3, 1, figsize=(10, 8))
    
    def declare(self):
        len=10

        self.position_x = deque(maxlen=len)
        self.position_y = deque(maxlen=len)
        self.position_z = deque(maxlen=len)

        
        self.joint1_force_x_data = deque(maxlen=len)  # Limiting the deque size to 100 for better visualization
        self.joint1_force_y_data = deque(maxlen=len)
        self.joint1_force_z_data = deque(maxlen=len)
        self.joint1_torque_x_data = deque(maxlen=len)
        self.joint1_torque_y_data = deque(maxlen=len)
        self.joint1_torque_z_data = deque(maxlen=len)

        self.joint2_force_x_data = deque(maxlen=len)  
        self.joint2_force_y_data = deque(maxlen=len)
        self.joint2_force_z_data = deque(maxlen=len)
        self.joint2_torque_x_data = deque(maxlen=len)
        self.joint2_torque_y_data = deque(maxlen=len)
        self.joint2_torque_z_data = deque(maxlen=len)

        self.joint3_force_x_data = deque(maxlen=len)  
        self.joint3_force_y_data = deque(maxlen=len)
        self.joint3_force_z_data = deque(maxlen=len)
        self.joint3_torque_x_data = deque(maxlen=len)
        self.joint3_torque_y_data = deque(maxlen=len)
        self.joint3_torque_z_data = deque(maxlen=len)

        self.joint4_force_x_data = deque(maxlen=len)  
        self.joint4_force_y_data = deque(maxlen=len)
        self.joint4_force_z_data = deque(maxlen=len)
        self.joint4_torque_x_data = deque(maxlen=len)
        self.joint4_torque_y_data = deque(maxlen=len)
        self.joint4_torque_z_data = deque(maxlen=len)

        self.joint5_force_x_data = deque(maxlen=len)  
        self.joint5_force_y_data = deque(maxlen=len)
        self.joint5_force_z_data = deque(maxlen=len)
        self.joint5_torque_x_data = deque(maxlen=len)
        self.joint5_torque_y_data = deque(maxlen=len)
        self.joint5_torque_z_data = deque(maxlen=len)

        self.joint6_force_x_data = deque(maxlen=len)  
        self.joint6_force_y_data = deque(maxlen=len)
        self.joint6_force_z_data = deque(maxlen=len)
        self.joint6_torque_x_data = deque(maxlen=len)
        self.joint6_torque_y_data = deque(maxlen=len)
        self.joint6_torque_z_data = deque(maxlen=len)

        self.joint7_force_x_data = deque(maxlen=len)  
        self.joint7_force_y_data = deque(maxlen=len)
        self.joint7_force_z_data = deque(maxlen=len)
        self.joint7_torque_x_data = deque(maxlen=len)
        self.joint7_torque_y_data = deque(maxlen=len)
        self.joint7_torque_z_data = deque(maxlen=len)

        self.joint8_force_x_data = deque(maxlen=len)  
        self.joint8_force_y_data = deque(maxlen=len)
        self.joint8_force_z_data = deque(maxlen=len)
        self.joint8_torque_x_data = deque(maxlen=len)
        self.joint8_torque_y_data = deque(maxlen=len)
        self.joint8_torque_z_data = deque(maxlen=len)

        self.joint9_force_x_data = deque(maxlen=len)  
        self.joint9_force_y_data = deque(maxlen=len)
        self.joint9_force_z_data = deque(maxlen=len)
        self.joint9_torque_x_data = deque(maxlen=len)
        self.joint9_torque_y_data = deque(maxlen=len)
        self.joint9_torque_z_data = deque(maxlen=len)
    
    def plot(self):
        #X - values
        self.axs[0].clear()
        self.axs[0].plot(self.joint1_force_x_data, label='Joint 1 Force X')
        self.axs[0].plot(self.joint2_force_x_data, label='Joint 2 Force X')
        self.axs[0].plot(self.joint3_force_x_data, label='Joint 3 Force X')
        self.axs[0].plot(self.joint4_force_x_data, label='Joint 4 Force X')
        self.axs[0].plot(self.joint5_force_x_data, label='Joint 5 Force X')
        self.axs[0].plot(self.joint6_force_x_data, label='Joint 6 Force X')
        self.axs[0].plot(self.joint7_force_x_data, label='Joint 7 Force X')
        self.axs[0].plot(self.joint8_force_x_data, label='Joint 8 Force X')
        self.axs[0].plot(self.joint9_force_x_data, label='Joint 9 Force X')
        self.axs[0].legend(loc='upper left', bbox_to_anchor=(1, 1))
        self.axs[0].set_title('Force X Values')
        self.axs[0].set_xlabel('Time')
        self.axs[0].set_ylabel('Force X (N)')

        self.axs[1].clear()
        self.axs[1].plot(self.joint1_torque_x_data, label='Joint 1 Torque X')
        self.axs[1].plot(self.joint2_torque_x_data, label='Joint 2 Torque X')
        self.axs[1].plot(self.joint3_torque_x_data, label='Joint 3 Torque X')
        self.axs[1].plot(self.joint4_torque_x_data, label='Joint 4 Torque X')
        self.axs[1].plot(self.joint5_torque_x_data, label='Joint 5 Torque X')
        self.axs[1].plot(self.joint6_torque_x_data, label='Joint 6 Torque X')
        self.axs[1].plot(self.joint7_torque_x_data, label='Joint 7 Torque X')
        self.axs[1].plot(self.joint8_torque_x_data, label='Joint 8 Torque X')
        self.axs[1].plot(self.joint9_torque_x_data, label='Joint 9 Torque X')
        self.axs[1].legend(loc='upper left', bbox_to_anchor=(1, 1))
        self.axs[1].set_title('Torque X Values')
        self.axs[1].set_xlabel('Time')
        self.axs[1].set_ylabel('Torque X (Nm)')

        self.axs[2].clear()
        self.axs[2].plot(self.position_x, label='X')
        self.axs[2].legend(loc='upper left', bbox_to_anchor=(1, 1))
        self.axs[2].set_title('Position X Values')
        self.axs[2].set_xlabel('Time')
        self.axs[2].set_ylabel('Position X')

        # Y-values

        self.axs2[0].clear()
        self.axs2[0].plot(self.joint1_force_y_data, label='Joint 1 Force Y')
        self.axs2[0].plot(self.joint2_force_y_data, label='Joint 2 Force Y')
        self.axs2[0].plot(self.joint3_force_y_data, label='Joint 3 Force Y')
        self.axs2[0].plot(self.joint4_force_y_data, label='Joint 4 Force Y')
        self.axs2[0].plot(self.joint5_force_y_data, label='Joint 5 Force Y')
        self.axs2[0].plot(self.joint6_force_y_data, label='Joint 6 Force Y')
        self.axs2[0].plot(self.joint7_force_y_data, label='Joint 7 Force Y')
        self.axs2[0].plot(self.joint8_force_y_data, label='Joint 8 Force Y')
        self.axs2[0].plot(self.joint9_force_y_data, label='Joint 9 Force Y')
        self.axs2[0].legend(loc='upper left', bbox_to_anchor=(1, 1))
        self.axs2[0].set_title('Force Y Values')
        self.axs2[0].set_xlabel('Time')
        self.axs2[0].set_ylabel('Force Y (N)')

        self.axs2[1].clear()
        self.axs2[1].plot(self.joint1_torque_y_data, label='Joint 1 Torque Y')
        self.axs2[1].plot(self.joint2_torque_y_data, label='Joint 2 Torque Y')
        self.axs2[1].plot(self.joint3_torque_y_data, label='Joint 3 Torque Y')
        self.axs2[1].plot(self.joint4_torque_y_data, label='Joint 4 Torque Y')
        self.axs2[1].plot(self.joint5_torque_y_data, label='Joint 5 Torque Y')
        self.axs2[1].plot(self.joint6_torque_y_data, label='Joint 6 Torque Y')
        self.axs2[1].plot(self.joint7_torque_y_data, label='Joint 7 Torque Y')
        self.axs2[1].plot(self.joint8_torque_y_data, label='Joint 8 Torque Y')
        self.axs2[1].plot(self.joint9_torque_y_data, label='Joint 9 Torque Y')
        self.axs2[1].legend(loc='upper left', bbox_to_anchor=(1, 1))
        self.axs2[1].set_title('Torque Y Values')
        self.axs2[1].set_xlabel('Time')
        self.axs2[1].set_ylabel('Torque Y (Nm)')

        self.axs2[2].clear()
        self.axs2[2].plot(self.position_y, label='Y')
        self.axs2[2].legend(loc='upper left', bbox_to_anchor=(1, 1))
        self.axs2[2].set_title('Position Y Values')
        self.axs2[2].set_xlabel('Time')
        self.axs2[2].set_ylabel('Position Y')

        # Z-values

        self.axs3[0].clear()
        self.axs3[0].plot(self.joint1_force_z_data, label='Joint 1 Force Z')
        self.axs3[0].plot(self.joint2_force_z_data, label='Joint 2 Force Z')
        self.axs3[0].plot(self.joint3_force_z_data, label='Joint 3 Force Z')
        self.axs3[0].plot(self.joint4_force_z_data, label='Joint 4 Force Z')
        self.axs3[0].plot(self.joint5_force_z_data, label='Joint 5 Force Z')
        self.axs3[0].plot(self.joint6_force_z_data, label='Joint 6 Force Z')
        self.axs3[0].plot(self.joint7_force_z_data, label='Joint 7 Force Z')
        self.axs3[0].plot(self.joint8_force_z_data, label='Joint 8 Force Z')
        self.axs3[0].plot(self.joint9_force_z_data, label='Joint 9 Force Z')
        self.axs3[0].legend(loc='upper left', bbox_to_anchor=(1, 1))
        self.axs3[0].set_title('Force Z Values')
        self.axs3[0].set_xlabel('Time')
        self.axs3[0].set_ylabel('Force Z (N)')

        self.axs3[1].clear()
        self.axs3[1].plot(self.joint1_torque_z_data, label='Joint 1 Torque Z')
        self.axs3[1].plot(self.joint2_torque_z_data, label='Joint 2 Torque Z')
        self.axs3[1].plot(self.joint3_torque_z_data, label='Joint 3 Torque Z')
        self.axs3[1].plot(self.joint4_torque_z_data, label='Joint 4 Torque Z')
        self.axs3[1].plot(self.joint5_torque_z_data, label='Joint 5 Torque Z')
        self.axs3[1].plot(self.joint6_torque_z_data, label='Joint 6 Torque Z')
        self.axs3[1].plot(self.joint7_torque_z_data, label='Joint 7 Torque Z')
        self.axs3[1].plot(self.joint8_torque_z_data, label='Joint 8 Torque Z')
        self.axs3[1].plot(self.joint9_torque_z_data, label='Joint 9 Torque Z')
        self.axs3[1].legend(loc='upper left', bbox_to_anchor=(1, 1))
        self.axs3[1].set_title('Torque Z Values')
        self.axs3[1].set_xlabel('Time')
        self.axs3[1].set_ylabel('Torque Z (Nm)')

        self.axs3[2].clear()
        self.axs3[2].plot(self.position_z, label='Z')
        self.axs3[2].legend(loc='upper left', bbox_to_anchor=(1, 1))
        self.axs3[2].set_title('Position Z Values')
        self.axs3[2].set_xlabel('Time')
        self.axs3[2].set_ylabel('Position Z')

        

        plt.tight_layout()
        plt.pause(0.01)


    def tf_callback(self, msg):
        for transform in msg.transforms:
            if transform.child_frame_id == 'base_link':  # Replace 'model_name' with the name of your model
                position = transform.transform.translation
                pos_x = position.x
                pos_y = position.y
                pos_z = position.z
                self.position_x.append(pos_x)
                self.position_y.append(pos_y)
                self.position_z.append(pos_z)
                #self.get_logger().info(f"Model position: x={position.x}, y={position.y}, z={position.z}")


    def joint_1_callback(self, msg):
        force_x = msg.wrench.force.x
        force_y = msg.wrench.force.y
        force_z = msg.wrench.force.z
        torque_x = msg.wrench.torque.x
        torque_y = msg.wrench.torque.y
        torque_z = msg.wrench.torque.z

        self.joint1_force_x_data.append(force_x)
        self.joint1_force_y_data.append(force_y)
        self.joint1_force_z_data.append(force_z)
        self.joint1_torque_x_data.append(torque_x)
        self.joint1_torque_y_data.append(torque_y)
        self.joint1_torque_z_data.append(torque_z)
    
    def joint_2_callback(self, msg):
        force_x = msg.wrench.force.x
        force_y = msg.wrench.force.y
        force_z = msg.wrench.force.z
        torque_x = msg.wrench.torque.x
        torque_y = msg.wrench.torque.y
        torque_z = msg.wrench.torque.z

        self.joint2_force_x_data.append(force_x)
        self.joint2_force_y_data.append(force_y)
        self.joint2_force_z_data.append(force_z)
        self.joint2_torque_x_data.append(torque_x)
        self.joint2_torque_y_data.append(torque_y)
        self.joint2_torque_z_data.append(torque_z)
    
    def joint_3_callback(self, msg):
        force_x = msg.wrench.force.x
        force_y = msg.wrench.force.y
        force_z = msg.wrench.force.z
        torque_x = msg.wrench.torque.x
        torque_y = msg.wrench.torque.y
        torque_z = msg.wrench.torque.z

        self.joint3_force_x_data.append(force_x)
        self.joint3_force_y_data.append(force_y)
        self.joint3_force_z_data.append(force_z)
        self.joint3_torque_x_data.append(torque_x)
        self.joint3_torque_y_data.append(torque_y)
        self.joint3_torque_z_data.append(torque_z)
    
    def joint_4_callback(self, msg):
        force_x = msg.wrench.force.x
        force_y = msg.wrench.force.y
        force_z = msg.wrench.force.z
        torque_x = msg.wrench.torque.x
        torque_y = msg.wrench.torque.y
        torque_z = msg.wrench.torque.z

        self.joint4_force_x_data.append(force_x)
        self.joint4_force_y_data.append(force_y)
        self.joint4_force_z_data.append(force_z)
        self.joint4_torque_x_data.append(torque_x)
        self.joint4_torque_y_data.append(torque_y)
        self.joint4_torque_z_data.append(torque_z)

    def joint_5_callback(self, msg):
        force_x = msg.wrench.force.x
        force_y = msg.wrench.force.y
        force_z = msg.wrench.force.z
        torque_x = msg.wrench.torque.x
        torque_y = msg.wrench.torque.y
        torque_z = msg.wrench.torque.z

        self.joint5_force_x_data.append(force_x)
        self.joint5_force_y_data.append(force_y)
        self.joint5_force_z_data.append(force_z)
        self.joint5_torque_x_data.append(torque_x)
        self.joint5_torque_y_data.append(torque_y)
        self.joint5_torque_z_data.append(torque_z)
    
    def joint_6_callback(self, msg):
        force_x = msg.wrench.force.x
        force_y = msg.wrench.force.y
        force_z = msg.wrench.force.z
        torque_x = msg.wrench.torque.x
        torque_y = msg.wrench.torque.y
        torque_z = msg.wrench.torque.z

        self.joint6_force_x_data.append(force_x)
        self.joint6_force_y_data.append(force_y)
        self.joint6_force_z_data.append(force_z)
        self.joint6_torque_x_data.append(torque_x)
        self.joint6_torque_y_data.append(torque_y)
        self.joint6_torque_z_data.append(torque_z)

    def joint_7_callback(self, msg):
        force_x = msg.wrench.force.x
        force_y = msg.wrench.force.y
        force_z = msg.wrench.force.z
        torque_x = msg.wrench.torque.x
        torque_y = msg.wrench.torque.y
        torque_z = msg.wrench.torque.z

        self.joint7_force_x_data.append(force_x)
        self.joint7_force_y_data.append(force_y)
        self.joint7_force_z_data.append(force_z)
        self.joint7_torque_x_data.append(torque_x)
        self.joint7_torque_y_data.append(torque_y)
        self.joint7_torque_z_data.append(torque_z)
    
    def joint_8_callback(self, msg):
        force_x = msg.wrench.force.x
        force_y = msg.wrench.force.y
        force_z = msg.wrench.force.z
        torque_x = msg.wrench.torque.x
        torque_y = msg.wrench.torque.y
        torque_z = msg.wrench.torque.z

        self.joint8_force_x_data.append(force_x)
        self.joint8_force_y_data.append(force_y)
        self.joint8_force_z_data.append(force_z)
        self.joint8_torque_x_data.append(torque_x)
        self.joint8_torque_y_data.append(torque_y)
        self.joint8_torque_z_data.append(torque_z)
    
    def joint_9_callback(self, msg):
        force_x = msg.wrench.force.x
        force_y = msg.wrench.force.y
        force_z = msg.wrench.force.z
        torque_x = msg.wrench.torque.x
        torque_y = msg.wrench.torque.y
        torque_z = msg.wrench.torque.z

        self.joint9_force_x_data.append(force_x)
        self.joint9_force_y_data.append(force_y)
        self.joint9_force_z_data.append(force_z)
        self.joint9_torque_x_data.append(torque_x)
        self.joint9_torque_y_data.append(torque_y)
        self.joint9_torque_z_data.append(torque_z)

        self.plot()
    


        



def main(args=None):
    rclpy.init(args=args)

    force_torque_visualizer = ForceTorqueVisualizer()
    rclpy.spin(force_torque_visualizer)

    force_torque_visualizer.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
