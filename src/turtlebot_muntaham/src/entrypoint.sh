#!/bin/bash
source /opt/ros/noetic/setup.bash
roscore & sleep 5
python3 /control.py &
python3 /speaker.py
exec "$@"
