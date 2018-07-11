#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Software License Agreement (BSD License)
#
# Copyright (c) 2008, Willow Garage, Inc.
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
#  * Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
#  * Redistributions in binary form must reproduce the above
#    copyright notice, this list of conditions and the following
#    disclaimer in the documentation and/or other materials provided
#    with the distribution.
#  * Neither the name of Willow Garage, Inc. nor the names of its
#    contributors may be used to endorse or promote products derived
#    from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
# FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
# COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
# INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
# BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
# LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN
# ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.
#
# Revision $Id$

## Simple talker demo that listens to std_msgs/Strings published 
## to the 'chatter' topic

import rospy
from std_msgs.msg import String
import time
import base64
import os
import objectdetect
import sys
import cv2
#import glob


def callback(data):
    '''
    #根据自己的实际情况更改目录。
    #要转换的图片的保存地址，按顺序排好，后面会一张一张按顺序读取。
    convert_image_path = 'image_storage'

    #帧率(fps)，尺寸(size)，此处设置的fps为24，size为图片的大小，本文转换的图片大小为400×1080，
    #即宽为400，高为1080，要根据自己的情况修改图片大小。
    fps = 24
    size = (400,1080)

    IN_VIDEO_PATH = 'my_test_video/video2.avi'
    videoWriter = cv2.VideoWriter('my_test_video/video2.avi',cv2.VideoWriter_fourcc('I','4','2','0'), fps, size)

    for img in glob.glob(convert_image_path + "/*.jpg") :
        read_img = cv2.imread(img)
        videoWriter.write(read_img)
    videoWriter.release()
    '''
    '''
    imgdata = data.data
    imgdata = base64.b64decode(imgdata)
    print(type(imgdata))
    upload_image_path = 'image_storage/frame.jpg'
    with open(upload_image_path, 'wb') as f:
        f.write(imgdata)
    '''

    print(data.data)

    res = objectdetect.video_detect()
    print(res)
    ret_message = String()
    ret_message.data = res
    pub = rospy.Publisher('results', String, queue_size=10)
    
    # keep publishing for 1 min
    start_time = time.clock()
    while not rospy.is_shutdown():
        pub.publish(ret_message)
        wait_time = time.clock() - start_time
        if wait_time >= 60:
            break 


def listener():

    # In ROS, nodes are uniquely named. If two nodes with the same
    # name are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('cloud_server', anonymous=True)

    rospy.Subscriber('chatter', String, callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    listener()
