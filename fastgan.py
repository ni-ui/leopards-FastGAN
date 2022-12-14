# -*- coding: utf-8 -*-
"""FastGAN

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1lMsOLMU8H0bq-M8YWDz8hUQ25RljQPkl
"""

!git clone https://github.com/odegeasslbc/FastGAN-pytorch.git

from __future__ import print_function
#%matplotlib inline
import argparse
import cv2
import glob
from google.colab.patches import cv2_imshow
import os
import random
import numpy as np
from IPython.display import HTML

#LINK FOR BACKGROUND IMAGES

#https://drive.google.com/drive/folders/1HqUJ0UMOelk1jokhCYs3cFvbbFWB3PP-?usp=sharing

#LINK FOR LEOPARD IMAGES WITH BACKGROUNDS REMOVED

#https://drive.google.com/drive/folders/1EYrLJA4Z1v0nclAMTYrlY_Dec7k4OttU?usp=share_link

#CODE FOR GENERATING OVERLAYS

background_imgs = glob.glob('/content/drive/MyDrive/backgrounds/*')
overlays =  glob.glob('/content/drive/MyDrive/Leopard_bg_remove/*')
print(len(overlays))

for idx in range(len(overlays)):
  for k in range(len(background_imgs)):

    background = cv2.imread(background_imgs[k])
    foreground = cv2.imread(overlays[idx], cv2.IMREAD_UNCHANGED)

    background  = cv2.resize(background, dsize=(256,256))
    foreground  = cv2.resize(foreground, dsize=(256,256))

    alpha_channel = foreground[:, :, 3] / 255 # convert from 0-255 to 0.0-1.0
    overlay_colors = foreground[:, :, :3]

    alpha_mask = np.dstack((alpha_channel, alpha_channel, alpha_channel))

    h, w = foreground.shape[:2]
    background_subsection = background[0:h, 0:w]

    added_image = background_subsection * (1 - alpha_mask) + overlay_colors * alpha_mask
    background[0:h, 0:w] = added_image

  # display the image
    cv2.imwrite('/content/drive/My Drive/leopard_overlays/'+str(idx)+"_"+str(k)+".png" , background)

import glob
imgs = glob.glob('/content/drive/MyDrive/leopard_overlays/*')
print(len(imgs))

!ls '/content/FastGAN-pytorch'

!python '/content/FastGAN-pytorch/train.py' --path '/content/drive/MyDrive/leopard_overlays' --im_size 256 --iter 2000

