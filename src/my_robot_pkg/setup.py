from setuptools import find_packages, setup

package_name = 'my_robot_pkg'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='user',
    maintainer_email='user@todo.todo',
    description='TODO: Package description',
    license='Apache-2.0',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            'publisher_node = my_robot_pkg.publisher_node:main',
            'subscriber_node = my_robot_pkg.subscriber_node:main',
            'wheel_speed_publisher = my_robot_pkg.wheel_speed_publisher:main',
            'wheel_speed_subscriber = my_robot_pkg.wheel_speed_subscriber:main',
            'cmd_vel_publisher = my_robot_pkg.cmd_vel_publisher:main',
        ],
    },
)
