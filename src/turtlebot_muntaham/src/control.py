#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist
from std_msgs.msg import String

class Node():
    def __init__(self):
        rospy.init_node("middle",anonymous=True)
        self.pub=rospy.Publisher("cmd_vel",Twist,queue_size=10)
        rospy.Subscriber("speaker",String,self.clbk)
        self.rate=rospy.Rate(1)
        self.energy=100
    def clbk(self,msg):
        command=msg.data.split()
        
        if(command[0].lower()=="forward"):
            if(len(command)>1):
                    
                self.energy-=10
                rospy.loginfo(f"command={command[0]} and remaining energy {self.energy}")
                start_time=rospy.get_time()
                m=Twist()
                while rospy.get_time() - start_time < float(command[1]) :
                        
                    
                    m.linear.x=0.2
                    m.linear.y=0
                    m.linear.z=0
                    m.angular.x=0
                    m.angular.z=0
                    m.angular.y=0
                    self.pub.publish(m)
                    self.rate.sleep()
                m.linear.x = 0.0
                self.pub.publish(m)
            else: 
                                    
                self.energy-=10
                rospy.loginfo(f"command={command[0]} and remaining energy {self.energy}")
                start_time=rospy.get_time()
                m=Twist()
                while rospy.get_time() - start_time < 2 :
                        
                    
                    m.linear.x=0.2
                    m.linear.y=0
                    m.linear.z=0
                    m.angular.x=0
                    m.angular.z=0
                    m.angular.y=0
                    self.pub.publish(m)
                    self.rate.sleep()
                m.linear.x = 0.0
                self.pub.publish(m)
                

        
        if(command[0].lower()=="backward"):
            if(len(command)>1):
                    
                self.energy-=10
                rospy.loginfo(f"command={command[0]} and remaining energy {self.energy}")
                start_time=rospy.get_time()
                m=Twist()
                while rospy.get_time() - start_time < float(command[1]) :
                        
                    
                    m.linear.x=-0.2
                    m.linear.y=0
                    m.linear.z=0
                    m.angular.x=0
                    m.angular.z=0
                    m.angular.y=0
                    self.pub.publish(m)
                    self.rate.sleep()
                m.linear.x = 0.0
                self.pub.publish(m)
            else: 
                                    
                self.energy-=10
                rospy.loginfo(f"command={command[0]} and remaining energy {self.energy}")
                start_time=rospy.get_time()
                m=Twist()
                while rospy.get_time() - start_time < 2 :
                        
                    
                    m.linear.x=-0.2
                    m.linear.y=0
                    m.linear.z=0
                    m.angular.x=0
                    m.angular.z=0
                    m.angular.y=0
                    self.pub.publish(m)
                    self.rate.sleep()
                m.linear.x = 0.0
                self.pub.publish(m)



        if(command[0].lower()=="right"):
            if(len(command)>1):
                    
                self.energy-=10
                rospy.loginfo(f"command={command[0]} and remaining energy {self.energy}")
                start_time=rospy.get_time()
                m=Twist()
                while rospy.get_time() - start_time < float(command[1]) :
                        
                    
                    m.linear.x=0
                    m.linear.y=0
                    m.linear.z=0
                    m.angular.x=0
                    m.angular.z=0.2
                    m.angular.y=0
                    self.pub.publish(m)
                    self.rate.sleep()
                m.linear.x = 0.0
                self.pub.publish(m)
            else: 
                                    
                self.energy-=10
                rospy.loginfo(f"command={command[0]} and remaining energy {self.energy}")
                start_time=rospy.get_time()
                m=Twist()
                while rospy.get_time() - start_time < 2 :
                        
                    
                    m.linear.x=0.2
                    m.linear.y=0
                    m.linear.z=0
                    m.angular.x=0
                    m.angular.z=0
                    m.angular.y=0
                    self.pub.publish(m)
                    self.rate.sleep()
                m.linear.x = 0.0
                self.pub.publish(m)











        if(command[0].lower()=="left"):
            if(len(command)>1):
                self.energy-=10
                rospy.loginfo(f"command={command[0]} and remaining energy {self.energy}")
                start_time=rospy.get_time()
                m=Twist()
                duration = float(command[1])  
                while rospy.get_time() - start_time < duration:
                    if rospy.is_shutdown():  
                        break
                    m.linear.x = 0
                    m.linear.y = 0
                    m.linear.z = 0
                    m.angular.x = 0
                    m.angular.z = -0.2 
                    m.angular.y = 0
                    self.pub.publish(m)
                    self.rate.sleep()
                m.linear.x = 0.0
                self.pub.publish(m)
            else:
               
                self.energy -= 10
                rospy.loginfo(f"command={command[0]} and remaining energy {self.energy}")
                start_time = rospy.get_time()
                m = Twist()
                while rospy.get_time() - start_time < 2:
                    m.linear.x = 0
                    m.linear.y = 0
                    m.linear.z = 0
                    m.angular.x = 0
                    m.angular.z = -0.2  
                    m.angular.y = 0
                    self.pub.publish(m)
                    self.rate.sleep()
                m.linear.x = 0.0
                self.pub.publish(m)


        if(command[0].lower()=="kaboom"):
            self.energy+=10
            rospy.loginfo("energy increased")





if __name__=="__main__":
    n=Node()
    rospy.spin()

    
