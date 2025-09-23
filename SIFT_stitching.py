import cv2
import numpy as np

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

# SIFT feature detector + brute force matcher
sift = cv2.SIFT_create()
bf = cv2.BFMatcher()

frame1_kp = cv2.drawKeypoints(frames[0], sift.detect(frames[0], None), None)
frame2_kp = cv2.drawKeypoints(frames[1], sift.detect(frames[1], None), None)
cv2.imwrite('frame1_keypoints.png', frame1_kp)
cv2.imwrite('frame2_keypoints.png', frame2_kp)

def stitch_images(img1, img2):

    kp1, des1 = sift.detectAndCompute(img1, None)
    kp2, des2 = sift.detectAndCompute(img2, None)

    matches = bf.knnMatch(des1, des2, k=2)

    # ratio test to filter good matches (basically compares distances of two closest matches)
    good_matches = []
    for m, n in matches:
        if m.distance < 0.75 * n.distance:
            good_matches.append(m)

    
    src_pts = np.float32([kp1[m.queryIdx].pt for m in good_matches]).reshape(-1, 1, 2)
    dst_pts = np.float32([kp2[m.trainIdx].pt for m in good_matches]).reshape(-1, 1, 2)

    # homography matrix 
    H, mask = cv2.findHomography(src_pts, dst_pts, cv2.RANSAC, 5.0)

    h1, w1 = img1.shape[:2]
    h2, w2 = img2.shape[:2]

    # hard code canvas size to be large enough to hold both images (need to fix)
    result = cv2.warpPerspective(img1, H, (max(w1, w2), h1 + h2))

    result[0:h2, 0:w2] = img2

    return result
    
# run the stitching
stitched_image = frames[0]
for i in range(1, len(frames)):
    stitched_image = stitch_images(stitched_image, frames[i])

cv2.imshow('stitched', stitched_image)
cv2.imwrite('stitched_output_SIFT.png', stitched_image)
cv2.waitKey(0)
cv2.destroyAllWindows()