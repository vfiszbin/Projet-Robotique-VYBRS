# GoPiGo Robot Programming

This project involves programming a GoPiGo robot on a Raspberry Pi to execute a series of strategies for navigating its environment.

The robot can execute different strategies in a sequence, offering the following functionalities:
- Moving forward or backward for a specified distance at a designated speed.
- Rotating by a certain angle at a given speed.
- Maneuvering in square or triangular patterns.
- Maneuvering in an arc pattern, where parameters like the diameter of the arc, speed, and direction (clockwise or counter-clockwise) can be set.
- Obstacle detection: during strategy execution, a laser sensor is used to prevent collisions. If an obstacle is detected, the robot can either change its course or stop, depending on the strategy in use.
- Target detection: the robot's camera output is analyzed to enable target detection and following. In this mode, the robot scans its environment for a specific target (usually a colorful object) and moves toward it. The image analysis algorithm was made from scratch using Numpy for efficiency.
