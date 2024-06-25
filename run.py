import cv2
import numpy as np
import mediapipe as mp

# This file simply outlines which lines should be removed or replaced in the run.py file of Concept-Bytes' Holomat tutorial part 2
# I did not include the original code here as I do not want to spread the source code that he shows to his patreon members.

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(static_image_mode=False,
                       max_num_hands=1, # These can be modified as you wish
                       min_detection_confidence=0.3,
                       min_tracking_confidence=0.4)

mp_drawing = mp.solutions.drawing_utils
cap = cv2.VideoCapture(0)

# These lines should be added after the imports
M = np.load("calibrate/M.npy")
homography = np.load("calibrate/homography_matrix.npy")

width, height = 2560, 1440


# Line 29 is not needed and should be deleted.
# As the M transformation matrix has already been multiplied with the homography matrix, we simply
# need the warpPerspective line and not the frame = cv2.undistort part.

while True:
    ret, frame = cap.read()
    if not ret: # I recommend adding this line in case of your camera not working
        break
    
    try:
        # All the code that was shown in the tutorial should be entered here
        print("Hi") # Placeholder so there is no error lol
        
    except Exception as e: # I also recommend adding this line to catch any errors (library compatibility issues etc).
        print(f"An error has occured: {e}")
        continue