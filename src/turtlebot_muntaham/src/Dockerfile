
FROM ros:noetic

RUN apt-get update && apt-get install -y \
    python3-pip \
    python3-dev \
    portaudio19-dev \
    python3-pyaudio \
    ros-noetic-rospy \
    ros-noetic-geometry-msgs \
    espeak\
    alsa-utils \
    pulseaudio \
    ros-noetic-std-msgs

    
RUN pip3 install speechrecognition
RUN pip3 install sounddevice
RUN apt-get install -y ros-noetic-rospy
RUN pip3 install pyttsx3 
ENV PULSE_SERVER=unix:/run/user/1000/pulse/native
RUN usermod -a -G audio root
COPY control.py /control.py
COPY speaker.py /speaker.py



RUN chmod +x /control.py
RUN chmod +x /speaker.py
    
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]

