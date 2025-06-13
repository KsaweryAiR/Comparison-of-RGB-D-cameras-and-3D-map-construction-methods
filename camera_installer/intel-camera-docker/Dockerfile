ARG ROS_DISTRO=humble

FROM ros:${ROS_DISTRO}-ros-core-jammy

SHELL ["/bin/bash", "-c"]

# Podstawowe narzędzia i ROS
RUN apt-get update && apt-get install -y \
    git \
    curl \
    wget \
    gnupg2 \
    lsb-release \
    python3-rosdep \
    python3-pip \
    python3-colcon-common-extensions \
    software-properties-common \
    apt-transport-https \
    && rm -rf /var/lib/apt/lists/*

# Inicjalizacja rosdep
RUN rosdep init || true && rosdep update

# Dodaj repozytorium librealsense
RUN mkdir -p /etc/apt/keyrings && \
    curl -sSf https://librealsense.intel.com/Debian/librealsense.pgp | tee /etc/apt/keyrings/librealsense.pgp > /dev/null && \
    echo "deb [signed-by=/etc/apt/keyrings/librealsense.pgp] https://librealsense.intel.com/Debian/apt-repo $(lsb_release -cs) main" | \
    tee /etc/apt/sources.list.d/librealsense.list

# Instalacja librealsense2 z .deb
RUN apt-get update && apt-get install -y \
    librealsense2-dev \
    librealsense2-dbg \
    v4l-utils \
    && rm -rf /var/lib/apt/lists/*
    
RUN apt-get update && apt-get install -y \
    libboost-python-dev \ 
    ros-humble-cv-bridge \
    && rm -rf /var/lib/apt/lists/*
   
RUN apt-get update && apt-get install -y \
    ros-humble-image-transport \
    libeigen3-dev \
    ros-humble-rviz2 \
    ros-humble-tf2-ros \
    ros-humble-ros2bag* \
    ros-humble-rosbag2* \
    ros-humble-rosbag2-storage-default-plugins \
    && rm -rf /var/lib/apt/lists/*
    
RUN apt-get update && apt-get install -y \
    ros-humble-diagnostic-updater \
    && rm -rf /var/lib/apt/lists/*

# Utwórz workspace ROS2 i klonuj realsense-ros
WORKDIR /ros2_ws
RUN mkdir -p src
RUN git clone https://github.com/IntelRealSense/realsense-ros.git -b ros2-master src/realsense-ros
RUN git clone https://github.com/KsaweryAiR/Comparison-of-RGB-D-cameras-and-3D-map-construction-methods.git src/start_camera

WORKDIR /ros2_ws
RUN apt-get update && apt-get install -y python3-rosdep
RUN rosdep init || true
RUN rosdep update
RUN rosdep install -i --from-path src --rosdistro $ROS_DISTRO --skip-keys=librealsense2 -y

RUN bash -c "source /opt/ros/$ROS_DISTRO/setup.bash && colcon build"

RUN echo "source /opt/ros/humble/setup.bash" >> /root/.bashrc

RUN echo "source /ros2_ws/install/local_setup.bash" >> /root/.bashrc

STOPSIGNAL SIGINT

