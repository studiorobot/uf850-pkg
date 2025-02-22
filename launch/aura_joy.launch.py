#!/usr/bin/env python3

import os
import sys
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    # Add the package's src directory to PYTHONPATH
    package_share_directory = os.path.join(
        os.getenv('COLCON_PREFIX_PATH', '/opt/ros/galactic'),
        'share/joy2uf850'
    )
    src_directory = os.path.join(package_share_directory, '../src/joy2uf850')
    sys.path.append(src_directory)

    # Define nodes
    aura_joy_node = Node(
        package='joy2uf850',
        executable='aura_joy',
        output='screen',
        name='aura_joy',
    )

    joy_node = Node(
        package='joy',
        executable='joy_node',
        name='joy_node',
        output='screen',
        parameters=[{
            'autorepeat_rate': 25.0,
            'deadzone': 0.1
            }],
    )

    return LaunchDescription([
        joy_node,
        aura_joy_node,
    ])