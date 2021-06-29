import numpy as np
import cv2
import math
from pygame import mixer
import time

drum=cv2.imread("drum/pad2.jpg")
drum=cv2.resize(drum, (0,0),fx=0.35,fy=0.35)
cap = cv2.VideoCapture(0)
curr_time=[0]*8
time_delay=0.5
while True:
    ret, frame = cap.read()
    if cv2.waitKey(25) ==ord(' ') or ret==False:
        break
    for i in range(len(frame)):
        frame[i]=frame[i][::-1] #taking mirror frame for convenience
    frame_h,frame_w,_=frame.shape
    drum_h,drum_w,__=drum.shape

    # taking the region of interest to put the watermark
    top_y=(frame_h-drum_h)//2
    top_x=(frame_w-drum_w)//2

    bottom_y=(frame_h+drum_h)//2
    bottom_x=(frame_w+drum_w)//2

    range_x=bottom_x-top_x
    range_y=bottom_y-top_y

    roi=frame[top_y:bottom_y,top_x:bottom_x]
    watermark=cv2.addWeighted(roi, 1, drum, 0.8, 0)
    result=np.array(frame)
    result[top_y:bottom_y,top_x:bottom_x]=watermark
    mask=cv2.inRange(frame, np.array([0,0,150]), np.array([60,60,255]))
    cv2.imshow("Watermarked", result)
    # cv2.imshow("masked",mask)
    beat=[0,0]
    target = np.where(mask==255)
    if target[0].size==0:
        continue
    target_h = target[0][len(target[0])//2]
    target_w = target[1][len(target[1])//2]

    beat=[math.ceil(((target_h-top_y)/range_y)*2),math.ceil(((target_w-top_x)/range_x)*4)]
    #beat[0] denotes row of drum
    #beat[1] denotes column of drum
    #red colour in one of the eight parts
    #of the drum makes that part beat
    mixer.init()

    if beat[0]==1 :

        if beat[1]==1 and time.time()-curr_time[0]>time_delay:
            mixer.music.load("drum/Oct1.mp3")
            mixer.music.play()
            curr_time[0]=time.time()

        if beat[1]==2 and time.time()-curr_time[1]>time_delay:
            mixer.music.load("drum/Oct2.mp3")
            mixer.music.play()
            curr_time[1]=time.time()

        if beat[1]==3 and time.time()-curr_time[2]>time_delay:
            mixer.music.load("drum/Oct3.mp3")
            mixer.music.play()
            curr_time[2]=time.time()

        if beat[1]==4 and time.time()-curr_time[3]>time_delay:
            mixer.music.load("drum/Oct4.mp3")
            mixer.music.play()
            curr_time[3]=time.time()


    if beat[0]==2:

        if beat[1]==1 and time.time()-curr_time[4]>time_delay:
            mixer.music.load("drum/Oct5.mp3")
            mixer.music.play()
            curr_time[4]=time.time()

        if beat[1]==2 and time.time()-curr_time[5]>time_delay:
            mixer.music.load("drum/Oct6.mp3")
            mixer.music.play()
            curr_time[5]=time.time()

        if beat[1]==3 and time.time()-curr_time[6]>time_delay:
            mixer.music.load("drum/Oct7.mp3")
            mixer.music.play()
            curr_time[6]=time.time()

        if beat[1]==4 and time.time()-curr_time[7]>time_delay:
            mixer.music.load("drum/Oct8.mp3")
            mixer.music.play()
            curr_time[7]=time.time()

    # print(beat)

cv2.waitKey(0)
cv2.destroyAllWindows()




