# Practical Course: Intelligent Mobile Robots with ROS (PCIMR)

## Tutorial 01: Linux, Software & ROS

### Introduction

The aim of the first tutorial was to demonstrate the effective completion of a basic ros node.
This included: a service call, publishing and subscribing.
This is demonsrated by:
- setting the initial location to 2,0 explicitly (can be tested by restarting the application after a few movement steps)
- taking sensor and location input, and using this to determine the move action.
- sending an appropriate move action to the robot.

### Code Overview

The required trajectory is quite simple. 
Move up until you encounter a wall, then move right until you encouter a wall, then move up until you encounter a wall, then move right again. 
In principle, if you can move up, move up. else, if you can move right, move right. If you can move neither up nor right, you are at your destination.
Whether there was a wall can be determined using the 'ranges' property of the scan object. 
Whether you are at your desintation can be determined also by whether you have reached the end position of 16, 12 as demarcated on the map.


