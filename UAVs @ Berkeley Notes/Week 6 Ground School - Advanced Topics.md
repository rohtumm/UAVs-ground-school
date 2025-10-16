
1. What are the benefits of simulating a drone with software/hardware-in-the-loop before flying?
	- Lots of cost benefits, and it's a huge hassle to plan out actual fly days for the drone
	- We can test more complex software easily
	- We can test processing power and communication links
	- We can train AI models with the flight data
    
2. How is machine learning used to improve drone autonomy (navigation, obstacle avoidance, etc.)? What benefits does it have over traditional guidance systems like PID loops?
	- Supervised ML
		- Model learns from labeled flight data for tasks like object detection
	- Unsupervised ML
		- Model discovers patterns in sensor data (example is something like terrain clustering)
	- Reinforcement Learning
		- Model learns by trail and error to find the optimal solution in simulation (example is agile maneuvers)
	- Applications of ML include path planning in clustered environments, obstacle avoidance in real time, and adaptive control in different circumstances
	- Sim2Real transfer can be a challenge
		- It's very hard to get your model that works in simulation to work on the first try in real life
			- There's a lot of different variables that can throw off our algorithms which worked to perfection in simulation
		- Zeroshot: can you transfer to reality and get it to work on first try?
    
3. What is ROS, and why is it universal in autonomous robotics?
	- ROS is robot operating system
		- It's actually not an operating system, it runs on linux
		- It's an open source framework for building and running robotic software
		- Features include
			- Modularity: node based system for reusable code
			- Communication: topics, services, actions to pass messages between nodes
			- Ecosystem: there are lots of ros packages for existing sensors
			- Simulation support: it works right out of the box with Gazebo or Isaac Sim
	- Some definitions:
		- Node: Process that performs a specific function like a camera driver or path planner
		- Topic: Named place where nodes can publish messages or subscribe to listen for messages
		- Message: Data structure sent between nodes
		- Service: A request/response communication
		- Action: Service but supports long-running tasks
		- Package: Collection of ROS code, nodes, config files
		- Launch File: Script that starts the nodes
    
4. What are the steps/challenges of deploying ROS on embedded systems like the drone?
	- A big problem is synchronization between ROS systems (ROS 1 vs ROS 2) 
		- The current research robot uses ROS 1 with old cameras and other components
    