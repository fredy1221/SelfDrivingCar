# Self Driving Cars in Carla
Self driving car control in Carla simulator using DL techniques

## Project general overview
Self-driving cars are definitely coming into our day-to-day life sooner or later, and controlling them will be heavily impacted by AI and especially deep learning. The project consists of simulating a car in a virtual environment, where we can control it using AI. The main tasks are to design and test Deep Learning models for autonomous driving scenarios. Gather data from different sensors and join them to actuate commands from the Deep Learning module. A comparison will be made with classical computer vision techniques to see where the DL stands out and where the classical methods are enough.
 
## Results
To test our controller we will use a virtual world made of a racetrack only to avoid any other objects that might distract the control like pedestrians and other cars. To simulate our controller, we will track a trajectory made of waypoints. Each waypoint is a (x,y) coordinate and desired linear speed vx.

![Results](https://github.com/fredy1221/SelfDrivingCar/blob/master/Images/results_control.jpg)

The x-axis represents the time variable in all of the graphs. The forward speed graphs show the increase in speed at the beginning, to go from the initial position to the steady-state speed. The increase in speed required a considerable amount of throttle. It directly reflects the car’s acceleration. A decrease in throttle leads to a direct decrease in forward speed. In this example, the throttle is always positive because we didn’t need to break at any point on the trajectory. The steering angle represents the steering wheel, we can see it varying on the positive and negative sides, but always in small vales. This is to make sure we meet the passenger’s comfort requirements. We can also check that we are actually following the required speed during the trajectory. This was verified due to the fact that both orange and blue lines are nearly the same.
For simplicity reasons, we will just show the trajectory that we successfully were able to follow.
We can see from the following picture that 89% of the waypoints were met precisely and the general trajectory is the same as the desired one, so this controller will be implemented in our simulations.

![Trajectory](https://github.com/fredy1221/SelfDrivingCar/blob/master/Images/trajectory.jpg)

Once we detected the lines, the job is basically done. We can calculate the center of the road, thus planning where the car should drive. This location will be sent to the longitudinal and lateral control to ensure a smooth driving experience and that we respect the planned trajectory. By doing so, we were successfully able to specify the car’s position based on the two lines that delimit the road. This was made assuming nothing blocks the lines from the car’s camera and the lines are always visible with no hard turns. It can be used to drive on relatively straight roads, with few turns, that can still be considered as straight lines at each sample time. 

![Lines using classical computer vision](https://github.com/fredy1221/SelfDrivingCar/blob/master/Images/lines.jpg)

This technique is good enough under a very limited environment where the lines are clearly visible, with little to no curvature in the road, and without any cars blocking the lines from the range of the camera. If any condition is not met anymore, or we can no longer detect the lines, then this technique will fail. That’s why a deep learning approach is encouraged.
Other limitations emerge when the driver is on a highway with multiple lines, confusion can arise we could easily detect lines that are not on our driving lane which can cause problems.
