#!/usr/bin/env python
# -*- encoding: utf-8 -*-
import os
import numpy as np
import pandas as pd

from keras.models import Sequential, load_model 
from keras.layers import Dense, Dropout, Flatten, Conv2D, MaxPooling2D
from keras.utils import np_utils

from PIL import Image
from capture import Capture

# 從 HDF5 檔案中載入模型
model = load_model("mnistCNN.h5")

#顯示模型
print(model.summary())

## 初始化 capture 物件
capture = Capture()

capture.set_camera()
while True:
    capture.set_crop()

    while True:
        img_file = capture.shot()
        print("image file: %s" % img_file)

        x_Test = np.empty((1, 1, 28, 28), dtype="float32")

        with Image.open(img_file) as img:
            arr = np.asarray(img, dtype="float32")
            x_Test[0, :, :, :] = arr
            x_Test = x_Test.reshape(1, 28, 28, 1)

            x_Test4D = x_Test.reshape(x_Test.shape[0], 28, 28, 1).astype('float32')

            x_Test4D_normalize = x_Test4D / 255

            prediction = model.predict_classes(x_Test4D_normalize)

            print(prediction[0])

            if input("Continue prediction (Y/n) ?").upper() == "N":
                break
if input("reCaptrue (Y/n)?").upper() == "N":
    break
