---
title: Day03 - pycharm，註解，PEP8規範，變量與常量，基本數據類型int、float、str、list、dict(初探)，練習題(數據類型)
description: 
slug: python-self-learning-day03
date: 2023-10-07 03:00:00+0800
image: 
categories:
  - python
tags:
  - python
  - pycharm
weight: 1
---


# 今日内容概要
- pycharm下載與使用
	- MAC版安裝
	- WINDOWS版安裝
- python語法之注釋
- PEP8規範
- python語法之變數與常量
- python基本數據類型(先大致了解有哪些)
	- 整型int
	- 浮點型float
	- 字串str
	- 列表list
	- 字典dict
- 練習題(數據類型)

```python
# 整體內容大綱
pycharm下載與使用
    MAC版安裝：
    windows版安裝：
    回到我的MAC電腦，創建項目
        1. 處建項目
        2. Location要填寫、解釋器選擇，先不要用虛擬環境
        3. 儲存python代碼的文件後綴名一般叫.py
        4. 使用pycharm創建的py文件在編寫程式碼的時候有自動提示 tab補全 方向鍵選擇
        5. 配置調整
        6.運行python代碼
python語法之注釋
PEP8規範
變數與常量
變數的基本使用
    1. 日常生活中的變數案例
    2. 變數使用的語法結構與底層原理
    3. 變數名的命名規範
    4. 變數名的命名風格
常量的基本使用
數據類型
數據類型之整型int
數據類型之浮點型float
數據類型之字串str
    1.定義字串有四種方式
數據類型之列表list
數據類型之字典dict
小結 今日PEP8規範
練習題

```




### pycharm下載與使用

```python
1.該軟體分為收費版和免費版
  免費版功能太少(community) 我們盡量使用收費版(professional) 30天試用
2.pycharm比較笨重
  本身占據的資源較多 並且保持運行的情況下需要消耗計算機1GB多的資源
3.文件後綴名
  儲存python代碼的文件後綴名一般叫.py
4.如何創建py文件
  使用pycharm創建的py文件在編寫程式碼的時候有自動提示 tab補全 方向鍵選擇
5.配置調整
  字體大小
  編程背景
  解釋器選擇
6.運行python代碼
```

Pycharm官網下載網址：
https://www.jetbrains.com/pycharm/download/?section=mac

#### MAC版安裝：
下載最新版Pycharm
![https://ithelp.ithome.com.tw/upload/images/20230916/20132481jHMxC9Sxc9.png](https://ithelp.ithome.com.tw/upload/images/20230916/20132481jHMxC9Sxc9.png)

下載其他版本，我電腦是mac m1晶片
![https://ithelp.ithome.com.tw/upload/images/20230916/20132481b3mJVujroH.png](https://ithelp.ithome.com.tw/upload/images/20230916/20132481b3mJVujroH.png)

拖曳過去Applications檔案夾即可
![https://ithelp.ithome.com.tw/upload/images/20230916/20132481JodobzlU6q.png](https://ithelp.ithome.com.tw/upload/images/20230916/20132481JodobzlU6q.png)

需要licenses授權，因為我是有購買的，所以我採取登入JB帳號，即可使用
![https://ithelp.ithome.com.tw/upload/images/20230916/20132481MNpYFmG0Db.png](https://ithelp.ithome.com.tw/upload/images/20230916/20132481MNpYFmG0Db.png)

#### windows版安裝：
Next
![https://ithelp.ithome.com.tw/upload/images/20230916/20132481beORdhOGFq.png](https://ithelp.ithome.com.tw/upload/images/20230916/20132481beORdhOGFq.png)

目錄選擇簡單一點的名稱，方便後續查找
![https://ithelp.ithome.com.tw/upload/images/20230916/20132481YlDMszlBcn.png](https://ithelp.ithome.com.tw/upload/images/20230916/20132481YlDMszlBcn.png)

安裝後，桌面會一個PyCharm的icon捷徑
![https://ithelp.ithome.com.tw/upload/images/20230916/20132481JFXQDhopa8.png](https://ithelp.ithome.com.tw/upload/images/20230916/20132481JFXQDhopa8.png)

#### 回到我的MAC電腦，創建項目

##### 1. 處建項目
![https://ithelp.ithome.com.tw/upload/images/20230916/20132481a8M6SCQhSf.png](https://ithelp.ithome.com.tw/upload/images/20230916/20132481a8M6SCQhSf.png)

##### 2. Location要填寫、解釋器選擇，先不要用虛擬環境
![https://ithelp.ithome.com.tw/upload/images/20230916/20132481G2AyFwQPZh.png](https://ithelp.ithome.com.tw/upload/images/20230916/20132481G2AyFwQPZh.png)

##### 3. 儲存python代碼的文件後綴名一般叫.py

![https://ithelp.ithome.com.tw/upload/images/20230916/2013248193Hq5yFPpg.png](https://ithelp.ithome.com.tw/upload/images/20230916/2013248193Hq5yFPpg.png)

![https://ithelp.ithome.com.tw/upload/images/20230916/20132481bIgMKnOZtX.png](https://ithelp.ithome.com.tw/upload/images/20230916/20132481bIgMKnOZtX.png)

項目創建的資料，就會看到上面創建的.py文件
![https://ithelp.ithome.com.tw/upload/images/20230916/20132481KhTkwcjYSy.png](https://ithelp.ithome.com.tw/upload/images/20230916/20132481KhTkwcjYSy.png)
##### 4. 使用pycharm創建的py文件在編寫程式碼的時候有自動提示 tab補全 方向鍵選擇
![https://ithelp.ithome.com.tw/upload/images/20230916/20132481uxHGEjr5gl.png](https://ithelp.ithome.com.tw/upload/images/20230916/20132481uxHGEjr5gl.png)

##### 5. 配置調整
![https://ithelp.ithome.com.tw/upload/images/20230916/2013248176ZUTEGxB7.png](https://ithelp.ithome.com.tw/upload/images/20230916/2013248176ZUTEGxB7.png)

字體
![https://ithelp.ithome.com.tw/upload/images/20230916/20132481mUSWuhh2lg.png](https://ithelp.ithome.com.tw/upload/images/20230916/20132481mUSWuhh2lg.png)

背景，我習慣用白的，這裡再依各位個人喜好去修改
![https://ithelp.ithome.com.tw/upload/images/20230916/20132481qNMwDfc2Gg.png](https://ithelp.ithome.com.tw/upload/images/20230916/20132481qNMwDfc2Gg.png)

可以看到選擇Darcula，視窗就變暗色系了
![https://ithelp.ithome.com.tw/upload/images/20230916/20132481atQeLJY1Fm.png](https://ithelp.ithome.com.tw/upload/images/20230916/20132481atQeLJY1Fm.png)

如果pycharm無法找到python解釋器，可以再來這裡再設定
![https://ithelp.ithome.com.tw/upload/images/20230916/201324819cPDx76gio.png](https://ithelp.ithome.com.tw/upload/images/20230916/201324819cPDx76gio.png)

有新安裝版本，也能從旁右方齒輪按鍵，去新增
![https://ithelp.ithome.com.tw/upload/images/20230916/20132481Clm05y3Tkc.png](https://ithelp.ithome.com.tw/upload/images/20230916/20132481Clm05y3Tkc.png)

##### 6.運行python代碼
代碼行處，右鍵，即可執行此當下這個.py文件代碼
![https://ithelp.ithome.com.tw/upload/images/20230916/20132481YZKDpusEEK.png](https://ithelp.ithome.com.tw/upload/images/20230916/20132481YZKDpusEEK.png)

或者視窗右上面，也能執行
![https://ithelp.ithome.com.tw/upload/images/20230916/20132481rO1yQSlC9P.png](https://ithelp.ithome.com.tw/upload/images/20230916/20132481rO1yQSlC9P.png)

### python語法之注釋
```python
1.什麼是注釋
  注釋其實就是對一段代碼的解釋說明
2.如何編寫注釋
  方式1:解釋說明文字前加警號   pycharm中有快捷鍵 ctrl + / mac電腦，用 command + /
        # 注釋(單行注釋)  
  方式2:鍵盤enter鍵左邊那個鍵英文輸入法下連續按三下
         '''
         多行注釋
         '''
  方式3:鍵盤enter鍵左邊那個鍵英文輸入法下+shift 連續按三下
         """
         多行注釋
         """
```


```python
print('hello world')  #1. 這是列印數據方式，單行註釋  
# print('hello world') # Prcharm快捷鍵，command + /(右邊shift左邊那個鍵)  

'''  
2. 多行註釋:  
大家好，我是翻轉吧金魚腦  
'''  
  
"""  
3. 多行註釋:  
哈摟，我是翻轉吧金魚腦  
"""
```

### PEP8規範

```python
"""
pycharm中很多時候會有各種顏色提示還有波浪線
  只要不是紅線一般都不影響代碼運行
"""
python代碼編寫規範
  1.單行注釋如果跟在代碼之後 那麼警號與代碼之間需要空兩格 內容與警號空一格
  2.如果單行注釋自成一行 那麼內容與警號空一格
ps:如何學習規範 可以借助於pycharm自動化格式程式碼反向學習
```
**``EX1: 單行注釋如果跟在代碼之後 那麼警號與代碼之間需要空兩格 內容與警號空一格``**
![https://ithelp.ithome.com.tw/upload/images/20230916/201324818R0yXdJ2qy.png](https://ithelp.ithome.com.tw/upload/images/20230916/201324818R0yXdJ2qy.png)

![https://ithelp.ithome.com.tw/upload/images/20230916/201324818uUz9fNCgy.png](https://ithelp.ithome.com.tw/upload/images/20230916/201324818uUz9fNCgy.png)

**``EX2: 如果單行注釋自成一行 那麼內容與警號空一格``**
![https://ithelp.ithome.com.tw/upload/images/20230916/201324817kAqHOGaO6.png](https://ithelp.ithome.com.tw/upload/images/20230916/201324817kAqHOGaO6.png)
![https://ithelp.ithome.com.tw/upload/images/20230916/20132481uWlvpQluAk.png](https://ithelp.ithome.com.tw/upload/images/20230916/20132481uWlvpQluAk.png)


**``EX3: 如何學習規範 可以借助於pycharm自動化格式程式碼反向學習``**
![https://ithelp.ithome.com.tw/upload/images/20230916/201324811qduMtokcQ.png](https://ithelp.ithome.com.tw/upload/images/20230916/201324811qduMtokcQ.png)

![https://ithelp.ithome.com.tw/upload/images/20230916/201324810ppTAhFBsw.png](https://ithelp.ithome.com.tw/upload/images/20230916/201324810ppTAhFBsw.png)

![https://ithelp.ithome.com.tw/upload/images/20230916/201324817MWBV5NMs6.png](https://ithelp.ithome.com.tw/upload/images/20230916/201324817MWBV5NMs6.png)

### 變數與常量

```python
變數與常量就是為了讓程序具備人記錄事物狀態的能力
1.什麼是變數?
  記錄變化(可能會經常改變)的事物狀態
    eg:年齡 容貌 薪資
2.什麼是常量?
  記錄固定(可能不經常改變)的事物狀態
      eg:圓周率 重力加速度
```

### 變數的基本使用

```python
日常生活中的變數案例
  翻轉吧金魚腦
    姓名叫jimmy
      年齡是20
      性別是男性
      
代碼中如何記錄事物狀態
  name = 'jimmy'
  age = 20
  gender = 'male'
 
 變數使用的語法結構與底層原理
  """
  name = 'jimmy'
  變數名 賦值符號 數據值
  1.一旦看到賦值符號 那麼一定先看符號的右側
  2.在記憶體空間中申請一塊記憶體空間儲存數據值
  3.給數據值綁定一個變數名
  4.以後就可以通過變數名訪問到數據值
  """
  
  注意事項:
	  1.同一個數據值可以綁定多個變數名
      2.賦值符號也可能是變數名 如果是就先找該變數名綁定的數據值
      3.一個變數名同一時間只能綁定一個數據值
	      name = 'jimmy'
	      name1 = name
	      name2 = name1
	      
	      x = 10
	      x = x + 1
	      print(x)
 
```

#### 1. 日常生活中的變數案例
![https://ithelp.ithome.com.tw/upload/images/20230916/20132481Uzvr5cf1io.png](https://ithelp.ithome.com.tw/upload/images/20230916/20132481Uzvr5cf1io.png)

![https://ithelp.ithome.com.tw/upload/images/20230916/20132481WlmsceNEuR.png](https://ithelp.ithome.com.tw/upload/images/20230916/20132481WlmsceNEuR.png)

#### 2.  變數使用的語法結構與底層原理

```python
  """
  name = 'jimmy'
  變數名 賦值符號 數據值
  1.一旦看到賦值符號 那麼一定先看符號的右側
  2.在記憶體空間中申請一塊記憶體空間儲存數據值
  3.給數據值綁定一個變數名
  4.以後就可以通過變數名訪問到數據值
  """
```

**``EX1: 變數名 賦值符號 數據值``**
![https://ithelp.ithome.com.tw/upload/images/20230916/201324814tQJ0AtQde.png](https://ithelp.ithome.com.tw/upload/images/20230916/201324814tQJ0AtQde.png)
```python
  注意事項:
	  1. 同一個數據值可以綁定多個變數名
      2.賦值符號也可能是變數名 如果是就先找該變數名綁定的數據值
      3.一個變數名同一時間只能綁定一個數據值
```

**``EX1: 一個數據值可以綁定多個變數名(賦值符號也可能是變數名 如果是就先找該變數名綁定的數據值)``**
![https://ithelp.ithome.com.tw/upload/images/20230916/201324810DpWmvlU3V.png](https://ithelp.ithome.com.tw/upload/images/20230916/201324810DpWmvlU3V.png)
**``EX2: 一個變數名同一時間只能綁定一個數據值``**
![https://ithelp.ithome.com.tw/upload/images/20230916/20132481oJfkaOoaOa.png](https://ithelp.ithome.com.tw/upload/images/20230916/20132481oJfkaOoaOa.png)


#### 3. 變數名的命名規範

```python
變數名的命名規範
  1.中文是可以用作變數名的 但是不建議使用 並且容易報錯
  2.變數名只能出現字母、數字、下劃線
  3.數字不能開頭
  4.變數名盡量做到見名知意
  5.變數名不能與關鍵字衝突
```

**``EX1: 中文是可以用作變數名的 但是不建議使用 並且容易報錯``**
![https://ithelp.ithome.com.tw/upload/images/20230916/20132481wGMhsG0ofs.png](https://ithelp.ithome.com.tw/upload/images/20230916/20132481wGMhsG0ofs.png)

![https://ithelp.ithome.com.tw/upload/images/20230916/20132481yfUJgOxbc4.png](https://ithelp.ithome.com.tw/upload/images/20230916/20132481yfUJgOxbc4.png)

**``EX2: 變數名只能出現字母、數字、下劃線、數字不能開頭``**
![https://ithelp.ithome.com.tw/upload/images/20230916/201324812wy2FJw4qC.png](https://ithelp.ithome.com.tw/upload/images/20230916/201324812wy2FJw4qC.png)

**``EX3: 見名之意 ``**
![https://ithelp.ithome.com.tw/upload/images/20230916/20132481cbvhLeBjuE.png](https://ithelp.ithome.com.tw/upload/images/20230916/20132481cbvhLeBjuE.png)

**``EX4: 關鍵字``**
![https://ithelp.ithome.com.tw/upload/images/20230916/20132481cFujswvc4n.png](https://ithelp.ithome.com.tw/upload/images/20230916/20132481cFujswvc4n.png)


#### 4. 變數名的命名風格

```python
變數名的命名風格
  1.下劃線式    python推薦使用
    變數名中單字很多 彼此使用下劃線隔開
      name_from_mysql_db1_userinfo = 'jimmy'
  2.駝峰體式    JS推薦使用
      大駝峰
        NameFromMysqlDb1Userinfo = 'jimmy'
      小駝峰
        nameFromMysqlDb1Userinfo = 'jimmy'
  ps:在同一個程式語言中盡量固定使用一種 不要隨意切換
```

**``EX1: 下劃線式 (變數名中單字很多 彼此使用下劃線隔開)``**

![https://ithelp.ithome.com.tw/upload/images/20230916/20132481hkhaKSLRqx.png](https://ithelp.ithome.com.tw/upload/images/20230916/20132481hkhaKSLRqx.png)

### 常量的基本使用

```python
1.在python沒有真正意義上的常量(定義了就不能改) 定義了可以隨時修改
2.在python中如果想表示出常量 那麼可以使用全大寫的變數名
  HOST = '127.0.0.1'
ps:除了全大寫之外 其他與變數用法一致
```

![https://ithelp.ithome.com.tw/upload/images/20230916/20132481LhJDVnqr2N.png](https://ithelp.ithome.com.tw/upload/images/20230916/20132481LhJDVnqr2N.png)
![https://ithelp.ithome.com.tw/upload/images/20230916/20132481htiFUXUnWY.png](https://ithelp.ithome.com.tw/upload/images/20230916/20132481htiFUXUnWY.png)


### 數據類型

```python
1.什麼是數據類型
  在日常生活中數據的表現形式多種多樣 在程序中也是如此
2.為何學習數據類型
  針對不同的數據採用最佳的數據類型來表示出該數據的價值
3.本次學習數據類型僅僅是了解
  只要看到每個數據類型能夠叫出它們的名字以及代碼如何編寫即可
4.學前必會
  如何查看數據值的數據類型
      type(數據值)\type(變數名)
```

**``EX1: ``**

![https://ithelp.ithome.com.tw/upload/images/20230916/20132481ykVbo5EJLi.png](https://ithelp.ithome.com.tw/upload/images/20230916/20132481ykVbo5EJLi.png)

### 數據類型之整型int

```python
大白話的意思其實就是整數
應用場景:年齡 班級人數 年份
```

**``EX1:``**
![https://ithelp.ithome.com.tw/upload/images/20230916/20132481MAkMG50Ua2.png](https://ithelp.ithome.com.tw/upload/images/20230916/20132481MAkMG50Ua2.png)

![https://ithelp.ithome.com.tw/upload/images/20230916/20132481qbEse25PFw.png](https://ithelp.ithome.com.tw/upload/images/20230916/20132481qbEse25PFw.png)

### 數據類型之浮點型float

```python
大白話的意思其實就是小數
應用場景:身高 體重 薪資
```

**``EX1:``**
![https://ithelp.ithome.com.tw/upload/images/20230916/20132481d7OY4Wsja0.png](https://ithelp.ithome.com.tw/upload/images/20230916/20132481d7OY4Wsja0.png)

![https://ithelp.ithome.com.tw/upload/images/20230916/20132481gbzFuBRKCG.png](https://ithelp.ithome.com.tw/upload/images/20230916/20132481gbzFuBRKCG.png)

### 數據類型之字串str

```python
大白話的意思其實就是文本類型的數據>>>:引號引起來的部分都是字串
應用場景:姓名 地址 愛好
1.定義字串有四種方式
  name = 'jimmy'
  name1 = "jimmy"
  name2 = '''jimmy'''
  name3 = """jimmy"""
2.為什麼定義字串需要有多種方式
  我們在字串中編寫文本也可能會使用到引號 為了避免衝突 有了多種方式
  info = "jimmy說:'好學'"
3.如何區分三引號是字串還是注釋
  關注左側是否含有賦值符號和變數名 如果有則為字串 沒有則為注釋
```

**``EX1:``**
![https://ithelp.ithome.com.tw/upload/images/20230916/20132481JpAuNseOuw.png](https://ithelp.ithome.com.tw/upload/images/20230916/20132481JpAuNseOuw.png)

![https://ithelp.ithome.com.tw/upload/images/20230916/20132481AmriHTCGrm.png](https://ithelp.ithome.com.tw/upload/images/20230916/20132481AmriHTCGrm.png)

#### 1.定義字串有四種方式
```python
1.定義字串有四種方式
  name = 'jimmy'
  name1 = "jimmy"
  name2 = '''jimmy'''
  name3 = """jimmy"""
2.為什麼定義字串需要有多種方式
  我們在字串中編寫文本也可能會使用到引號 為了避免衝突 有了多種方式
  info = "jimmy說：'好學'"
3.如何區分三引號是字串還是注釋
  關注左側是否含有賦值符號和變數名 如果有則為字串 沒有則為注釋
```

**``EX1:``** 
![https://ithelp.ithome.com.tw/upload/images/20230916/2013248168cjHdewDQ.png](https://ithelp.ithome.com.tw/upload/images/20230916/2013248168cjHdewDQ.png)

**``EX2: 為什麼定義字串需要有多種方式(為了避免衝突)``**
![https://ithelp.ithome.com.tw/upload/images/20230916/20132481eW3QBenJiO.png](https://ithelp.ithome.com.tw/upload/images/20230916/20132481eW3QBenJiO.png)

### 數據類型之列表list

```python
大白話的意思其實就是可以儲存多個數據值的類型 並且可以非常方便的取
應用場景:儲存多個數據值 並且將來可能需要單獨取其中一些
代碼實現:
    name_list = ['jimmy', 'tony', 'kevin', 'oscar', 'jerry']
1.列表的文字描述
  中括號括起來 內部可以存放多個數據值 數據值與數據值之間逗號隔開 數據值可以是任意數據類型
    l1 = [11, 11.11, 'jimmy',[11, 22]]
2.索引取值
  起始數字是從0開始 
    l1[索引值]
   
"""
PEP8規範補充
  1.逗號後面與數據值空一格
  2.賦值符號左右都得空一格
"""
```


**``EX1:``**
![https://ithelp.ithome.com.tw/upload/images/20230916/201324814hopyTagwk.png](https://ithelp.ithome.com.tw/upload/images/20230916/201324814hopyTagwk.png)

![https://ithelp.ithome.com.tw/upload/images/20230916/201324810yyJKkC5FZ.png](https://ithelp.ithome.com.tw/upload/images/20230916/201324810yyJKkC5FZ.png)

**``EX2:``**
![https://ithelp.ithome.com.tw/upload/images/20230916/20132481Noiht6ZySb.png](https://ithelp.ithome.com.tw/upload/images/20230916/20132481Noiht6ZySb.png)
![https://ithelp.ithome.com.tw/upload/images/20230916/20132481NlCZgoMV42.png](https://ithelp.ithome.com.tw/upload/images/20230916/20132481NlCZgoMV42.png)

### 數據類型之字典dict

```python
能夠非常精確的儲存和表達數據值的含義
代碼實現:
    info_dict = {
        'username': 'jimmy', 
        'age': 20, 
        'hobby': 'coding', 
  }
1.字典文字描述
  大括號括起來 內部可以存放多個數據 數據的組織形式是K:V鍵值對
  鍵值對與鍵值對之間逗號隔開
      K是對V的描述性性質的資訊(解釋說明) 一般都是字串類型
      V是真正的數據值 可以是任意數據類型
2.按K取值
   字典只能按K取值 因為字典是無序的 沒有索引的概念
   info_dict['username']

"""
PEP8規範補充
  1.字典K:V，:右邊要空一格
"""
```
**``EX1:字典``**
![https://ithelp.ithome.com.tw/upload/images/20230916/2013248183BgL1bxlf.png](https://ithelp.ithome.com.tw/upload/images/20230916/2013248183BgL1bxlf.png)


**``EX2: 按鍵取值``**
![https://ithelp.ithome.com.tw/upload/images/20230916/20132481YcLzi4Ap67.png](https://ithelp.ithome.com.tw/upload/images/20230916/20132481YcLzi4Ap67.png)

### 小結 今日PEP8規範

```python
  1.單行注釋如果跟在代碼之後 那麼警號與代碼之間需要空兩格 內容與警號空一格
  2.如果單行注釋自成一行 那麼內容與警號空一格
  3.list
    1.逗號後面與數據值空一格
    2.賦值符號左右都得空一格   
  4.dict
    1.字典K:V，:右邊要空一格

ps:如何學習規範 可以借助於pycharm自動化格式程式碼反向學習
(mac快捷鍵command+option+L)
```
 

### 練習題(數據類型)


```python
# 附加練習題(提示:一步步拆解)
# 1.想辦法列印出jimmy
l1 = [11,  
      22,      
      'kevin',      
      ['tony', 'jerry', [123, 456, 'jimmy']]      
      ]

'''分步操作'''  
# 1.先看大列表到底有幾個數據值 以及我們想要的數據值在哪個裡面  
# print(l1[3])  
l2 = l1[3]  # ['tony', 'jerry', [123, 456, 'jimmy']]  
# 2.再次思考小列表有幾個數據值 以及我們想要的數據值在哪個裡面  
# print(l2[2])  
l3 = l2[2]  # [123, 456, 'jimmy']  
# 3.最後轉化成了簡單的索引直接取值  
print(l3[2])  
'''簡化操作'''  
print(l1[3][2][2])



# 2.想辦法列印出大寶貝
d1 = {'name': 'jimmy', 
      'others': {'a1': 'heiheihei', 
                 'a2': {'k1': 'hahaha', 
                        'k2': 'hehehe', 
                        'k3': '大寶貝'}
                 }
      }

'''分步操作'''
# 1.先拿大字典第二個鍵值對的值
# print(d1['others'])
d2 = d1['others']  # {'a1': 'heiheihei', 'a2': {'k1': 'hahaha', 'k2': 'hehehe', 'k3': '大寶貝'}}
# 2.再拿小字典第二個鍵值對的值
# print(d2['a2'])
d3 = d2['a2'] # {'k1': 'hahaha', 'k2': 'hehehe', 'k3': '大寶貝'}
# 3.轉化成簡單的按k直接取值
print(d3['k3'])
'''簡化操作'''
print(d1['others']['a2']['k3'])



# 3.想辦法列印出run
data = {'username': 'jimmy', 
        'hobby': [11,
                  22, 
                  {'height': 183, 
                   'hobby': ['read', 
                             'run', 
                             'music'
                             ]
                   }
                  ]
        }
'''分步操作'''
# print(data['hobby'])
data1 = data['hobby']  # [11, 22, {'height': 183, 'hobby': ['read', 'run', 'music']}]
# print(data1[2])
data2 = data1[2]  # {'height': 183, 'hobby': ['read', 'run', 'music']}
# print(data2['hobby'])
data3 = data2['hobby'] # ['read', 'run', 'music']
print(data3[1])
'''簡化操作'''
print(data['hobby'][2]['hobby'][1])
```


**``EX1: 想辦法列印出jimmy``**
![https://ithelp.ithome.com.tw/upload/images/20230916/20132481kMbzFu90dY.png](https://ithelp.ithome.com.tw/upload/images/20230916/20132481kMbzFu90dY.png)

![https://ithelp.ithome.com.tw/upload/images/20230916/20132481VR7kMNfM5R.png](https://ithelp.ithome.com.tw/upload/images/20230916/20132481VR7kMNfM5R.png)

**``EX2: 想辦法列印出大寶貝``**
![https://ithelp.ithome.com.tw/upload/images/20230916/20132481DWOpQt4Cpp.png](https://ithelp.ithome.com.tw/upload/images/20230916/20132481DWOpQt4Cpp.png)

![https://ithelp.ithome.com.tw/upload/images/20230916/20132481E2BOkRwmGK.png](https://ithelp.ithome.com.tw/upload/images/20230916/20132481E2BOkRwmGK.png)

**``EX3: 想辦法列印出run``**
![https://ithelp.ithome.com.tw/upload/images/20230916/20132481LvFAeXpEMx.png](https://ithelp.ithome.com.tw/upload/images/20230916/20132481LvFAeXpEMx.png)

![https://ithelp.ithome.com.tw/upload/images/20230916/201324813l3KmpF0xH.png](https://ithelp.ithome.com.tw/upload/images/20230916/201324813l3KmpF0xH.png)

# YouTube教學影片
[![Yes](https://img.youtube.com/vi/QVndMgzyljI/0.jpg)](https://www.youtube.com/watch?v=QVndMgzyljI)