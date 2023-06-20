import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration
from launch.substitutions import ThisLaunchFileDir
from launch_ros.actions import Node

def generate_launch_description():
    # jetson_port = LaunchConfiguration('jetson_port', default='/dev/ttyUSB0')

    return LaunchDescription([
        # DeclareLaunchArgument(
        #     'jetson_port',
        #     default_value = jetson_port,
        #     description = 'Serial port for communication w microcontroller'
        # ),
        Node(
            package='robot-bring-up-dev',
            executable='odom.py',
            parameters=[],
            arguments=[],
            output='screen'
        ),
    ])
