# Lab 1: Intro to ROS 2

## Written Questions

### Q1: During this assignment, you've probably ran these two following commands at some point: ```source /opt/ros/foxy/setup.bash``` and ```source install/local_setup.bash```. Functionally what is the difference between the two?

Answer: ```source /opt/ros/foxy/setup.bash``` Is the underlay that contains all the ROS2 commands and build tool and gives the terminal access to them. ```source install/local_setup.bash``` is the overaly that adds only the specific packages that you built in your workspace. 

### Q2: What does the ```queue_size``` argument control when creating a subscriber or a publisher? How does different ```queue_size``` affect how messages are handled?

Answer: A buffer for late messages. When the subscribers can't consume what the publisher is publishing to a topic, a queue builds up. The queue size, is the number of messages that will be kept before the oldest ones are dropped. 

### Q3: Do you have to call ```colcon build``` again after you've changed a launch file in your package? (Hint: consider two cases: calling ```ros2 launch``` in the directory where the launch file is, and calling it when the launch file is installed with the package.)

Answer: It depends, because running it with let's say ```ros2 launch lab1_pkg lab1_launch.py``` , it uses the compiled install folder and not the the actual launch file. If we wanted to not have to call colcon build, we would point the command directly to the launch file and not have to call colcon since the command is not looking at the install directory anymore. 
