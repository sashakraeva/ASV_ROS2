from launch import LaunchDescription
from launch.actions import ExecuteProcess

def generate_launch_description():
    return LaunchDescription([
        ExecuteProcess(
            cmd=['ign', 'gazebo', '/hull_ws/install/hull_simulation/share/hull_simulation/worlds/hull_world.sdf'],
            output='screen'
        )
    ])
