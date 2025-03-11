import launch
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='gazebo_ros',
            executable='gzserver',
            name='gazebo',
            output='screen',
            parameters=[{'use_sim_time': True}],
        ),
        Node(
            package='gazebo_ros',
            executable='spawn_entity.py',
            name='spawn_hull',
            output='screen',
            arguments=['-entity', 'hull', '-file', 'src/hull_simulation/hull_model.urdf'],
        ),
    ])
