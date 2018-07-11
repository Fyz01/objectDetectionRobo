#!/usr/bin/env python
# -*- coding:utf-8 -*-
import numpy as np
from std_msgs.msg import String
import robo_talker
import sys
# correct the PYTHONPATH for opencv
sys.path.remove('/opt/ros/kinetic/lib/python2.7/dist-packages')
import cv2

# video starts
cap = cv2.VideoCapture(0)

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('my_test_videos/video1.mp4',fourcc, 20.0, (640,480))

while(cap.isOpened()):
    ret, frame = cap.read()
    if ret==True:
        # do flipping 
        #frame = cv2.flip(frame,1)

        # write the flipped frame
        out.write(frame)

        cv2.imshow('frame',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

# Release everything if job is finished
cap.release()
out.release()
cv2.destroyAllWindows()

# start waiting result
print("waiting...")
message = String()
message.data = "video detection start"
robo_talker.talker(message)


# then check the result
if robo_talker.MSG != None:
    result = robo_talker.MSG
    robo_talker.MSG = None 
    print("result:" + result) 
else:
    print("无法识别")

'''
videoCapture = cv2.VideoCapture()
videoCapture.open('output.avi')

fps = videoCapture.get(cv2.CAP_PROP_FPS)
frames = videoCapture.get(cv2.CAP_PROP_FRAME_COUNT)
#fps是帧率，意思是每一秒刷新图片的数量，frames是一整段视频中总的图片数量。
print("fps=",fps,"frames=",frames)

for i in range(int(frames)):
    ret,frame = videoCapture.read()
    cv2.imwrite("image_storage/frame.avi(%d).jpg"%i,frame)

    f = open(r'image_storage/frame.jpg', 'rb')
    image_b64 = base64.b64encode(f.read())
    robo_talker.talker(image_b64)
    '''

if __name__ == '__main__':
    pass