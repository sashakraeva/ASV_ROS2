# ASV_ROS2

### This repository is a property of IAAC Engineering Club.

## Explanation
The project aims to create a digital twin of ASV using ROS2 Humble and Gazebo Fortress.

Currently we are testing our project on tutorial from [Gazebo Fortress](https://gazebosim.org/docs/fortress/tutorials/) 

P.s. These tutorials are not for Hull, but for robots and gazebo in gneral

P.s. For now our "FUTURE HULL" looks a bit silly (check the image below)

The tutorials made so far:
- [Building your own robot](https://gazebosim.org/docs/fortress/building_robot/)
- [Moving the robot](https://gazebosim.org/docs/fortress/moving_robot/)

Current result looks like this:
![alt text](/images/image.png)


## Requirements

1. Computer running **Linux Ubuntu 22.04 (jammy)**
2. Docker 
    - [install](https://docs.docker.com/engine/install/ubuntu/) 
    - [postinstall](https://docs.docker.com/engine/install/linux-postinstall/)


## Running the project

### 1. Fork this repository https://github.com/sashakraeva/ASV_ROS2.git

### 2. Navigate to desired directory on your machine where you want to clone your repository

``` bash
cd path/to/folder
```

### 3. Clone the repository using your SHH key 

``` bash
git clone your/shh/link/ASV_ROS2.git
```

!!! If you dont have SHH key, follow tutorial [Generating a new SSH key and adding it to the ssh-agent](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent)

### 4. Navigate to repo and build Docker Image

This docker image contains ROS2 Humble, Gazebo Fortress and other required libraries

``` bash
cd ~/ASV_ROS2
.docker/build_image.sh
```

### 5. Run the image 

``` bash
cd ~/ASV_ROS2
.docker/run_image.sh
```

it will ask you to do following to own the workspace:

``` bash
sudo chown -R $USER /hull_ws
```

!!! From now on you will be working only in terminator, so run

``` bash
terminator
```

Hide the normal terminal, BUT DONT CLOSE IT.


### 6. Open container in VS code

1. Open VS code
2. if not installed, install docker extension for VS Code in Extension (Ctrl+Shift+X)
3. Do to Docker extension, right click on the running image *"Attach Visual Studio Code"*
4. File -> Open Folder -> type: **/hull_ws/src**
5. Now you are working inside your working space

### 7. Folder structure explanation:

We are currently working only in hull_simulation/ folder (is is a ros package)


*hull_simulation/*:

+ launch/ - package launching files (ros2 launch .....)
+ worlds/ - .sdf world files that we see in Gazebo.
    - currently we are working with building_robot.sdf (Gazebo Fortress tutorial)
    - building_robot.sdf contains:
        - world setting
        - model (robot) setting with links between the wheels and physics
        - plugins for model to make it move using keypad

### 8. Run Gazebo without ROS

To run only gazebo with our building_robot.sdf file we can do following:

1. This starts the simulation

``` bash
cd ~/hull_ws
ign gazebo building_robot.sdf
```

2. This Activates the keypad and movement

- Inside Gazebo click on the right top corner three dots and type Key Publisher
- Press play in left down corner
- Press arrow on your keypad 

This will make our robot move


### 9. Run Gazebo with ROS

To do so, we fisrt need to build our hull_simulation package
!!! Every time you change smth inside the codes on hull_simulation/ you need to do following steps:

1. Building hull_simulation package

``` bash
cd /hull_ws
colcon build --symlink-install
source install/setup.bash
```

2. Run the simulation

``` bash
ros2 launch hull_simulation simulation_launch.py
```

- Inside Gazebo click on the right top corner three dots and type Key Publisher
- Press play in left down corner
- Press up arrow on your keypad 

This will make our robot move


### OTHER FILES

### 01_With_Sensors (IMU, Contact, LiDAR)

sensor_tutorial.sdf
/hull_ws/src/hull_simulation/worlds/sensor_tutorial.sdf

1) In first terminal:

``` bash
ign gazebo sensor_tutorial.sdf
```
2) Check IMU sensor values

In second terminal:

``` bash
ign topic -e -t /imu
```

Inside gazebo window:

```
- Klick on the right top corner three dots and type Key Publisher
- Press play in left down corner
- Press arrow on your keypad 
- check second terminal values
```

In second terminal you will recieve values like: 

``` 
header {
  stamp {
    sec: 36
  }
  data {
    key: "frame_id"
    value: "vehicle_blue::chassis::imu_sensor"
  }
  data {
    key: "seq"
    value: "36"
  }
}
entity_name: "vehicle_blue::chassis::imu_sensor"
orientation {
  x: 7.9718030854165078e-07
  y: 8.39381347583856e-07
  z: 8.6009772919773909e-13
  w: 0.99999999999933
}
```

3) Check Contact sensor values

In second terminal:

``` bash
ign topic -e -t /wall/touched
```

Inside gazebo window:

```
- Klick on the right top corner three dots and type Key Publisher
- Press play in left down corner
- Press arrow on your keypad 
- try to crash into the wall
- check second terminal values
```

In second terminal you will recieve values like: 

```
"data: true" - meaning that you heated the wall
```



## Trubleshooting

### Path problems

you may need to add some paths to: 

``` bash
code ~/.bashrc
``` 

### To clean the docker images u dont use

```bash
docker system prune
```







