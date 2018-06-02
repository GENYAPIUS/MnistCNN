import tensorflow as tf
import numpy as np
from keras.models import Sequential, load_model
from keras.layers import Dense, Dropout, Flatten, Conv2D, MaxPooling2D
from keras.utils import np_utils


# 從 HDF5 檔案中載入模型
model = load_model("MnistCNN.h5")

# 驗證模型
score = model.evaluate(x_test, y_test, verbose=0)

# 輸出結果
print('Test loss:', score[0])
print('Test accuracy:', score[1])
