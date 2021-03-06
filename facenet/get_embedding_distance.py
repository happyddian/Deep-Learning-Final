# -*- coding: utf-8 -*-

import tensorflow as tf
import numpy as np
import scipy.misc
import cv2
import facenet
import imageio

image_size = 160 #don't need equal to real image size, but this value should not small than this
modeldir = '/content/facenet_distance/model_check_point/20180402-114759.pb' #change to your model dir
print('建立facenet embedding模型')
tf.Graph().as_default()
sess = tf.compat.v1.Session()

facenet.load_model(modeldir)
images_placeholder = tf.compat.v1.get_default_graph().get_tensor_by_name("input:0")
embeddings = tf.compat.v1.get_default_graph().get_tensor_by_name("embeddings:0")
phase_train_placeholder = tf.compat.v1.get_default_graph().get_tensor_by_name("phase_train:0")
embedding_size = embeddings.get_shape()[1]
dist = []
print('facenet embedding模型建立完毕')
for i in range(200):
  s = str(i)
  if len(s)==1:
    s = "000"+s
  elif len(s)==2:
    s = "00"+s
  else:
    s = "0"+s 
  image_name1 = '/content/drive/MyDrive/DL_final/with_mask/with-mask-default-mask-seed'+s+".png" #change to your image name
  image_name2 = '/content/drive/MyDrive/DL_final/without_mask/seed'+s+".png" #change to your image name
  scaled_reshape = []

  image1 = imageio.imread(image_name1, pilmode='RGB')
  image1 = cv2.resize(image1, (image_size, image_size), interpolation=cv2.INTER_CUBIC)
  image1 = facenet.prewhiten(image1)
  scaled_reshape.append(image1.reshape(-1,image_size,image_size,3))
  emb_array1 = np.zeros((1, embedding_size))
  emb_array1[0, :] = sess.run(embeddings, feed_dict={images_placeholder: scaled_reshape[0], phase_train_placeholder: False })[0]

  image2 = imageio.imread(image_name2, pilmode='RGB')
  image2 = cv2.resize(image2, (image_size, image_size), interpolation=cv2.INTER_CUBIC)
  image2 = facenet.prewhiten(image2)
  scaled_reshape.append(image2.reshape(-1,image_size,image_size,3))
  emb_array2 = np.zeros((1, embedding_size))
  emb_array2[0, :] = sess.run(embeddings, feed_dict={images_placeholder: scaled_reshape[1], phase_train_placeholder: False })[0]

  dist.append(np.sqrt(np.sum(np.square(emb_array1[0]-emb_array2[0]))))
  print(i)
  # print("128维特征向量的欧氏距离：%f "%dist)
print(np.average(dist))