#!/usr/bin/env python3

import rospy
import speech_recognition as sr
import sounddevice

from std_msgs.msg import String

import pyttsx3

class Node():
    def __init__(self):
        rospy.init_node("pagol_pub", anonymous=True)
        self.pub = rospy.Publisher("speaker", String, queue_size=10)
        self.engine = pyttsx3.init()
        self.recognizer = sr.Recognizer()
        self.listener()

    def listener(self):
        with sr.Microphone() as source:
            rospy.loginfo("Adjusting for ambient noise...")
            self.recognizer.adjust_for_ambient_noise(source, duration=2)
            rospy.loginfo("Listening for command...")
            while not rospy.is_shutdown():  
                    
                
                    audio = self.recognizer.listen(source)
                    rospy.loginfo("Processing command...")
                    command = self.recognizer.recognize_google(audio)
                    rospy.loginfo(f"Command received: {command}")
                    self.pub.publish(command)  
              
if __name__ == "__main__":

    
    node = Node()
  
