ARG ROS_DISTRO=humble
ARG PREFIX=

FROM ros:humble-ros-core-jammy

SHELL ["/bin/bash", "-c"]

WORKDIR /ros2_ws

# Zainstaluj podstawowe narzędzia, git i rosdep
RUN apt-get update && apt-get install -y \
    git \
    python3-rosdep \
    python3-pip \
    python3-colcon-common-extensions \
    && rm -rf /var/lib/apt/lists/*
    
RUN pip3 install xacro

# Inicjalizacja rosdep (ignoruj błąd jeśli już zainicjowany)
RUN rosdep init || true
RUN rosdep update

# Stwórz workspace i sklonuj repozytorium
RUN mkdir -p ~/ros2_ws/src
RUN git clone https://github.com/juancarlosmiranda/azure_kinect_notes.git && cd azure_kinect_notes && chmod 755 install_azure_kinect_camera_u_22.04.sh

RUN git clone https://github.com/pal-robotics/backward_ros src/backward_ros
RUN git clone https://github.com/microsoft/Azure_Kinect_ROS_Driver.git -b humble src/Azure_Kinect_ROS_Driver
RUN git clone https://github.com/KsaweryAiR/Comparison-of-RGB-D-cameras-and-3D-map-construction-methods.git src/start_camera



# Zainstaluj zależności systemowe i ROS pakiety
RUN apt-get update && apt-get install -y \
    libgflags-dev \
    nlohmann-json3-dev \
    libgoogle-glog-dev \
    libdw-dev \
    wget \
    ros-$ROS_DISTRO-image-transport \
    ros-$ROS_DISTRO-image-publisher \
    ros-$ROS_DISTRO-camera-info-manager \
    ros-$ROS_DISTRO-rviz2 \
    ros-$ROS_DISTRO-ros2bag* \
    ros-$ROS_DISTRO-rosbag2* \
    ros-$ROS_DISTRO-rosbag2-storage-default-plugins \
    ros-$ROS_DISTRO-tf2-eigen \
    ros-$ROS_DISTRO-tf2-sensor-msgs \
    ros-$ROS_DISTRO-diagnostic-updater \
    ros-$ROS_DISTRO-joint-state-publisher \
    ros-$ROS_DISTRO-angles \
    ros-$ROS_DISTRO-robot-state-publisher \
    libogre-1.12-dev \
    && rm -rf /var/lib/apt/lists/*
    
RUN mkdir -p /etc/udev/rules.d/
RUN bash -c "cp azure_kinect_notes/99-k4a.rules /etc/udev/rules.d/99-k4a.rules"

# Automatyczna zgoda na licencję – zamień "read" na odpowiedź yes
# RUN echo ./azure_kinect_notes/install_azure_kinect_camera_u_22.04.sh

# Zainstaluj zależności ROS z rosdep
RUN source /opt/ros/$ROS_DISTRO/setup.bash

# Ustaw zmienną środowiskową dla OGRE
#ENV LD_LIBRARY_PATH=/opt/ros/$ROS_DISTRO/lib:${LD_LIBRARY_PATH:-}

#RUN bash -c "source /opt/ros/$ROS_DISTRO/setup.bash && colcon build"

#RUN echo "source /ros2_ws/install/setup.bash" >> ~/.bashrc

STOPSIGNAL SIGINT

