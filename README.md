# MnistCNN

## 環境設定

[下載 imagemagick](http://www.imagemagick.org/script/download.php)
[下載 ffmpeg](https://www.ffmpeg.org/download.html)
[下載並安裝 Anaconda](https://www.anaconda.com/download/)，選擇搭配 Python 3.6 的版本


### Windows 環境

如果是 Windows 使用者需要設定 conda 環境
```cmd
conda --name myname python=3.6 anaconda
activate  myname
```

提示符號會變成
```cmd
(myname) 當前路徑>
```


### Linux 環境

非 Linux 可以透過套件管理程式安裝 `imagemagic` 與 `ffmpeg` 套件，指令如下

```bash
# ArchLinux
sudo pacman -Syu imagemagic ffmpeg

# Debian / Ubuntu 與其他使用 apt 的 Linux
sudo apt-get install imagemagic ffmpeg

# Red Hat Entprise Linux / CentOS 與其他使用 yum 的 Linux
sudo yum install imagemagic ffmpeg
```

安裝後請確認可以在終端機可以輸入 `ffmpeg --version` 與 `magick --version` 可以正確顯示套件版本。

如果是非 Windows 使用者，安裝完成後會提示是否要將初始環境變數的指令加入 `~/.bashrc` ，如果不使用 bash 需字型調整下面指令
```bash
export PATH=/home/dd-han/anaconda3/bin:$PATH
```

加入後，需執行 `source ~/.bashrc` 或 `source ~/.zshrc` 啟用環境變數。

完成後，執行以下指令確保 Python 從 Anaconda 來：

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
