import cv2

vid = cv2.VideoCapture('Minecraft_stitch_test.mp4')
#frames is a list of all the frames in the video with shape 1652 (height) 2880 (width) 3 (color channels) - very large !!
frames = []
while True:
    ret, frame = vid.read()
    if not ret:
        break
    frames.append(frame)

#downsample num of frames 
frames = frames[::38]

#downsize the image to 1/4th the size
for i in range(len(frames)):
    frames[i] = cv2.resize(frames[i], (0,0), fx=0.25, fy=0.25)


stitcher = cv2.Stitcher_create(cv2.Stitcher_SCANS)
status, stitched = stitcher.stitch(frames)

#display stitched image
cv2.imshow('stitched', stitched)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite('stitched_output_second_trial.png', stitched)