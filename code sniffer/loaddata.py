import os
from PIL import Image
import numpy as np

def load_data():
    data = np.empty((42000, 1, 28, 28), dtype="float32")
    label = np.empty((42000,), dtype="uint8")

    imgs = os.listdir("d:/mnist")
    num = len(imgs)
    for i in range(num):
        img = Image.open("d:/mnist/"+imgs[i])
        arr = np.asarray(img, dtype="float32")
        data[i, :, :, :] = arr
        label[i] = int(imgs[i].split('.')[0])
    data = data.reshape(42000, 28, 28, 1)
    return data, label


data, label = load_data()
