CMAKE_MINIMUM_REQUIRED(VERSION 4.3.0)

PROJECT(cbackend)

set(CMAKE_CXX_STANDARD 20)
set(COMPILER_FLAGS
        -Wall
        -Wpedantic
        -Wextra
        -Werror
        -mssse3
        -Wno-unused-parameter
)
SET(PYBIND_FINDPYTHON ON)

FIND_PACKAGE(pybind11 CONFIG REQUIRED)
FIND_PACKAGE(yaml-cpp REQUIRED)

SET(EXE cbackend)
PYBIND11_ADD_MODULE(${EXE}
  src/cpy/number.cpp
)
TARGET_LINK_LIBRARIES(${EXE} PRIVATE
  yaml-cpp::yaml-cpp
)
TARGET_INCLUDE_DIRECTORIES(${EXE} PUBLIC
  include
  .venv/lib/python3.14/site-packages/pybind11/include
)
SET_TARGET_PROPERTIES(${EXE} PROPERTIES CMAKE_POSITION_INDEPENDENT_CODE ON)
INSTALL(TARGETS ${EXE} DESTINATION .)
