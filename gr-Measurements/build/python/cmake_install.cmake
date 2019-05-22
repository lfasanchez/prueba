# Install script for directory: /home/user/workarea-gnuradio/gr-Measurements/python

# Set the install prefix
if(NOT DEFINED CMAKE_INSTALL_PREFIX)
  set(CMAKE_INSTALL_PREFIX "/home/user/prefix")
endif()
string(REGEX REPLACE "/$" "" CMAKE_INSTALL_PREFIX "${CMAKE_INSTALL_PREFIX}")

# Set the install configuration name.
if(NOT DEFINED CMAKE_INSTALL_CONFIG_NAME)
  if(BUILD_TYPE)
    string(REGEX REPLACE "^[^A-Za-z0-9_]+" ""
           CMAKE_INSTALL_CONFIG_NAME "${BUILD_TYPE}")
  else()
    set(CMAKE_INSTALL_CONFIG_NAME "Release")
  endif()
  message(STATUS "Install configuration: \"${CMAKE_INSTALL_CONFIG_NAME}\"")
endif()

# Set the component getting installed.
if(NOT CMAKE_INSTALL_COMPONENT)
  if(COMPONENT)
    message(STATUS "Install component: \"${COMPONENT}\"")
    set(CMAKE_INSTALL_COMPONENT "${COMPONENT}")
  else()
    set(CMAKE_INSTALL_COMPONENT)
  endif()
endif()

# Install shared libraries without execute permission?
if(NOT DEFINED CMAKE_INSTALL_SO_NO_EXE)
  set(CMAKE_INSTALL_SO_NO_EXE "1")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/python2.7/dist-packages/Measurements" TYPE FILE FILES
    "/home/user/workarea-gnuradio/gr-Measurements/python/__init__.py"
    "/home/user/workarea-gnuradio/gr-Measurements/python/Amp_Dist_Zero_py_cf.py"
    "/home/user/workarea-gnuradio/gr-Measurements/python/wmoving.py"
    "/home/user/workarea-gnuradio/gr-Measurements/python/Std_Dev_Stream_ff.py"
    "/home/user/workarea-gnuradio/gr-Measurements/python/Std_Dev_PMT.py"
    )
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/python2.7/dist-packages/Measurements" TYPE FILE FILES
    "/home/user/workarea-gnuradio/gr-Measurements/build/python/__init__.pyc"
    "/home/user/workarea-gnuradio/gr-Measurements/build/python/Amp_Dist_Zero_py_cf.pyc"
    "/home/user/workarea-gnuradio/gr-Measurements/build/python/wmoving.pyc"
    "/home/user/workarea-gnuradio/gr-Measurements/build/python/Std_Dev_Stream_ff.pyc"
    "/home/user/workarea-gnuradio/gr-Measurements/build/python/Std_Dev_PMT.pyc"
    "/home/user/workarea-gnuradio/gr-Measurements/build/python/__init__.pyo"
    "/home/user/workarea-gnuradio/gr-Measurements/build/python/Amp_Dist_Zero_py_cf.pyo"
    "/home/user/workarea-gnuradio/gr-Measurements/build/python/wmoving.pyo"
    "/home/user/workarea-gnuradio/gr-Measurements/build/python/Std_Dev_Stream_ff.pyo"
    "/home/user/workarea-gnuradio/gr-Measurements/build/python/Std_Dev_PMT.pyo"
    )
endif()

