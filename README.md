# MnistCNN
安裝Anaconda：https://www.anaconda.com/download/

github內，image資料夾內圖片為我自己拍並處理為灰階的一張圖片。(?

在一個自己爽就好的地方創目錄，使用cmd進入該目錄後輸入指令，myname為自訂名字：
conda --name myname python=3.6 anaconda

等他創建完成後輸入
activate  myname

會變為
(myname) 當前路徑>

先更新pip
python -m pip install --upgrade pip

安裝tensorflow
pip install tensorflow

安裝keras
pip install keras

安裝h5py
pip insyall h5py

要使用jupyter notebook開啟程式碼，輸入jupyter notebook就會開啟網頁；網頁開啟後點選mnistCNN.ipynb

一格稱為一個Cell，Ctrl+Enter為執行該Cell。

第一個Cell為讀取模組。

第二個Cell為load_data Function，包括圖片維度化以及上label
圖片路徑為imgs = os.listdir("d:/school/image")這一行。

np.empty((1, 1, 28, 28), dtype="float32")
label = np.empty((1,), dtype="uint8")
data = data.reshape(1, 28, 28, 1)
這三行第一個1為資料夾內圖片數目，須依情況更改。

因預測範圍只有0~9之手寫數字，檔案名稱格式為 數字.第幾張.jpg 
例：0.1.jpg為數字0、第1張圖片
另外請注意別讓資料夾內有除了jpg檔以外的檔案，否則會出錯。

第三個Cell為使用load_data Function讀取圖片並將維度標準化。

第四個Cell為在使用完第三個Cell後使用標準化的測驗資料進行預測。

第五個Cell為以混淆矩陣顯示預測結果，橫排predict為預測值、直排label為實際值。

