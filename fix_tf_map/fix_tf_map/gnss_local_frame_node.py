#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import PoseWithCovarianceStamped, TransformStamped
from sensor_msgs.msg import PointCloud2
from tf2_ros import TransformBroadcaster

class GNSSLocalFrameNode(Node):
    def __init__(self):
        super().__init__('gnss_local_frame_node')

        # Subskrypcja GNSS
        self.subscription = self.create_subscription(
            PoseWithCovarianceStamped,
            '/sensing/gnss/gnss_transforms/rover_pose_cov',
            self.gnss_callback,
            10
        )

        # Subskrypcja PointCloud2 (kamera)
        self.pc_subscription = self.create_subscription(
            PointCloud2,
            '/camera/camera/depth/color/points',
            self.pc_callback,
            10
        )

        self.br = TransformBroadcaster(self)
        self.initialized = False
        self.origin_position = None
        self.origin_orientation = None

     
        self.latest_pc_stamp = None

    def pc_callback(self, msg: PointCloud2):
        #Mój zegarek z chmury
        self.latest_pc_stamp = msg.header.stamp

    def gnss_callback(self, msg: PoseWithCovarianceStamped):
        if self.latest_pc_stamp is None:
            self.get_logger().warn("Brak czasu z PointCloud2, transformacja nie zostanie opublikowana.")
            return

        current_pos = msg.pose.pose.position
        current_ori = msg.pose.pose.orientation

        if not self.initialized:
            self.origin_position = current_pos
            self.origin_orientation = current_ori
            self.initialized = True
            self.get_logger().info("Zainicjowano lokalny układ współrzędnych.")
            return

        dx = current_pos.x - self.origin_position.x
        dy = current_pos.y - self.origin_position.y

        t = TransformStamped()
 
        t.header.stamp = self.latest_pc_stamp  
        t.header.frame_id = 'map'
        t.child_frame_id = 'camera_link'

        t.transform.translation.x = dx
        t.transform.translation.y = dy
        t.transform.translation.z = 1.0
        t.transform.rotation = current_ori

        self.br.sendTransform(t)

def main(args=None):
    rclpy.init(args=args)
    node = GNSSLocalFrameNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
