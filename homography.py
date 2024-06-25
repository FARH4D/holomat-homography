import cv2
import numpy as np

def warp_image_without_zoom(img, src_points):

    h, w = img.shape[:2] # Gets the dimensions of your image
    
    src = np.float32(src_points) # Converts the source points list into a numpy array 
    
    H, _ = cv2.findHomography(src, np.float32([[0,0], [w,0], [w,h], [0,h]])) # Finds a homography matrix that maps the source points to the destination points
                                                            # All the destination points correspond to the corners of the output image
    
    corners = np.float32([[0,0], [w,0], [w,h], [0,h]]).reshape(-1,1,2) # Creates a numpy array for the 4 corners of the image, they have to be reshaped so they can fit the format to be put into the perspective transform function
    transformed_corners = cv2.perspectiveTransform(corners, H) # Applies my homography matrix to the corners of the image
    
    min_x = np.min(transformed_corners[:,:,0]) # Finds the leftmost, rightmost, topmost and bottommost points of the transformed
    max_x = np.max(transformed_corners[:,:,0]) # image, this is so we can find the bounding box of the transformed image.
    min_y = np.min(transformed_corners[:,:,1]) # the bounding box is the smallest rectangle that can enclose the image, 
    max_y = np.max(transformed_corners[:,:,1]) # ensures the transformed image fits in the new image dimensions without any parts being cut off
    
    out_w = int(max_x - min_x) # Calculates the width and height of the new image using the minimum and maximum coordinates
    out_h = int(max_y - min_y)
    
    dst = np.float32([
        [0 - min_x, 0 - min_y], # Creates an array of the destination points for the transformation, this is so the transformed
        [w - min_x, 0 - min_y], # image can fit in the new dimensions (otherwise it zooms out a lot)
        [w - min_x, h - min_y],
        [0 - min_x, h - min_y]
    ])
    
    M = cv2.getPerspectiveTransform(src, dst) # Calculates the transformation matrix that maps the source points to the destination points
    warped = cv2.warpPerspective(img, M, (out_w, out_h)) # Applies the transformation to the image using M and the calculated width and height
    np.save('homography_matrix.npy', H)
    
    return warped

img = cv2.imread('unwarpedImage.jpg') # Loading my distorted image

pts_src = []
for i in range(4):
    r = cv2.selectROI("Select Point", img)  # Lets me manually select the 4 corners
    pts_src.append([r[0], r[1]])
    cv2.destroyWindow("Select Point")

pts_src = np.array(pts_src)

warped_img = warp_image_without_zoom(img, pts_src)

cv2.imwrite('warpedImage.jpg', warped_img )# Saves the newly warped image
cv2.imshow('Warped Image', warped_img)
cv2.waitKey(0)
cv2.destroyAllWindows()