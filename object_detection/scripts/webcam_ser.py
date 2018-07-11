#!/usr/bin/env python
# -*- coding:utf-8 -*-
from flask import Flask
import time
from flask import render_template
from flask import request
import base64
from PIL import Image
from io import StringIO, BytesIO
import robo_talker
import cv2
import numpy as np
from sensor_msgs.msg import Image

app = Flask(__name__)

@app.route('/')
def webcam():
    return render_template('index.html')

@app.route('/upload', methods=['POST','GET'])
def upload():
    print('getting data from web.')
    if request.method == 'POST':
        image_b64 = request.form['img']
        robo_talker.talker(image_b64)
        imgdata = base64.b64decode(image_b64)
        with open('org_img.jpg', 'wb') as f:
            f.write(imgdata)
            
        time.sleep(3)
        if robo_talker.MSG != None:
            result = robo_talker.MSG
            robo_talker.MSG = None 
            return "result:" + result 
        else:
            return "无法识别"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=7777, ssl_context='adhoc')
