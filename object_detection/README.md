# 图像物体识别 Demo

图像物体识别Demo具有前端界面利用摄像头拍摄图片，机器人节点获取和传输图片数据以及接收服务器处理结果消息，后台服务器接收图片数据进行物体识别处理并显示结果以及通知机器人节点结果消息。

## 框架设计

![framework](https://reganfan.github.io/assets/cloud-robot-diagram/framework.png)

## 运行时节点关系

机器人节点通过主题*chatter*将图片源数据发布出去，云服务器节点订阅该主题获取源图片数据；待云服务器节点识别处理完成后，通过主题*results*将完成消息发布出去，机器人节点订阅该主题，并将获得的处理消息传输到前端显示。

![node_graph](https://reganfan.github.io/assets/cloud-robot-diagram/node_graph.png)

## 示例

### 图片获取

![capture](https://reganfan.github.io/assets/cloud-robot-diagram/capture.PNG)

### 后台识别结果

![out_image](https://reganfan.github.io/assets/cloud-robot-diagram/out_image.jpg)

## 参考

本Demo极大地参考了以下代码的框架和设计：

- [RoboEyes--A face recognition demo for ROS.](https://github.com/shleeky/robo_eyes)
- [Quick Start: Jupyter notebook for off-the-shelf inference](https://github.com/tensorflow/models/blob/master/research/object_detection/object_detection_tutorial.ipynb)