
1. How do we communicate with the drone while it’s in the air?
	- We use a hybrid Mavlink/DDS model
	- Radio and Ground Station
		- Ground Station
			- Communicates with the onboard computer over WiFi (UDP) (drone is wifi hotspot)
				- UDP: User Datagram Protocol
					- Fast and lightweight way of throwing data upon a request and seeing what goes through
					- Flight computer constantly sends messages for ground station to pick up on (packets can be lost oftentimes)
				- TCP: Transmission Control Protocol
					- Makes sure you have a user session between both sides before sending data
					- Much more reliable but slower
	- RC Transmitters and Receivers
		- TX
			- The handheld device
			- Uses radio protocols to communicate wirelessly with the receiver
		- RX
			- Mounted on drone, receives signals from transmitter
			- Passes commands to the FC via protocols like Serial Bus
    
2. What is the role of the onboard computer system and how does it complement the flight controller? How does it communicate?
	- Onboard computer is more for high level tasks, and runs things like CV, ROS, object detection
		- Sends commands to FC and receives telemetry for decision making
		- Connects via serial, Ethernet, or USB depending on setup
		- Jetson Orin Nano
			- USB-C port for data transfer
			- Ethernet port
				- Connects to gimbal camera
			- Display Port (HDMI)
				- can see what's in the brain of jetson
			- Lots of extra pins
			- SD card and WiFi
			- Built in AI accelerator designed for AI inference
			- Orin Nano: either 4 GB or 8 GB RAM
			- Runs Linux, we use Ubuntu
			- Runs ROS2 nodes for SLAM, path planning, control
	- FC
		- Processes radio inputs and executes control loops
		- Not autonomous usually
		- Communicates via protocols like MAVlink, usually over UART or CAN
	- 
    
3. What are the trade-offs between different data links (WiFi, radio, LTE)?
	- WiFi Pros
		- High bandwidth
		- Works well for short with communication
	- WiFi Cons
		- Limited range (few hundred meters)
		- Interference in commonly used bands
		- Line of sight required
	- Radio Pros
		- Can go very long range with proper antennas
		- Reliable, low latency
		- Works without cellular or WiFI
	- Radio Cons
		- Less data can be sent because of lower bandwidth (lower frequency)
		- Requires dedicated hardware that is not usually built into computers
		- Regulations on allowed frequencies
	- LTE (new) Pros
		- Wide wide coverage (because you're relying on cell towers which are everywhere)
		- High bandwidth and data rate
		- Skydio uses this
	- LTE Cons
		- Latency higher than WiFi and radio
		- Requires SIM card and data plan
		- There are some cell dead zones
	- Starlink?
		- Very new, mainly used in Ukraine
    
4. How does the onboard computer connect to the ground station or other devices over WiFi? (SSH tutorial)
	- SSH
		- Allows for secure remote access to computer so that we can send commands that are encrypted
    