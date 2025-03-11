import launch
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='hull_simulation',
            executable='hull_control.py',
            name='hull_control',
            output='screen',
        ),
    ])
