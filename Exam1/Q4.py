import numpy as np
import math

d1=float(input("Enter the value of d1: ")) #offsets 
d4=float(input("Enter the value of d4: "))
d5=float(input("Enter the value of d5: "))
d6=float(input("Enter the value of d6: "))

a2=float(input("Enter the value of a2: ")) #link lengths
a3=float(input("Enter the value of a3: ")) #link lengths


q1=float(input("Enter the value of q1: ")) #joint angles
q2=float(input("Enter the value of q2: ")) #joint angles
q3=float(input("Enter the value of q3: ")) #joint angles
q4=float(input("Enter the value of q4: ")) #joint angles
q5=float(input("Enter the value of q5: ")) #joint angles
q6=float(input("Enter the value of q6: ")) #joint angles

#Writing the Jacbian Matrix

J11=-(a3*math.sin(q1)*math.sin(q2)*math.sin(q3))-(a3*math.cos(q1)*math.cos(q3)*math.sin(q2))-(a2*math.cos(q1)*math.sin(q2))
J12=-(a3*math.cos(q1)*math.sin(q2)*math.sin(q3))+(a3*math.cos(q3)*math.sin(q1)*math.sin(q2))+(a2*math.sin(q1)*math.sin(q2))
J13=-(a3*math.cos(q2)*math.sin(q3))-(a2*math.cos(q2))
J14=0
J15=0
J16=0
J21=(a3*math.cos(q1)*math.cos(q2)*math.sin(q3))-(a3*math.cos(q1)*math.cos(q2)*math.cos(q3))-(a2*math.cos(q1)*math.cos(q2))
J22=(a3*math.sin(q1)*math.sin(q2)*math.sin(q3))-(a3*math.cos(q3)*math.sin(q1)*math.sin(q2))-(a2*math.sin(q1)*math.sin(q2))
J23=-(a3*math.cos(q2)*math.sin(q3))-(a2*math.cos(q2))
J24=0
J25=0
J26=0
J31=0
J32=-(a3*math.cos(q2)*math.sin(q3))-(a2*math.cos(q2))
J33=-(a3*math.sin(q2)*math.cos(q3))-(a2*math.sin(q2))
J34=0  
J35=0
J36=0
J41= 


J = [[J11,J12,J13,J14,J15,J16],[J21,J22,J23,J24,J25,J26],[J31,J32,J33,0,0,0],[J41]]