1. Main components:
- Onboard computer: NVIDIA Jetson Orin Nano
	- Does all the computation/calculations
- Gimbal camera: stabilizes camera footage
- Cube (flight controller)
	- Responsible for stabilizes drone's flight and adjusts motors' speeds to maintain control
	- Runs Ardupilot
- GPS receivers
- WIFi antenna

2. Software Specs:
- Object Detection
	- Done using OpenCV/YOLO
- Aerial Imagery
	- OpenCV/OpenDroneMap is used

3. Projects we can work on:
	- Reinforcement learning for improving flight controller
	- Try out different computer vision techniques for improving object detection
	- Different methods for real-time stitching
	- Applications only
		- Aerial Imagery

4. Commercial vs Hobbyist Tech Stack
	- Flight Software
		- Hobbyist: Ardupilot/Betaflight
		- Commercial: ROS, PX4
	- Real-time Autonomy
		- Hobbyist: YOLO
		- Commercial: SLAM (Simultaneous Localization and Mapping), path planning, AI inference
	- Compliance and Safety
		- Hobbyist: RFID
		- Commercial: Automated risk assessments, airspace alerts
	- Data Integration
		- Hobbyist: Local
		- Commercial: Cloud (need to be able to operate without seeing aka BVLOS - Beyond Visual Line of Sight)

5. How to learn about drones effectively?
	- AI is good for answering specific niche questions about a topic of interest, but don't just ask it to code everything for you
	- Go to OH/ask peers