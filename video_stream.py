# -*- coding: utf-8 -*-
"""
Created on Wed Jul  6 21:30:17 2022

@author: Yogov
"""

import cv2
import pickle

cap = cv2.VideoCapture("rtsp://admin:GZVTFN@192.168.1.4:554/H.264")

frames_list=[]

while(cap.isOpened()):
    ret, frame = cap.read()
    print("Ret is : ",ret)
    #print("Frame is : ",frame)
    cv2.imshow('frame', frame)
    frames_list.append(frame)
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()

print("Frames List : ",frames_list)


#with open('E://RTSP_STREAM//outfile.dat', 'wb') as fp:
#   pickle.dump(frames_list, fp)


with open("E://RTSP_STREAM//outfileframes1.dat", "w") as outfile:
    #outfile.write("\n".join(str(frames_list)))
    outfile.write(str(frames_list))
    
 
print("Process Completed ...")    