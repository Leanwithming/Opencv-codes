import cv2

cap = cv2.VideoCapture("G:\Outplayed\CSGO\CSGO_10-12-2022_14-33-58-52\CSGO_10-12-2022_14-59-55-555.mp4")

while True:

    success, img = cap.read()
    cv2.imshow("video", img)
    cv2.waitKey(1)