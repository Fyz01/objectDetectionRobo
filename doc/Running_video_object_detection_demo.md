# Run video object detection demo

以下为具体的运行视频物体识别Demo的方法，请在运行前确保[安装](https://github.com/ReganFan/objectDetectionRobo/blob/master/doc/Installation.md)部署源码完成。

## 修改API源码路径

使用代码编辑器打开video_detection/scripts/objectdetect.py文件，根据你具体下载保存的物体识别API文件object_detection的路径来修改`OBJECT_DETECTION_PATH`的值，如下：

```python
# the path that object_detection folder locates, change it when you use it
OBJECT_DETECTION_PATH = "/home/fan/models/research/"
```

## 修改调用模型和下载地址

同样地，在objectdetect.py文件中找到如下代码：

```shell
MODEL_NAME = OBJECT_DETECTION_PATH + 'object_detection/' + 'ssd_mobilenet_v1_coco_2018_01_28'
MODEL_FILE = MODEL_NAME + '.tar.gz'
DOWNLOAD_BASE = 'https://reganfan.github.io/assets/models/'
```

`ssd_mobilenet_v1_coco_2018_01_28`为使用的物体识别模型名字，这是一个识别快速但准确率相对较低的模型，可以访问官方[detection_model_zoo](https://github.com/tensorflow/models/blob/master/research/object_detection/g3doc/detection_model_zoo.md)页面了解更多的模型信息，同时也可以下载其他模型，下载地址为http://download.tensorflow.org/models/object_detection/model_name ，其中model_name替换成上述的具体模型名字加版本号。同时需要提醒的是，下载模型需要科学上网，所以本次Demo使用了已上传在自己个人仓库的一个模型，如果你只想看看Demo的效果，就没有必要更改下载地址和模型了。

另外，如果你是第一次执行该代码，请取消以下部分代码的注释，当本地已有识别模型后，可以再次注释该下载模型代码：

```python
# Download Model
# if you have downloaded a model, you do not need to download it again
#opener = urllib.request.URLopener()
#opener.retrieve(DOWNLOAD_BASE + MODEL_FILE, MODEL_FILE)
#tar_file = tarfile.open(MODEL_FILE)
#for file in tar_file.getmembers():
#  file_name = os.path.basename(file.name)
#  if 'frozen_inference_graph.pb' in file_name:
#    tar_file.extract(file, os.getcwd())
```

## 其他代码修改

如果你在编译过程中遇到了cv2包引用路径出错的问题，请在video_detection/scripts/cam.py和objectdetect.py中找到以下代码：

```python
# correct the PYTHONPATH for opencv
sys.path.remove('/opt/ros/kinetic/lib/python2.7/dist-packages')
import cv2
```

请查看两个版本python的PYTHONPATH，然后将2.7版本的路径在执行时删除，即在`sys.path.remove()`中删除。如果你没遇到该问题，请注释掉这一行。

## 运行ROS环境

ROS运行环境必须为python2.7，所以请注意切换系统默认python版本为2.7，再执行下列指令：

```shell
roscore
```

## 启动服务器

打开一个新的Terminal，依次输入下列指令，编译并后台运行本地服务器：

```shell
cd ~/catkin_ws
catkin_make
source ~/catkin_ws/devel/setup.bash
roscd video_detection/
cd ./scripts/
# rosrun video_detection cloud_server.py
python3 cloud_server.py
```

由于创建资源包出现问题，无法正常使用rosrun来运行代码，目前仍未找到解决方法，所以这里直接使用`python3`执行程序。

## 启动本地摄像头拍摄视频

打开一个新的Terminal，依次输入下列指令，编译并启动本地摄像头拍摄视频：

```shell
cd ~/catkin_ws
catkin_make
source ~/catkin_ws/devel/setup.bash
roscd video_detection/
cd ./scripts/
# rosrun video_detection cam.py
python cam.py
```

由于创建资源包出现问题，无法正常使用rosrun来运行代码，目前仍未找到解决方法，所以这里直接使用`python`执行程序。

按键盘上的`Q`键会停止拍摄并保存源视频到 video_detection/scripts/my_test_videos/video1.mp4 。因为Demo较小，所以请控制视频长度在10s内，否则会出现警告提示。

## 运行过程示例

等待对视频源的物体识别处理结果：

![cam_catch](https://reganfan.github.io/assets/cloud-robot-diagram/cam_catch.PNG)

服务器正在对视频源进行物体识别分析：

![video_detect](https://reganfan.github.io/assets/cloud-robot-diagram/video_detect.PNG)

处理完成的识别视频会自动播放，并保存在 video_detection/scripts/my_test_videos/out_video1.mp4 。

模拟的摄像头前端接收到处理完成消息：

![finishdetection](https://reganfan.github.io/assets/cloud-robot-diagram/finishdetection.PNG)