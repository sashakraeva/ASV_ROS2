import os
from launch import LaunchDescription
from launch.actions import ExecuteProcess

def generate_launch_description():
    return LaunchDescription([
        ExecuteProcess(
            cmd=["ros2", "run", "teleop_twist_keyboard", "teleop_twist_keyboard"],
            output="screen"
        )
    ])
