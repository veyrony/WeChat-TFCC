cmake_minimum_required(VERSION 3.14)
project(tfcc_runtime_example)

# c++11
set(CMAKE_CXX_STANDARD 11)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS OFF)

find_package(tfcc_runtime)

if(tfcc_runtime_FOUND)
    message("tfcc_runtime FOUND")
else(tfcc_runtime_FOUND)
    message(FATAL_ERROR "tfcc_runtime not found")
endif(tfcc_runtime_FOUND)


find_package(tfcc)
if(tfcc_FOUND)
    message("tfcc FOUND")
else(tfcc_FOUND)
    message(FATAL_ERROR "tfcc not found")
endif(tfcc_FOUND)


add_executable(tfcc_runtime_example run_model.cpp)
target_link_libraries(tfcc_runtime_example tfcc_runtime)

add_executable(demo0 demo0.cpp)
target_link_libraries(demo0 tfcc_runtime)
add_executable(demo1 demo1.cpp)
target_link_libraries(demo1 tfcc_runtime)
