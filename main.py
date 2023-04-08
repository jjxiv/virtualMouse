import mediapipe as mp
import cv2
import pyautogui

cap = cv2.VideoCapture(0) # Select the camera to be used
hand_detector = mp.solutions.hands.Hands() # Use variable for detecting hand
drawing_utils = mp.solutions.drawing_utils # Use variable for drawing POINTS in hands
screen_width, screen_height = pyautogui.size()
index_y = 0

while True:
    _, frame = cap.read() # read every frame
    frame = cv2.flip(frame, 1) # the frame should be flipped because of pov
    # frame is flipped on y axis that has value of 1
    frame_height, frame_width, _ = frame.shape

    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB) # convert frame rgb to bgr
    output = hand_detector.process(rgb_frame) # display the coordinates where the hand is

    #get the hand landmarks
    hands = output.multi_hand_landmarks
    print(hands)

    if hands:
        for hand in hands:
            drawing_utils.draw_landmarks(frame, hand)
            landmarks = hand.landmark
            for id, landmark in enumerate (landmarks):
                # pass the landmarks and counts
                # Get the landmark coordinates first of id == 8 (the tip of index)
                x = int(landmark.x*frame_width) # this is multiplied to framewidth in order to get values that are close to frame values
                y = int(landmark.y*frame_height)
                print(x,y)

                if id == 8: # INDEX FINGER
                    cv2.circle(img=frame, center=(x,y), radius=10, color =(0,255,255))
                    index_x = (screen_width / frame_width) * x
                    index_y = (screen_height / frame_height) * y
                    # pyautogui.moveTo(index_x,index_y)

                if id == 12:  # middle FINGER
                    cv2.circle(img=frame, center=(x, y), radius=10, color=(0, 255, 255))
                    index_MX = (screen_width / frame_width) * x
                    index_MY = (screen_height / frame_height) * y
                    pyautogui.moveTo(index_MX, index_MY)

                if id == 4: # THUMB FINGER
                    cv2.circle(img=frame, center=(x, y), radius=10, color=(0, 255, 255))
                    thumb_x = (screen_width / frame_width) * x
                    thumb_y = (screen_height / frame_height) * y
                    print("outside", abs(index_y - thumb_y))

                    if abs(index_y - thumb_y) < 20:
                        pyautogui.click()
                        pyautogui.sleep(1)
                        print("clicked")

                    # draw a circle on the 8. INDEX_FINGER_TIP
                    # create 10 radius pixel in the center of x and y
                    # assign color yellow
    cv2.imshow('Virtual Mouse', frame)
    cv2.waitKey(1)

