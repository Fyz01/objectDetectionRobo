# Run image object detection demo

以下为具体的运行图像物体识别Demo的方法，请在运行前确保[安装](https://github.com/ReganFan/objectDetectionRobo/blob/master/doc/Installation.md)部署源码完成。

## 修改API源码路径

使用代码编辑器打开object_detection/scripts/objectdetect.py文件，根据你具体下载保存的物体识别API文件object_detection的路径来修改`OBJECT_DETECTION_PATH`的值，如下：

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

使用代码编辑器打开object_detection/scripts/cloud_server.py文件，找到以下代码：

```python
# correct the PYTHONPATH for opencv
sys.path.remove('/opt/ros/kinetic/lib/python2.7/dist-packages')
import cv2
```

如果你遇到了cv2包引用路径出错的问题，可以查看两个版本python的PYTHONPATH，然后将2.7版本的路径在执行时删除，如上。如果你没遇到该问题，请注释掉`sys.path.remove()`一行。

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
roscd object_detection/
cd ./scripts/
rosrun object_detection cloud_server.py
```

![cloud_server.py](https://reganfan.github.io/assets/cloud-robot-diagram/cloud_server.PNG)

## 启动前端网页

打开一个新的Terminal，依次输入下列指令，编译并启动前端网页：

```shell
cd ~/catkin_ws
catkin_make
source ~/catkin_ws/devel/setup.bash
roscd object_detection/
cd ./scripts/
rosrun object_detection webcam_ser.py
```

![webcam_ser.py](https://reganfan.github.io/assets/cloud-robot-diagram/webcam_ser.PNG)

## 查看本地IP

```shell
ifconfig
```

![ifconfig](https://reganfan.github.io/assets/cloud-robot-diagram/ifconfig.PNG)

比如上述的本地IP为192.168.233.133，那么前端页面的访问地址为https://192.168.233.133:7777

## 访问页面并拍摄图片

可以使用手机端或PC端网页访问上述地址，不过必须保证访问端和服务器是在同一局域网内。进入页面，选择好拍摄图片后，点击左下角的CAPTURE按钮截取图片，并获得返回信息。

![capture](https://reganfan.github.io/assets/cloud-robot-diagram/capture.PNG)

那么在后台，会收到传输的图片，保存在 object_detection/scripts/my_test_images/image1.jpg ，然后显示识别处理后的图片，并保存在 object_detection/scripts/out_images/out_image1.jpg 。

![out_image](https://reganfan.github.io/assets/cloud-robot-diagram/out_image.jpg)