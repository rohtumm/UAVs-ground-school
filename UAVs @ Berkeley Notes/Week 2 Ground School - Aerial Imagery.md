1. How are drones used for aerial imagery?
	- Search + rescue, agriculture, law enforcement, environmentalism
		- Oblique vs Nadir
		- RGB-D (provides depth)

2. OpenCV: General-purpose CV library that can do pretty much everything
	- 3D reconstruction, feature detection, photo manipulation, etc.
	- What parts do we use??
		- Feature detection
			- SIFT
				- Looks for all the corners in images and labels these as 'feature'
					- These features can then be used to match across images that are slightly distorted
					- Ultimately this is all linear algebra transformations in some shape/form
			- ORB
		- Feature matching
		- Image manipulation

3. Alternatives to writing our own imagery code?
	- OpenDroneMap
		- Pipeline:
			- Get pictures with Geo tags
			- Bunch of different settings you can adjust
			- Wait for program to stitch
			- Does a bunch of complicated 3d meshing, then takes a picture of it from top essentially (quite inefficient)

4. Next steps
	- Try to make our own image stitching algorithm with OpenCV that can run on our drone real-time
	- Try to neatly split up OpenDroneMap's stitching to make it more efficient
	- Also other projects:
		- SLAM
		- Optical Flow