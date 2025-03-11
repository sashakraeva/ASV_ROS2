import launch
from launch import LaunchDescription
from launch.actions import ExecuteProcess, TimerAction
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        # Launch Ignition Gazebo using the 'ign' command
        ExecuteProcess(
            cmd=['ign', 'gazebo', '/hull_ws/src/hull_simulation/models/hull_world.sdf', '-v', '4'],
            name='ign_gazebo',
            output='screen',
        ),
        # Wait for a longer time to ensure Gazebo is fully up
        TimerAction(
            period=10.0,  # Increase the waiting period to 10 seconds
            actions=[
                Node(
                    package='ros_ign_gazebo',  # Correct package for Ignition Gazebo
                    executable='spawn_entity.py',  # Directly reference the script
                    name='spawn_entity',
                    output='screen',
                    arguments=[
                        '-entity', 'hull', 
                        '-file', '/hull_ws/src/hull_simulation/models/hull_model.urdf'  # Ensure full path is used
                    ],
                )
            ]
        ),
    ])
