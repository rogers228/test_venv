# 說明

本專案為venv的測試

## 檔案說明

|檔案|說明|
|:--|:--|
|run.bat          | 快速以虛擬環境執行main.py             |
|run_venv.bat     | 快速以虛擬環境啟動cmd視窗，等待後續命令 |
|requirements.txt | 記得要導出，以利其他環境安裝套件        |


# 常用命令

## 啟動
```
cd /d C:\Users\USER\Documents\test_venv
venv\Scripts\activate.bat   啟動
venv\Scripts\deactivate.bat  退出
```

## 導出 requirements.txt
```
python -m pip freeze > requirements.txt    導出
python -m pip install -r requirements.txt  安裝
```