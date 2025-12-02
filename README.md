# Simple ROS2 Sensor Simulator Node in Docker

A ROS2 node that simulates a basic sensor by publishing sensor data (e.g., distance or velocity)


#### To Create and Run Ros2 Package in Docker container step by step
##Step o - Prerequisite

Step o - Install( Ubuntu 22.04, Ros2 Humble(or anyother distrobution) and Docker Engine)
- You need to have Ubuntu 22.04, Ros2 Humble and docker engine installed
- Install Ubuntu either wsl on your windows, desktop or server. [link](https://ubuntu.com/download)
- Install docker using the [instruction](https://docs.docker.com/engine/install/ubuntu/#install-using-the-repository) or execute below commands. NOTE: skip this step, If you already have docker installed.

```bash
   # Add Docker's official GPG key:
sudo apt-get update
sudo apt-get install ca-certificates curl gnupg
sudo install -m 0755 -d /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
sudo chmod a+r /etc/apt/keyrings/docker.gpg

# Add the repository to Apt sources:
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu \
  $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
  
sudo apt-get update

# Install the Docker packages.
sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
   ```


Step 1 - Create Source Files of the Nodes nad Packages:
First , source (access) the environment

```bash
   source /opt/ros/humble/setup.bash
   ```

Step 2 - Create our workspace folder and the package containing the nodes
Second,  create the folders from the home directory that will contain the publishers and scripers file and the python or C++ packages setup for building

```bash
   mkdir /onboarding_ws/src
   ```
   This command will create a folder called onboarding_ws and a subfolder called src

Step 3 - Create the package (py or c++)
third, To create the package we need to navigate into the src folder

```bash
   cd /onboarding_ws/src
   ```

   To create the package , we type the command below in the case I am using python paackage, you can replace the python with cpp then follows the package name of youe choice:
   ```bash
   ros2 pkg create --build-type ament_python my_ros_pkg
   ros2 pkg create --build-type ament_cpp my_ros_pkg
   ```

Step 4 - Now inside your package folder create the Publisher and suscriper nodes files
fourth, open a .py files for the various nodes you want to run from the code editor (e.g Vscode) from the terminal

```bash
   code .
   ```

Step 5 - Add your nodes and update the dependencies and entrypoint setup  from the package files

Step 6 - Check if all the depencies are met if not add dependencies to the package.eml file and the setup.py file

```bash
   cd /onboarding_ws/
   rosdep install -i --from-path src --rosdistro humble -y
   ```

## To create Docker File and Entrypoint File

```bash
   cd /onboarding_ws/docker
   ```
   - cretae the docker file "Dockerfile"
   -  create the entrypoint file

Step 7 - write the docker and enrypoint contents

Step 8 - Build the Docker Image and Run the Docker container

```bash
   docker build -f docker/Dockerfile . -t my_ros2_image
   ```

Step 9 - Create and run the container

```bash
   docker run -it --rm my_ros2_image:latest
   ```
   - Navigate into your project folder
   return to the root folder
```bash
   cd /onboarding_ws
   cd /
```

Step 10 - We run the Publisher or Subscriber node()
Finally, run the nodes with the command below ( ros2 run, package name and node name) in my case i used "my_ros2_pkg as the package and publisher as the name, adjust accordingly.
```bash
   ros2 run my_ros2_pkg talker
   ros2 run my_ros2_pkg listener
   ```

