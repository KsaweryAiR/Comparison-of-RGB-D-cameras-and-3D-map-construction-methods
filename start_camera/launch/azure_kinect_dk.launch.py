from launch import LaunchDescription
from launch.actions import ExecuteProcess
from launch_ros.actions import Node

def generate_launch_description():
    ld = LaunchDescription()

    # Uruchomienie launch pliku kamery Orbbec (przez ExecuteProcess)
    orbec_camera_launch = ExecuteProcess(
        cmd=[
            'ros2', 'launch', 'azure_kinect_ros_driver', 'driver.launch.py',
            'fps:=30',
            'depth_mode:=NFOV_UNBINNED',
        ],
        output='screen'
    )

    # Uruchomienie ros2 bag record --all
    rosbag_record = ExecuteProcess(
        cmd=['ros2', 'bag', 'record', '--all', '-o', 'azure_kinect_dk_bag'],
        output='screen'
    )

    # Dodanie obu procesów do launch description
    ld.add_action(orbec_camera_launch)
    ld.add_action(rosbag_record)

    return ld
