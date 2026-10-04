cmake_minimum_required(VERSION 3.8)
project(testbed_bringup)

find_package(ament_cmake REQUIRED)
find_package(rclpy REQUIRED)

install(DIRECTORY launch maps
  DESTINATION share/${PROJECT_NAME}/
)

ament_package()
