# Installation

## Ubuntu 16.04 安装 ROS系统

本系统以及Demo的开发平台是Ubuntu-16.04和ROS-Kinetic，所以请参考下面博客链接进行安装，其中Ubuntu系统可以使用虚拟机装载：

- [RoboEyes(二)：Ubuntu 16.04 安装 ROS系统](http://104.194.92.237/wordpress/index.php/2018/03/13/roboeyess1/)

安装完成后，可以运行ROS系统自带的Tutorial进行简单的测试：

- [从零实现ROS乌龟移动](http://104.194.92.237/wordpress/index.php/2018/04/03/ros_turtialor/)

## 安装 Python3

Ubuntu系统本身已经自带了python，版本为2.7，而我们将要使用的 Tensorflow Object Detection API 则需要使用python3的版本，所以我们要额外地安装python3，这里就不详细说明python3的安装过程了。以下为一些小技巧，之后操作可能会用到。

查看当前系统默认的python版本：

```shell
python
```

快速切换系统默认python版本：

```shell
sudo rm /usr/bin/python
sudo ln -s /usr/bin/pythonX.X /usr/bin/python    # 其中pythonX.X后为版本号，比如2.7或3.5
```

## 安装 TensorFlow

TensorFlow是我们用到的Object Detection API所依赖的框架，这里我们可以进行简易安装：

```shell
# For CPU
pip install tensorflow
# For GPU
pip install tensorflow-gpu
```

一般下载CPU版本的即可，当前的Demo使用的也是CPU版本。如果需要追求更高的性能，可以选择下载GPU版本，但同时对硬件的要求也更高。

更详细的TensorFlow安装可看教程：[Tensorflow installation instructions](https://www.tensorflow.org/install/)

## 安装 Object Detection API

系统使用了[Tensorflow Object Detection API](https://github.com/tensorflow/models/tree/master/research/object_detection)来进行物体识别，首先请根据[官方安装教程](https://github.com/tensorflow/models/blob/master/research/object_detection/g3doc/installation.md)安装各种依赖库。安装过程中，请注意依赖库的版本。

然后使用`git`方法把Github上的项目`clone`到本地，这里建议选择下载Tensorflow的models仓库：

```shell
git clone https://github.com/tensorflow/models
```

进入 models/research/ 文件夹，编译API代码：

```shell
# From models/research/
protoc object_detection/protos/*.proto --python_out=.
```

设置路径和验证是否安装成功的方法可看教程。

## 安装 Flask 和 OpenCV

Flask是前端框架，用于图像物体识别Demo使用。OpenCV则是一个图像处理库，用于处理图像和视频数据。

```shell
pip install flask
pip install opencv-python
```

## 安装其他图像处理库

在编译代码过程可能会出现其他模块缺失的问题，这里只需使用`pip install`直接安装对应库即可。

## 下载 Demo 源码

从Github上下载objectDetectionRobo项目：

```shell
git clone https://github.com/ReganFan/objectDetectionRobo
```

## 编译 Demo 源码 

先开启ROS环境：

```shell
roscore
```

复制objectDetectionRobo项目中的object_detection和video_detection到自己创建的catkin工作空间中的src文件夹，然后执行`catkin_make`编译：

```shell
cd ~/catkin_ws/src    # 定位到自己的workspace
ls
object_detection  video_detection
cd ~/catkin_ws
catkin_make           # 编译
source ~/catkin_ws/devel/setup.bash
```