# read and unzip the .npz annotation file
import os
import numpy as np
import cv2

ann_file = "./annotation/0a0f715b298cc59037ab4f317b97eb7a.jpg.npz"
ann = np.load(ann_file, allow_pickle=True)
ann = dict(ann)['label']
ann = np.clip(ann,1,9)
ann = ann - ann.min()
ann = ann / 1.0 / ann.max() * 255
print(ann.shape)
# use cv2 to write image to file
cv2.imwrite("unziped_annotation.jpg", ann)