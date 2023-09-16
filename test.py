from ultralytics import YOLO
import cv2
model = YOLO("yolov8n.pt")
model1 = YOLO("best.pt")
frame = cv2.VideoCapture("E:/Hackathon/Video_Phase1/Doto_132.mp4")
while True:
    ret, image = frame.read()
    resulst = model(image)
    resulst1 = model1(image)
    for resulsts in resulst:
        for resulsts1 in resulst1:
            box = resulsts.boxes
            box1 = resulsts1.boxes
            print(box,box1)
        cv2.imshow("Frame", image)
        # print(resulst)
        if cv2.waitKey(1) == ord('p'):
            break
