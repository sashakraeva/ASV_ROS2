# Base Image: ROS 2 Humble
ARG ROS_DISTRO=humble
FROM ros:$ROS_DISTRO-ros-base AS base

# Environment Variables
ENV LANG=C.UTF-8
ENV LC_ALL=C.UTF-8
ENV DEBIAN_FRONTEND=noninteractive
ENV TERM=xterm-256color

# Base ROS installation with essential tools
FROM base AS ros

RUN apt-get update && apt-get install -y --no-install-recommends \
    ssh \
    git \
    curl \
    wget \
    lsb-release \
    build-essential \
    cmake \
    python3-pip \
    python3-colcon-common-extensions \
    python3-rosdep \
    python3-vcstool \
    python3-pykdl \
    terminator \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# Install essential Python libraries
RUN pip3 install --no-cache-dir --upgrade pip \
    numpy \
    matplotlib \
    opencv-python \
    pyquaternion \
    python-dateutil \
    cython \
    transforms3d \
    pybullet \
    gym \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# Install ROS 2 Humble packages for simulation
RUN apt-get update && apt-get install -y --no-install-recommends \
<<<<<<< HEAD
=======
    ros-$ROS_DISTRO-rmw-cyclonedds-cpp \
>>>>>>> d22e2a4 (initial)
    ros-$ROS_DISTRO-gazebo-ros-pkgs \
    ros-$ROS_DISTRO-gazebo-ros2-control \
    ros-$ROS_DISTRO-nav2-bringup \
    ros-$ROS_DISTRO-xacro \
    ros-$ROS_DISTRO-robot-state-publisher \
    ros-$ROS_DISTRO-joint-state-publisher \
    ros-$ROS_DISTRO-joint-trajectory-controller \
    ros-$ROS_DISTRO-diagnostic-updater \
    ros-$ROS_DISTRO-image-transport-plugins \
    ros-$ROS_DISTRO-depthimage-to-laserscan \
    ros-$ROS_DISTRO-teleop-twist-keyboard \
    ros-$ROS_DISTRO-nav2-core \
    ros-$ROS_DISTRO-nav2-controller \
    ros-$ROS_DISTRO-nav2-planner \
    ros-$ROS_DISTRO-nav2-behavior-tree \
    ros-$ROS_DISTRO-slam-toolbox \
    ros-$ROS_DISTRO-ament-cmake \
    ros-$ROS_DISTRO-rviz2 \
    ros-$ROS_DISTRO-ros-gz \
<<<<<<< HEAD
    ros-$ROS_DISTRO-ros-gz-bridge \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# Install Gazebo Fortress
RUN apt-get update && apt-get install -y lsb-release wget gnupg curl && \
    sudo sh -c 'echo "deb [arch=amd64] http://packages.osrfoundation.org/gazebo/ubuntu $(lsb_release -cs) main" > /etc/apt/sources.list.d/gazebo-stable.list' && \
    curl -fsSL https://packages.osrfoundation.org/gazebo/gazebo-archive-keyring.gpg | sudo tee /usr/share/keyrings/gazebo-archive-keyring.gpg > /dev/null && \
    sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 67170598AF249743 && \
    apt-get update && \
    apt-get install -y \
    ignition-fortress \
    ros-humble-ros-gz-sim \
    && apt-get clean && rm -rf /var/lib/apt/lists/*
=======
    ros-$ROS_DISTRO-ros-gz-bridge && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# Install Gazebo Fortress
RUN apt-get update && apt-get install -y lsb-release wget gnupg curl && \
    curl -sSL https://packages.osrfoundation.org/gazebo.gpg --output /usr/share/keyrings/pkgs-osrf-archive-keyring.gpg && \
    echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/pkgs-osrf-archive-keyring.gpg] http://packages.osrfoundation.org/gazebo/ubuntu-stable $(lsb_release -cs) main" | tee /etc/apt/sources.list.d/gazebo-stable.list > /dev/null && \
    apt-get update && \
    apt-get install -y ignition-fortress ros-humble-ros-gz ros-humble-ros-gz-bridge && \
    apt-get clean && rm -rf /var/lib/apt/lists/*



>>>>>>> d22e2a4 (initial)

# Set up ROS 2 workspace
WORKDIR /
RUN mkdir -p hull_ws/src
WORKDIR /hull_ws/src

# Niceness permissions (for UR driver use without Preempt-RT)
RUN echo "* - nice -15" >> /etc/security/limits.conf

# Build workspace
FROM ros AS build

# Ensure .docker files are copied
COPY . /hull_ws/src/

WORKDIR /hull_ws

RUN ["/bin/bash", "-c", "source /opt/ros/$ROS_DISTRO/setup.bash &&\
    colcon build --symlink-install --cmake-args -DCMAKE_BUILD_TYPE=Release \
    "]

FROM build AS bash

RUN ["/bin/bash", "-c", "cp /hull_ws/src/.docker/setup.bash /hull_ws/setup.bash && chmod 777 /hull_ws/setup.bash"]
RUN ["/bin/bash", "-c", "cp /hull_ws/src/.docker/entrypoint.bash / && chmod 777 /entrypoint.bash"]
ENTRYPOINT ["bash", "/entrypoint.bash" ]

CMD ["bash"]

FROM build as dev
SHELL ["zsh", "chsh -s ~/.zshrc" ]
RUN ["/bin/bash", "-c", "cp /hull_ws/src/.docker/setup.zsh /hull_ws/setup.zsh && chmod 777 /hull_ws/setup.zsh"]
RUN ["/bin/bash", "-c", "cp /hull_ws/src/.docker/entrypoint.zsh / && chmod 777 /entrypoint.zsh"]
ENTRYPOINT ["zsh", "/entrypoint.zsh"]

