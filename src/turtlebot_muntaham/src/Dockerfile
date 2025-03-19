
FROM ros:noetic


RUN apt-get update && apt-get install -y \
    python3-pip \
    python3-dev \
    portaudio19-dev \
    python3-pyaudio \
RUN ros-noetic-rospy 
RUN ros-noetic-geometry-msgs 
RUN    ros-noetic-std-msgs \
    && rm -rf /var/lib/apt/lists/*

    
RUN pip3 install speechrecognition
RUN pip3 install sounddevice
RUN apt-get install -y ros-noetic-rospy
RUN pip3 install pyttsx3 
COPY control.py /control.py
COPY speaker.py /speaker.py



RUN chmod +x /control.py
RUN chmod +x /speaker.py
    

ENTRYPOINT ["/bin/bash", "-c", "source /opt/ros/noetic/setup.bash && roscore & sleep 5 && python3 /control.py & python3 /speaker.py"]