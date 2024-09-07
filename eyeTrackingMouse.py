import cv2
import mediapipe as mp  # Face detection library
import pyautogui    # Mouse, keyboard, and clipboard control library this brings in the pywin32 library
webCam=cv2.VideoCapture(0) # open the camera  the 0 is the camera index  for example 0 is the first camera
face_mesh = mp.solutions.face_mesh.FaceMesh(refine_landmarks=True)
screen_w , screen_h = pyautogui.size() # get the screen size

while True:
    ret,frame=webCam.read()  # read the camera frame
    frame=cv2.flip(frame,1)  # flip the frame with 180 degree
    imgRGB=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    results=face_mesh.process(imgRGB)
    landmarks_points=results.multi_face_landmarks
    # print(landmarks_points)
    frame_h,frame_w,_=frame.shape
    if landmarks_points:
        landmarks=landmarks_points[0].landmark
        for id,landmark in enumerate(landmarks[474:478]):
            x=int(landmark.x*frame_w)
            y=int(landmark.y*frame_h)
            # print(x,y)
            cv2.circle(frame,(x,y),3,(0,0,255))
            if id==1:
                screen_x=screen_w*landmark.x
                screen_y=screen_h*landmark.y
                pyautogui.moveTo(screen_x,screen_y)
        left=[landmarks[145],landmarks[159]]        
        for landmark in left:
            x=int(landmark.x*frame_w)
            y=int(landmark.y*frame_h)
            cv2.circle(frame,(x,y),3,(0,255,255))
        if(left[0].y-left[1].y) < 0.004:# if the distance between the two eyes is more than 0.5 then the mouse is moving up
            pyautogui.click(button='wheelUp')
            pyautogui.sleep(1)
        
    
    cv2.imshow('Eye Tracking Mouse',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

webCam.release()
cv2.destroyAllWindows() # close all the windows opened by opencv  q
##ghhgfdfhggggggggggggg   kkkdkkd