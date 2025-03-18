cmake_minimum_required(VERSION 3.5)
project(hull_simulation)

find_package(ament_cmake REQUIRED)
find_package(rclpy REQUIRED)
find_package(gazebo_ros REQUIRED)

install(DIRECTORY launch worlds
  DESTINATION share/${PROJECT_NAME}
)

ament_package()
