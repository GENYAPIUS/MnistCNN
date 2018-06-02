from keras.models import Sequential, load_model
from keras.layers import Dense, Dropout, Flatten, Conv2D, MaxPooling2D
from keras.utils import np_utils
import numpy as np

# 從 HDF5 檔案中載入模型
model = load_model("MnistCNN.h5")

#顯示模型
print(model.summary())
