import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node


def generate_launch_description():
    nav_pkg = get_package_share_directory('testbed_navigation')
    use_sim_time = LaunchConfiguration('use_sim_time')
    params = os.path.join(nav_pkg, 'config', 'nav2_params.yaml')

    nav_nodes = [
        ('nav2_controller', 'controller_server'),
        ('nav2_planner', 'planner_server'),
        ('nav2_behaviors', 'behavior_server'),
        ('nav2_bt_navigator', 'bt_navigator'),
        ('nav2_waypoint_follower', 'waypoint_follower'),
    ]

    actions = [DeclareLaunchArgument('use_sim_time', default_value='true')]

    for pkg, exe in nav_nodes:
        actions.append(Node(
            package=pkg,
            executable=exe,
            name=exe,
            output='screen',
            parameters=[params, {'use_sim_time': use_sim_time}],
        ))

    actions.append(Node(
        package='nav2_lifecycle_manager',
        executable='lifecycle_manager',
        name='lifecycle_manager_navigation',
        output='screen',
        parameters=[{
            'use_sim_time': use_sim_time,
            'autostart': True,
            'node_names': [exe for _, exe in nav_nodes],
        }],
    ))

    return LaunchDescription(actions)
