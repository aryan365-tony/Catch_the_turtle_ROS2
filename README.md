# Catch_the_turtle_ROS2


Following is the use of ROS2 with Turtlesim



1. first.py acts as a basic program that logs data in terminal
   
2. Circle.py uses the publish method to communicate with turtlesim and make it move in circular path as required

3. Pose.py works as a feedback from the turtle. It communicates with program through topic and returns the positions of turtle in window.

4. turtle_control.py is the main program that has program to catch the turtle. It randomly spawns the turtle and make other turtle chase it. Uses both publish and subscription method to move turtle and accept pose feedback from it.



Before using the codes,
>>>Make Sure ROS2 is installed

>>>Create A ros2 workspace in a folder and clone src/my_robot_control in the workspace folder

>>>Run "colcon build" in the terminal at path of workspace folder

>>>Source the setup.bash script in the install folder in the workspace folder

>>>Run turtlesim before running the codes that use it.
