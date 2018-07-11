# Imports
import numpy as np
import os
# solve the problem that tensorflow do not support some types of CPU
# you can delete the following sentence if you do not meet this problem
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
import six.moves.urllib as urllib
import sys
import tarfile
import tensorflow as tf
import zipfile

from collections import defaultdict
from io import StringIO
from matplotlib import pyplot as plt
from PIL import Image

# correct the PYTHONPATH for opencv
sys.path.remove('/opt/ros/kinetic/lib/python2.7/dist-packages')
import cv2

# the path that object_detection folder locates, change it when you use it
OBJECT_DETECTION_PATH = "/home/fan/models/research/"
# This is needed since the notebook is stored in the object_detection folder.
sys.path.append(OBJECT_DETECTION_PATH)
#from object_detection.utils import ops as utils_ops

if tf.__version__ < '1.4.0':
  raise ImportError('Please upgrade your tensorflow installation to v1.4.* or later!')

# Env setup
# This is needed to display the images.
#%matplotlib inline

# Object detection imports
from object_detection.utils import label_map_util

from object_detection.utils import visualization_utils as vis_util

# Model preparation
# Variables
# Any model exported using the export_inference_graph.py tool can be loaded here simply by changing PATH_TO_CKPT to point to a new .pb file.
# What model to download.
# you can change the model name to use other models
# such as ssd_inception_v2_coco_2018_01_28, rfcn_resnet101_coco_2018_01_28, faster_rcnn_resnet101_coco_2018_01_28
MODEL_NAME = OBJECT_DETECTION_PATH + 'object_detection/' + 'ssd_mobilenet_v1_coco_2018_01_28'
MODEL_FILE = MODEL_NAME + '.tar.gz'
DOWNLOAD_BASE = 'https://reganfan.github.io/assets/models/'

# Path to frozen detection graph. This is the actual model that is used for the object detection.
PATH_TO_CKPT = MODEL_NAME + '/frozen_inference_graph.pb'

# List of the strings that is used to add correct label for each box.
PATH_TO_LABELS = os.path.join(OBJECT_DETECTION_PATH + 'object_detection/data', 'mscoco_label_map.pbtxt')

NUM_CLASSES = 90

# Download Model
# if you have downloaded a model, you do not need to download it again
#opener = urllib.request.URLopener()
#opener.retrieve(DOWNLOAD_BASE + MODEL_FILE, MODEL_FILE)
#tar_file = tarfile.open(MODEL_FILE)
#for file in tar_file.getmembers():
#  file_name = os.path.basename(file.name)
#  if 'frozen_inference_graph.pb' in file_name:
#    tar_file.extract(file, os.getcwd())

# Load a (frozen) Tensorflow model into memory
detection_graph = tf.Graph()
with detection_graph.as_default():
  od_graph_def = tf.GraphDef()
  with tf.gfile.GFile(PATH_TO_CKPT, 'rb') as fid:
    serialized_graph = fid.read()
    od_graph_def.ParseFromString(serialized_graph)
    tf.import_graph_def(od_graph_def, name='')

# Loading label map
label_map = label_map_util.load_labelmap(PATH_TO_LABELS)
categories = label_map_util.convert_label_map_to_categories(label_map, max_num_classes=NUM_CLASSES, use_display_name=True)
category_index = label_map_util.create_category_index(categories)

# Helper code
def load_image_into_numpy_array(image):
  (im_width, im_height) = image.size
  return np.array(image.getdata()).reshape(
      (im_height, im_width, 3)).astype(np.uint8)

# Detection
# For the sake of simplicity we will use only 2 images:
# image1.jpg
# image2.jpg
# If you want to test the code with your images, just add path to the images to the TEST_IMAGE_PATHS.
#PATH_TO_TEST_IMAGES_DIR = 'my_test_images'
#TEST_IMAGE_PATHS = [ os.path.join(PATH_TO_TEST_IMAGES_DIR, 'image{}.jpg'.format(i)) for i in range(1, 3) ]

# Size, in inches, of the output images.
IMAGE_SIZE = (12, 8)

'''
with detection_graph.as_default():
  with tf.Session(graph=detection_graph) as sess:
    for image_path in TEST_IMAGE_PATHS:
      image = Image.open(image_path)
      # the array based representation of the image will be used later in order to prepare the
      # result image with boxes and labels on it.
      image_np = load_image_into_numpy_array(image)
      # Expand dimensions since the model expects images to have shape: [1, None, None, 3]
      image_np_expanded = np.expand_dims(image_np, axis=0)
      image_tensor = detection_graph.get_tensor_by_name('image_tensor:0')
      # Each box represents a part of the image where a particular object was detected.
      boxes = detection_graph.get_tensor_by_name('detection_boxes:0')
      # Each score represent how level of confidence for each of the objects.
      # Score is shown on the result image, together with the class label.
      scores = detection_graph.get_tensor_by_name('detection_scores:0')
      classes = detection_graph.get_tensor_by_name('detection_classes:0')
      num_detections = detection_graph.get_tensor_by_name('num_detections:0')
      # Actual detection.
      (boxes, scores, classes, num_detections) = sess.run(
          [boxes, scores, classes, num_detections],
          feed_dict={image_tensor: image_np_expanded})
      # Visualization of the results of a detection.
      vis_util.visualize_boxes_and_labels_on_image_array(
          image_np,
          np.squeeze(boxes),
          np.squeeze(classes).astype(np.int32),
          np.squeeze(scores),
          category_index,
          use_normalized_coordinates=True,
          line_thickness=8)
      plt.figure(figsize=IMAGE_SIZE)
      plt.imshow(image_np)
      plt.imshow(image)  # display pic
      plt.imshow(image_np)
      # plt.axis('off')  # do not display axis
      plt.show()
'''

# Video Detection 
import pylab
import imageio
import skimage.io
imageio.plugins.ffmpeg.download()

from moviepy.editor import VideoFileClip
from IPython.display import HTML

def detect_objects(image_np, sess, detection_graph):
    # Expand dimensions since the model expects images to have shape: [1, None, None, 3]
    image_np_expanded = np.expand_dims(image_np, axis=0)
    image_tensor = detection_graph.get_tensor_by_name('image_tensor:0')

    # Each box represents a part of the image where a particular object was detected.
    boxes = detection_graph.get_tensor_by_name('detection_boxes:0')

    # Each score represent how level of confidence for each of the objects.
    # Score is shown on the result image, together with the class label.
    scores = detection_graph.get_tensor_by_name('detection_scores:0')
    classes = detection_graph.get_tensor_by_name('detection_classes:0')
    num_detections = detection_graph.get_tensor_by_name('num_detections:0')

    # Actual detection.
    (boxes, scores, classes, num_detections) = sess.run(
        [boxes, scores, classes, num_detections],
        feed_dict={image_tensor: image_np_expanded})
    # Visualization of the results of a detection.
    vis_util.visualize_boxes_and_labels_on_image_array(
        image_np,
        np.squeeze(boxes),
        np.squeeze(classes).astype(np.int32),
        np.squeeze(scores),
        category_index,
        use_normalized_coordinates=True,
        line_thickness=8)
    return image_np

def process_image(image):
    # NOTE: The output you return should be a color image (3 channel) for processing video below
    # you should return the final output (image with lines are drawn on lanes)
    with detection_graph.as_default():
        with tf.Session(graph=detection_graph) as sess:
            image_process = detect_objects(image, sess, detection_graph)
            return image_process

'''
white_output = 'my_test_videos/video1_out.mp4'
clip1 = VideoFileClip("my_test_videos/video1.mp4").subclip(0,3)
white_clip = clip1.fl_image(process_image) #NOTE: this function expects color images!!s
#%time 
white_clip.write_videofile(white_output, audio=False)

# show result
cap = cv2.VideoCapture('my_test_videos/video1_out.mp4')

while(cap.isOpened()):
  ret, frame = cap.read()
  cv2.imshow("capture", frame)
  k = cv2.waitKey(20)
  if (k & 0xFF == ord('q')):
    break

cap.release()
cv2.destoryAllWindows()
'''

IF_DETECTION = 0

def video_detect():
  white_output = 'my_test_videos/video1_out.mp4'
  clip1 = VideoFileClip("my_test_videos/video1.mp4")
  white_clip = clip1.fl_image(process_image) #NOTE: this function expects color images!!s
  #%time 
  white_clip.write_videofile(white_output, audio=False)

  # show result
  cap = cv2.VideoCapture('my_test_videos/video1_out.mp4')
  while(cap.isOpened()):
    ret, frame = cap.read()
    if ret==True:
        # do flipping 
        #frame = cv2.flip(frame, 1)

        cv2.imshow('output', frame)
        if cv2.waitKey(25) & 0xFF == ord('q'):
          IF_DETECTION = 1
          break
    else:
        IF_DETECTION = 1
        break

  cap.release()
  cv2.destroyAllWindows()

  if IF_DETECTION == 1:
    IF_DETECTION = 0
    message = "FinishDetection"
  else:
    message = "DetectionError"
  
  return message

if __name__ == '__main__':
  res = video_detect()
  print(res)
