cmake_minimum_required(VERSION 3.5)
project(hull_simulation)

# Find dependencies
find_package(ament_cmake REQUIRED)
find_package(rclcpp REQUIRED)
find_package(std_msgs REQUIRED)
find_package(gazebo_ros REQUIRED)

# Install Python scripts
install(PROGRAMS
  scripts/hull_control.py
  DESTINATION lib/${PROJECT_NAME}
)

# Install launch files
install(DIRECTORY launch
  DESTINATION share/${PROJECT_NAME}/launch
)

# Install models
install(DIRECTORY models
  DESTINATION share/${PROJECT_NAME}/models
)

ament_package()
