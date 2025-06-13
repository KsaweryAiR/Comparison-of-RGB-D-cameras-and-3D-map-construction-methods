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

# Inicjalizacja rosdep (ignoruj błąd jeśli już zainicjowany)
RUN rosdep init || true
RUN rosdep update

# Stwórz workspace i sklonuj repozytorium
RUN mkdir -p ~/ros2_ws/src
RUN git clone https://github.com/orbbec/OrbbecSDK_ROS2.git src/OrbbecSDK_ROS2
RUN git clone https://github.com/pal-robotics/backward_ros src/backward_ros
RUN git clone https://github.com/KsaweryAiR/Comparison-of-RGB-D-cameras-and-3D-map-construction-methods.git src/start_camera


# Zainstaluj zależności systemowe i ROS pakiety
RUN apt-get update && apt-get install -y \
    libgflags-dev \
    nlohmann-json3-dev \
    libgoogle-glog-dev \
    libdw-dev \
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
    libogre-1.12-dev \
    && rm -rf /var/lib/apt/lists/*

# Zainstaluj zależności ROS z rosdep
RUN source /opt/ros/$ROS_DISTRO/setup.bash

# Zainstaluj reguły udev dla kamery Orbbec
RUN bash ./src/OrbbecSDK_ROS2/orbbec_camera/scripts/install_udev_rules.sh

# Ustaw zmienną środowiskową dla OGRE
ENV LD_LIBRARY_PATH=/opt/ros/$ROS_DISTRO/lib:${LD_LIBRARY_PATH:-}

RUN bash -c "source /opt/ros/$ROS_DISTRO/setup.bash && colcon build"

RUN echo "source /ros2_ws/install/setup.bash" >> ~/.bashrc

STOPSIGNAL SIGINT

