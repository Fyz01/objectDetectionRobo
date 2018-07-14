# ObjectDetectionRobo - 物体识别云机器人系统

ObjectDetectionRobo是一个兼具静态和动态物体识别（图像和视频物体识别）功能的云机器人系统。该系统的主要运行流程是机器人通过图像输入设备（如摄像机）获取图像或视频识别源，经由ROS机器人操作系统中间件对源数据进行初步处理，并传输数据到远程云服务器进行物体识别相关的计算、大数据分析以及数据存储操作。目前，项目处于初始开发阶段，用于个人专业实训学习内容，只提供了两个简单的Demo。

[实训总结报告]()

## Table of contents

**Setup:**

- [Installation](https://github.com/ReganFan/objectDetectionRobo/blob/master/doc/Installation.md)

**Running:**

- [Running image object detection demo](https://github.com/ReganFan/objectDetectionRobo/blob/master/doc/Running_image_object_detection_demo.md)
- [Running video object detection demo](https://github.com/ReganFan/objectDetectionRobo/blob/master/doc/Running_video_object_detection_demo.md)
- [Sample Output](https://github.com/ReganFan/objectDetectionRobo/blob/master/doc/Sample_Output.md)

**References:**

- [RoboEyes-云计算与机器人系统](http://www.vsaint.club/wordpress/)
- [Tensorflow Object Detection API](https://github.com/tensorflow/models/tree/master/research/object_detection)
- [Video Object Detection System Tutorial on Windows 10](https://blog.csdn.net/xiaoxiao123jun/article/details/76605928)

## Technology and framework

**Language:**

- python(2.7 and 3.5)

**Web Framework:**

- Flask

**Development Platform:**

- Ubuntu-16.04
- ROS-Kinetic

**Object Detection API:**

- [Tensorflow Object Detection](https://github.com/tensorflow/models/tree/master/research/object_detection)

**Image Processing Library:**

- OpenCV
- Matplotlib

## Maintainers

- Yeshu，github：[ReganFan](https://github.com/ReganFan)
- Fan，github：[Fyz01](https://github.com/Fyz01)

## Release information

### July 16, 2018

面向机器人的软件设计与开发实训项目制品交付，提供了[图像物体识别Demo](https://github.com/ReganFan/objectDetectionRobo/tree/master/object_detection)和[视频物体识别Demo](https://github.com/ReganFan/objectDetectionRobo/tree/master/video_detection)。图像物体识别Demo具有前端界面利用摄像头拍摄图片，机器人节点获取和传输图片数据以及接收服务器处理结果消息，后台服务器接收图片数据进行物体识别处理并显示结果以及通知机器人节点结果消息。视频物体识别Demo简单地利用本地摄像头拍摄短视频，经过机器人节点通知消息，本地服务器读取视频并进行物体识别处理，返回结果识别视频，同时通知机器人节点结果消息。

**Thanks to contributors:**  Yeshu，Fan
