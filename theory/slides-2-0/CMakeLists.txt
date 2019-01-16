cmake_minimum_required(VERSION 3.3)
project(intro-to-python)

# path to custom cmake modules
list(APPEND CMAKE_MODULE_PATH "${CMAKE_CURRENT_SOURCE_DIR}/cmake")
include(remark)
include(replace-by-file-contents)

# engine definition
add_subdirectory(remark.js)

# presentation definitions
add_subdirectory("topic-1")
