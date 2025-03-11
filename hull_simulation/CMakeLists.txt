cmake_minimum_required(VERSION 3.5)
project(hull_simulation)

find_package(ament_cmake REQUIRED)
find_package(rclpy REQUIRED)
find_package(gazebo_ros REQUIRED)

install(DIRECTORY launch models worlds
  DESTINATION share/${PROJECT_NAME}
)

install(PROGRAMS
  scripts/hull_control.py
  DESTINATION lib/${PROJECT_NAME}
)

ament_package()
