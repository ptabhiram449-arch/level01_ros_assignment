cmake_minimum_required(VERSION 3.8)
project(testbed_gazebo)

find_package(ament_cmake REQUIRED)
find_package(rclpy REQUIRED)
find_package(testbed_description REQUIRED)

install(DIRECTORY launch worlds models
  DESTINATION share/${PROJECT_NAME}/
)

ament_package()
