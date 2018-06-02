# MnistCNN

## 環境設定

- [下載 ffmpeg](https://www.ffmpeg.org/download.html)
- [下載並安裝 Anaconda](https://www.anaconda.com/download/)，選擇搭配 Python 3.6 的版本


### Windows 環境

Wndows 需下載 ffmpeg ，解壓縮到資料夾後，該資料夾加入 PATH

加入 PATH 請參考下方步驟：
- 在 `電腦` 或 `本機` 上點 `右鍵` 選擇 `內容`
- 點開左邊的 `進階系統設定` ，展開 `進階` 分頁
- 點擊 `環境變數`
- 如果出現清單，將 `ffmpeg.exe` 的所在路徑加入；如果沒出現清單請用 `;` 隔開原本的內容，將 `ffmpeg` 所在路徑附加上去

設定後後請開啟新的終端機環境確認可以輸入 `ffmpeg -version` 可以正確顯示套件版本。

Conda 環境初始化
```cmd
conda env --name myname python=3.6 anaconda
activate  myname
```

提示符號會變成
```cmd
(myname) 當前路徑>
```

進入環境後，請輸入下面指令將 cmd 切換為 Unicode 編碼（不然亂碼等著你）
```bash
chcp 65001
```

### Linux 環境

非 Linux 可以透過套件管理程式安裝 `ffmpeg` 套件，指令如下

```bash
# ArchLinux
sudo pacman -Syu ffmpeg

# Debian / Ubuntu 與其他使用 apt 的 Linux
sudo apt-get install ffmpeg

# Red Hat Entprise Linux / CentOS 與其他使用 yum 的 Linux
sudo yum install ffmpeg
```

安裝後請確認可以在終端機可以輸入 `ffmpeg --version` 可以正確顯示套件版本。

Anaconda 安裝完成後會提示是否要將初始環境變數的指令加入 `~/.bashrc` ，如果不使用 bash 需將下面指令加入對應的環境檔案。
```bash
export PATH=/home/dd-han/anaconda3/bin:$PATH
```

手動或加入後，需執行 `source ~/.bashrc` 或 `source ~/.zshrc` 更新環境變數（或是關閉終端機重開）。

更新後環境變數，執行以下指令確保 Python 從 Anaconda 而不是從系統來：

```bash
which python
```

### 共通步驟

啟用 Anaconda 環境後，還需要設定 Anaconda 環境的 python 套件

更新 pip

```bash
python -m pip install msgpack
python -m pip install --upgrade pip
```

安裝套件

```bash
pip install tensorflow keras h5py
```

## Jupyter 使用說明

Jupyter 是一個方便的 GUI 工具可以進行 Python Debug 與開發。

Repo 中， image 資料夾內圖片為 GENYAPIUS 並處理為灰階的一張圖片。(?

要使用 jupyter notebook 開啟程式碼，輸入 `jupyter notebook` 就會開啟網頁

網頁開啟後點選 `mnistCNN.ipynb`

一格稱為一個 Cell，Ctrl+Enter為執行該Cell。

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

## capture 使用說明

dd-han 表示他懶得寫註解，以下直接上 Sample
```python
from capture import Capture
import os

def job(self, image_object):
  gray_file = os.path.join(self.temp_dir, "gray.jpg")
  image_object.save(gray_file)
  self.open_image(gray_file)

capture = Capture()
print(capture.platform)
print(capture.temp_dir)

capture.set_camera()
print(capture.ffmpeg_command)

capture.set_crop()
print(capture.crop)

capture.timer(job, delay_time=0, count=None)
```