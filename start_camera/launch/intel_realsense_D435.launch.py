from launch import LaunchDescription
from launch.actions import ExecuteProcess
from launch_ros.actions import Node

def generate_launch_description():
    ld = LaunchDescription()

    # Uruchomienie launch pliku kamery Orbbec (przez ExecuteProcess)
    orbec_camera_launch = ExecuteProcess(
        cmd=[
            'ros2', 'launch', 'realsense2_camera', 'rs_launch.py',
            'pointcloud.enable:=true',
        ],
        output='screen'
    )

    # Uruchomienie ros2 bag record --all
    rosbag_record = ExecuteProcess(
        cmd=['ros2', 'bag', 'record', '--all', '-o', 'realsense_D435_bag'],
        output='screen'
    )

    # Dodanie obu procesów do launch description
    ld.add_action(orbec_camera_launch)
    ld.add_action(rosbag_record)

    return ld
