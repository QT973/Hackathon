import cv2
import time
import os

pTime = 0
count = 0
dem = 0
cap = cv2.VideoCapture("E:/Hackathon/Video_Phase1/Kabu_88.mp4")
path_folder = "E:/Hackathon/Data/Kabu_88"
while True:
    ret, image = cap.read()
    # image = cv2.resize(frame, (920, 840))
    # fps
    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime
    cv2.putText(image, f"FPS:{int(fps)}", (20, 20),
                cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (255, 0, 255), 1)
    # cut image
    if count % 15 == 0:
        save_path = os.path.join(path_folder, f'Kabu_88_{dem+1}.jpg')
        cv2.imwrite(save_path, image)
        dem +=1
    count = count + 1
    cv2.imshow('Webcam', image)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
