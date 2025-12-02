#!/bin/bash

# tells the shell to exit if any command return a non-zero 
set -e

# source ROS workspace
source /opt/ros/humble/setup.bash
source /app/onboarding_ws/install/setup.bash


# this means we are doing everythin in this script
exec "$@"