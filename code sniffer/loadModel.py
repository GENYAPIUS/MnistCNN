# 從 HDF5 檔案中載入模型
model = tf.contrib.keras.models.load_model('my_model.h5')

# 驗證模型
score = model.evaluate(x_test, y_test, verbose=0)

# 輸出結果
print('Test loss:', score[0])
print('Test accuracy:', score[1])