# Practical Course: Intelligent Mobile Robots with ROS (PCIMR)

## Tutorial 03: Probability Theory & Localization

### Introduction

Demonstrate basic knowledge of probability theory and an understanding of the principles of mobile robot localization. 

After completing this exercise you should be able to
- understand work with uncertainties in robotics and beyond
- understand how mobile robot localization works in general, including the challenges that arise:
  - potential problems due to uncertainties in the sensor, movement, etc.
  - discretization/approximation of the real-world
- implement a variety of mobile robot localization algorithms

The *navigator_node* is responsible for navigating the robot from its current position to another free cell in the world. 
It is started with: roslaunch pcimr_navigation navigation.launch

The move command is now modified to be uncertain, in order to make the simulation a bit more realistic. There are 5 values specifying this uncertainty:

    [𝑝(𝑢=𝑢 ̂ ),𝑝(𝑢=𝑢 ̂−90°),𝑝(𝑢=𝑢 ̂+90°),𝑝(𝑢=𝑢 ̂−180°), 𝑝(𝑢=∅)]

where 𝑢 is the performed action, 𝑢 ̂ is the expected action, 𝑢 ̂−90°, 𝑢 ̂+90°,  𝑢 ̂−180° the actions left, right and backwards with respect to the expected action 𝑢 ̂. The last one, ∅, stands in this case for no movement at all, i.e. the robot stays at its position.

---
### Code Overview

I parsed the move uncertainty into another array [0, +90, +180, +270] 
where 0 implies a desired move command and the actual command coicide
and +90 implies an attempted move forward, might instead move 90 degrees anti clockwise
I included the following arrays to assist in navigating movements and indices:
MOVE_IDS = 'NWSE'
MOVES = [np.array([0, 1]), # Up
        np.array([-1, 0]), # Left
        np.array([0, -1]),   # Down
        np.array([1, 0])]    # Right
SCAN_DIRECTIONS = [np.array([0, -1]),   # Down
                    np.array([-1, 0]), # Left
                    np.array([0, 1]),   # Up
                    np.array([1, 0])]   # Right 
Together, they enabled me to implement the probabilities algorithmically, in such a way that it could be extended for greater granularity, or a wider span of scan and movement possiblities. 
I published and subscribed to the following topics. 
        # Publishers
        ('/visualization/robot_pos', Marker,)
        ('visualization/robot_pos_array', MarkerArray)
        ('/robot_pos', Point)

        # Initialize Subscribers
        ('/move', String,)
        ('/scan', LaserScan
        ('/map', OccupancyGrid)
Remarks:
I found that the accuracy of the scanner alone was enough to entirely achieve the goal. Therefor, as the move certainty was reduced, I also downweighted the effect of the prior. This approach is typically adoped as a kalman filter, but I simply multiplied the prior by the probability of "correct" motion, ie, 0.7

The robot getting lost, by changing the rand_init_pos did fail on the system. 
It occured that the prior and likelihood had no coincidence, ie, the sensors data did not agree with any of the other prior belief.
If this occured, as measured by the the sum of all posterior possibilies being zero, I discarded the prior for the iteration and completely relied on the sensor data.
