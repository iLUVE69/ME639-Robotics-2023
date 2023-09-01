# ME639-Robotics-2023




**Author** = **Shashank Ghosh**, **21110196**

**Mini-Project**
This repository contains 5 python scripts that are the solution to Task 1, Task 1(a), Task 2, Task3 and Task 4.

In **Task 1**, dynamics of the 2R manipulator is ignored and simply the joint angles are passed into the Forward Kinematics function to print a random trajectory. The joint anlges q1,q2 belong to (0,pi).

In **Task 1(a)**, dynamics are included by assuming m1=m2=1.0 , and I1=I2=0.3333 (I=1/3ml^2). Low speed and High speed trajectories are realised by setting the num_steps as Large(1000) for low speed trajectory and Low(100) for high speed trajectory. It is seen that 

In **Task 2**, dynamics are included and num_steps can be changed accordingly to incorporate high speed trajectory and Low speed speed trajectory.

In **Task 3**, The fixed mean point chosen is (1,1) and the manipulator acts as a spring about that point. Initial displaced end effector point is (1,0). The Code doesn't work ;(

In**Task 4**, The workspace of the Manipulator are all points inside the Semi-Circular Figure that the End effector traces. The Dynamics are ignored.
