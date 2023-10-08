---
title: Day04 - 基本數據類型(bool、tuple、set)，與使用者交互，格式化輸出，基本運算符，常用賦值符，邏輯運算符，成員運算符，身份運算符，練習題
description: 再學習基礎數據類型(bool、tuple、set)觀念並實際在pycharm執行代碼，各類運算符與賦值符學習，並將數據藉由python進行運算與邏輯判斷。
slug: python-self-learning-day04
date: 2023-10-07 03:02:00+0800
image: 
categories:
  - python
tags:
  - python
weight: 1
---

# 今日内容概要

- python基本數據類型
- 與使用者交互
- 格式化輸出
- 基本運算符
- 多種賦值方式
- 邏輯運算符
- 成員運算符
- 身份運算符


### 基本數據類型之布爾值bool
```python
1.用來判斷事物的對錯 是否可行 只要用於流程控制中
2.只有兩種狀態
	True 對的 真的 可行的
  	False 錯的 假的 不可行的
3.python中所有數據都自帶布爾值
	布爾值為False的數據有：0 None '' [] {}
	布爾值為True的數據有：除了上面的都是True
4.存儲布爾值的變數名一般推薦使用is開頭
	is_delete = False
 	is_alive = True
"""
很多程式中提供的註銷帳戶的功能 其實底層並沒有刪除數據 而是修改了數據的狀態
id		username	password    phone    is_delete
1		jimmy		123		   110     	  1
2		kevin		321		   120		  0
"""
```


``EX：``
![[media/Pasted image 20230924132454.png]](https://drive.google.com/uc?export=view&id=1UKGhrcTgQmiyHRSeR7Lg-fih_pbBeH9z)

![[media/Pasted image 20230924132503.png]](https://drive.google.com/uc?export=view&id=1ULYWLzB01iQ7GzcVwSDX1m3leDzrEiPD)

### 基本數據類型之元組tuple
```python
1.也稱為『不可變』的列表
	元組內索引綁定的記憶體位址不能修改
2.小括弧括起來 內部存放多個數據值 數據值與數據值之間逗號隔開 數據值可以是任何數據類型
3.代碼實現
	t1 = (11, 22, 'jimmy')
4.元組與列表的對比
	# 列表
	l1 = [11, 22, 33]
    print(l1[0]) # 獲取索引0對應的數據值
    l1[0] = 666
    print(l1)  # [666, 22, 33]

	# 元組
	t1 = (11, 22, 33)
    print(t1[0])
    t1[0] = 999
    print(t1) # 報錯

	# 練習題 元組混列表
	t1 = (11, 22, [111, 222])
    t1[2][1] = 666
    print(t1) # (11, 22, [111, 666])
    """
    A.直接報錯
    B.(11, 22, [111, 666])
    C.不知道 超出了我的認知
    """
5.元組內如果只有一個數據值
	t1 = (1)
    t2 = (11.11)
    t3 = ('Jimmy')
    print(type(t1), type(t2), type(t3))  # <class 'int'> <class 'float'> <class 'str'>
    t1 = (1,)
    t2 = (11.11,)
    t3 = ('Jimmy',)
    print(type(t1), type(t2), type(t3))  # <class 'tuple'> <class 'tuple'> <class 'tuple'>
    """
    建議：以後在使用可以存放多個數據值的數據類型時 如果裡面暫時只有一個數據值 那麼也建議你加上逗號
    """
```

``EX1：元組與列表的對比``

列表：
![[media/Pasted image 20230924133144.png]](https://drive.google.com/uc?export=view&id=1UNTMp4yPuolhPzSyPej2VZie3y03TLf_)

![[media/Pasted image 20230924133151.png]](https://drive.google.com/uc?export=view&id=1UOCTk877VtPQb3_GoVL5dnoZtF1Pi6LX)

圖解：
![[media/Pasted image 20230924134118.png]](https://drive.google.com/uc?export=view&id=1UXXhPnGt7AQAzIcjEZ6eETZxg6au4jg6)

元組：
![[media/Pasted image 20230924133230.png]](https://drive.google.com/uc?export=view&id=1USayX3L1mJbGYMNE0rmGYGP_dSAy9MnQ)

![[media/Pasted image 20230924133318.png]](https://drive.google.com/uc?export=view&id=1UT9-mFcjaWiEzJQvJvZd4xsWCJlL4697)

圖解：
![[media/Pasted image 20230924134132.png]](https://drive.google.com/uc?export=view&id=1UmZ9kksysocDyVU5UJaUrfqvwW4Zq2k2)
``EX2：練習題 元組混列表``
![[media/Pasted image 20230924134356.png]](https://drive.google.com/uc?export=view&id=1UwJib92QzhP14nFJVOnNvudHTYWdWnha)

![[media/Pasted image 20230924134515.png]](https://drive.google.com/uc?export=view&id=1UxJwb9ou21ZOiRZJe29eqWZX4K-0--gQ)

圖解：

![[media/Pasted image 20230924134920.png]](https://drive.google.com/uc?export=view&id=1V9ypSNxKABMRj5Jblfh5oiF8wyayrqFr)

``EX3：元組內如果只有一個數據值``

![[media/Pasted image 20230924140052.png]](https://drive.google.com/uc?export=view&id=1VO20_6qbUH0mokCtLZkTo1MErCh2vYYF)


### 基本數據類型之集合set

```python
1.集合只能用於去重和關係運算
	後面再講 暫且忽略
2.集合內數據只能是不可變類型
	後面再講 暫且忽略
3.大括弧括起來 內部存放多個數據值 數據值與數據值之間逗號隔開 數據值不是k：v鍵值對
4.代碼實現
	s1 = {1, 2, 3, 4, 5, 6}
5.定義空集合與空字典	
	{} 預設是字典
 	set() 定義空集合
```

``EX1：定義空集合``

![[media/Pasted image 20230924135732.png]](https://drive.google.com/uc?export=view&id=1VKrI0Ly6DmQzf9Y1KFrV-AvR4wk21HXw)

### 與使用者交互

```python
1.獲取使用者輸入
	input
	# 獲取使用者輸入
    username = input('請輸入您的使用者名>>>：')
    """
    1.先執行input獲取用戶輸入
    2.將輸入的數據綁定給變數名username
    3.以後在程式中就可以使用變數名反覆調用用戶數據
    """
	強調：input獲取到的數據都會統一處理成字串類型

2.輸出內部資訊
	print
 	1.括弧內既可以放數據值也可以放變數名 並且支援多個 逗號隔開即可
 	2.print自帶換行符
		換行符：\r\n \n(斜杠與字母組合到一起可能會產生特殊的含義)
	3.print也可以切換結束符
    	print(數據,end='預設是\n')

擴展：python2與python3中兩個關鍵字的區別
 	python2中
    	input方法需要使用者自己提前指定數據類型 寫什麼類型就是什麼類型
 	 	 raw_input方法與python3中input一致 輸入的統一處理成字串	
	python2中
    	print方法有兩種使用方式
			print 數據值
			print(資料值)
```


``EX1：1.獲取使用者輸入``

![[media/Pasted image 20230924145933.png]](https://drive.google.com/uc?export=view&id=1VPOQE18WZKXhim0p24AEhtEnVy_jtD-S)

![[media/Pasted image 20230924145941.png]](https://drive.google.com/uc?export=view&id=1VkabhN6YRWzirOeB-bVgy_ze2foYKJSN)


``EX2：input獲取到的數據都會統一處理成字串類型``

![[media/Pasted image 20230924150312.png]](https://drive.google.com/uc?export=view&id=1VsxamENYyMmjSV-JrltrewhKCHuZrg2E)

![[media/Pasted image 20230924150214.png]](https://drive.google.com/uc?export=view&id=1Vkno0qxdZCQoDMt8OiuSFkC8JIO60MpQ)

![[media/Pasted image 20230924150232.png]](https://drive.google.com/uc?export=view&id=1VmtBhmKDm2226V3cxn9QV05MUKjq9_ir)

![[media/Pasted image 20230924150303.png]](https://drive.google.com/uc?export=view&id=1Vo98sapoA8uZ2vBzEOYFpt7ajWuljH2z)

``EX3：輸出內部資訊``
![[media/Pasted image 20230924150850.png]](https://drive.google.com/uc?export=view&id=1W0t52WQYj7_a0SpkKLzC-SIwRNOcyAay)

![[media/Pasted image 20230924150902.png]](https://drive.google.com/uc?export=view&id=1W3B8TAGggJvONfAFT22NOW8jdXPLICMr)

``EX4：2.print自帶換行符``

![[media/Pasted image 20230924151229.png]](https://drive.google.com/uc?export=view&id=1W3ym1qprsvZu6qDWUQTqefWfn6EWvJ8N)

![[media/Pasted image 20230924151236.png]](https://drive.google.com/uc?export=view&id=1W4oTdG5E_bKa9A-rb6ReBKmewMmfjfXY)

``EX5：3.print也可以切換結束符``
![[media/Pasted image 20230924151416.png]](https://drive.google.com/uc?export=view&id=1W5Pf2x060pAfzyPQQ7Ieo85CkNjVMbBF)

![[media/Pasted image 20230924151424.png]](https://drive.google.com/uc?export=view&id=1W94i8AqA_BnBnGWHhLpPS910Y2CXAHkR)

``EX6：python2與python3中兩個關鍵字的區別``

python2

```
input方法需要使用者自己提前指定數據類型 寫什麼類型就是什麼類型
raw_input方法與python3中input一致 輸入的統一處理成字串	
```
![[media/Pasted image 20230924152959.png]](https://drive.google.com/uc?export=view&id=1WFqqGgia6hn5VKdqA6vMoD6Dicos0XUl)

![[media/Pasted image 20230924153037.png]](https://drive.google.com/uc?export=view&id=1WMVeustUNexvZBCM2qzLvgFN2d6ODR6p)


python2
```
print方法有兩種使用方式
	print 數據值
	print(資料值)
```

![[media/Pasted image 20230924153154.png]](https://drive.google.com/uc?export=view&id=1WOrXnz3jBL39bAzTrBvZm3yU9Q6f4pqJ)


### 格式化輸出

```python
提前定義好一些內容 將來需要使用的時候可以局部修改
	
代碼實現
	在現實生活中大部分情況下使用下劃線提示別人填寫內容
 	但是在程式中需要使用佔位元：%s %d

info = '%s同學你好'
'''單個佔位符'''
# print(info % 'Jimmy') # Jimmy同學你好
# print('%s同學你好' % 'Tony') # Tony同學你好
# print(info % ('Jimmy',))
# print('%s同學你好' % ('Tony',))

'''多個佔位符'''
# desc = '姓名：%s 年齡：%s 愛好：%s'
# print(desc % ('Jimmy', 18, 'read'))
# print('姓名：%s 年齡：%s 愛好：%s' % ('tony', 28, 'rap'))

'''注意事項：有幾個佔位符就需要幾個數據值'''
# print('my name is %s my age is %s' % ('Jimmy',)) # 少了不行
# print('my name is %s my age is %s' % ('Jimmy', 18, 'read')) # 多了不行

'''不同佔位符的區別'''
# demo1 = '%s您好 您本月的話費是%s 餘額是%s' # %s常見數據類型都支援
# print(demo1 % ('Jimmy', 100, 10000000000000))
# demo2 = '%d您好 您本月的話費是%d 餘額是%d' # %d只支援數字類型
# print(demo2 % ('tony', 1000000000, -100000))

print('%08d'% 123)  # 00000123
print('%08d'% 1234324324)  # 1234324324
```

``EX1：單個佔位符``
![[media/Pasted image 20230924154615.png]](https://drive.google.com/uc?export=view&id=1WP1pcqIn0k9lsBtqHVkDSkK66kjS8A7p)

``EX2：多個佔位符``

![[media/Pasted image 20230924154626.png]](https://drive.google.com/uc?export=view&id=1WPVVNs4kxeI27ZmVyDqtUJoGHJbdEJ4X)

``EX3：注意事項：有幾個佔位符就需要幾個數據值``

![[media/Pasted image 20230924154812.png]](https://drive.google.com/uc?export=view&id=1WXJKWeotlTge8-WUmbJgX2GsCijcjga1)

``EX4：不同佔位符的區別``

```
%s常見數據類型都支援
```

![[media/Pasted image 20230924154936.png]](https://drive.google.com/uc?export=view&id=1W_5ByyA9tqEV2I32Tg_O0F3MRfv6Wyrc)

```
%d只支援數字類型
```
![[media/Pasted image 20230924154951.png]](https://drive.google.com/uc?export=view&id=1Wa1yC-SM5HnhTs-2tl0qUGxF624oh_GN)

![[media/Pasted image 20230924155002.png]](https://drive.google.com/uc?export=view&id=1WeKTpra0DR3xzB1soOyiNvmaeJBhkQ4I)


``EX5：%d補位功能``
![[media/Pasted image 20230924155155.png]](https://drive.google.com/uc?export=view&id=1WijFevjuTzqETBz3i2lu6_F7zJu_UxNG)

### 基本運算符

以下假設變數： **a=10，b=20**：

| 運算符       | 描述                        | 實例                                        |
|-----------|---------------------------|-------------------------------------------|
| +         | 加 - 兩個物件相加                | a + b 輸出結果 30                             |
| -         | 減 - 得到負數或是一個數減去另一個數       | a - b 輸出結果 -10                            |
| *         | 乘 - 兩個數相乘或是返回一個被重複若干次的字串 | a * b 輸出結果 200                            |
| /         | 除 - x除以y                  | b / a 輸出結果 2                              |
| %         | 取餘 - 返回除法的餘數              | b % a 输出结果 0                              |
| **        | 次方 - 返回x的y次方               | a\*\*b 為10的20次方， 輸出結果 100000000000000000000 |
| //        | 取整除 - 傳回商的整數部分（向下取整）      |    >>>9//2 4, >>>-9//2 -5                                     |


```python
1.數學運算符
    + - * / % // **
    簡化寫法
    n = 10
    n += 1  # n = n + 1
    n -= 1  # n = n - 1
    n *= 1  # n = n * 1
    n /= 1  # n = n / 1
    n %= 1  # n = n % 1
    n //= 1  # n = n // 1
    n **= 1  # n = n ** 1
2.比較運算符
	< > <= >= ==(等於號) !=(不等於)
```

### 常用賦值符

```python
1.鏈式賦值
	# name = 'jimmy'
    # name1 = name
    # name2 = name
    # 鏈式賦值
    name = name1 = name2 = 'jimmy'
2.交叉賦值
	m = 100
    n = 999
    '''讓m和n互相轉換綁定的值'''
    """奇葩式寫法"""
    # m = n
    # n = m
    # print(m, n)  # 999 999
    '''方式1:採用中間變數'''
    # temp = m
    # m = n
    # n = temp
    # print(m, n)  # 999 100
    '''方式2:交叉賦值語法'''
    m, n = n, m
    print(m, n)  # 999 100
3.解壓賦值
	 name_list = ['jimmy', 'kevin', 'tony', 'oscar']
    '''low的寫法'''
    # name1 = name_list[0]
    # name2 = name_list[1]
    # name3 = name_list[2]
    # name4 = name_list[3]
    '''解壓賦值語法'''
    # name1, name2, name3, name4 = name_list
    '''解壓賦值在使用的時候 正常情況下需要保證左邊的變數名與右邊的數據值個數一致'''
    # a, b = name_list  # 變數名少了不行
    # a, b, c, d, e = name_list  # 變數名多了也不行
    '''當需要解壓的數據個數特別多 並且我們只需要使用其中的幾個 那麼可以打破上述的規則'''
    # a, *b = name_list  # *會自動接收多餘的數據 組織成列表賦值給後面的變數名
    # print(a)  # jimmy
    # print(b)  # ['kevin', 'tony', 'oscar']
    # a, c, *b = name_list
    # print(a)
    # print(c)
    # print(b)  # ['tony', 'oscar']
    # a, *b, c = name_list
    # print(a)  # jimmy
    # print(b)  # ['kevin', 'tony']
    # print(c)  # oscar
    '''當數據值不準備使用的時候 可以使用下劃線作為變數名綁定'''
    a, *_, c = name_list
```


``EX1：1.鏈式賦值``
![[media/Pasted image 20230924161001.png]](https://drive.google.com/uc?export=view&id=1WkvQeI6jCqx7LjxeD_Am633bE3dPe4oW)


``EX2：2.交叉賦值``

奇葩式寫法：
![[media/Pasted image 20230924161159.png]](https://drive.google.com/uc?export=view&id=1Wmf0RWqS1D14pwwMfR4VdUTnU45P_iBF)

圖解：
![[media/Pasted image 20230924161420.png]](https://drive.google.com/uc?export=view&id=1Wrj8gJjos962NQSM6-e-cXC4F1142kXQ)

方式1:採用中間變數：

![[media/Pasted image 20230924161617.png]](https://drive.google.com/uc?export=view&id=1WyO8xfP9rSwPRckHth_LzW_TzaHZxiNR)

圖解：

![[media/Pasted image 20230924161808.png]](https://drive.google.com/uc?export=view&id=1X2zQV0va9R_TiyURbSjzJ5dvrf8mPnLz)

方式2:交叉賦值語法：

![[media/Pasted image 20230924161858.png]](https://drive.google.com/uc?export=view&id=1X5Uf-m-CqZfwJAa9AIYBtrB5BOhUWutw)


``EX3：3.解壓賦值``

![[media/Pasted image 20230924162110.png]](https://drive.google.com/uc?export=view&id=1XBRguC_2efTtnrCvkyg5NrAxA3J2zmly)


```
解壓賦值在使用的時候 正常情況下需要保證左邊的變數名與右邊的數據值個數一致
變數名少了不行
變數名多了也不行
```
![[media/Pasted image 20230924162629.png]](https://drive.google.com/uc?export=view&id=1XGmJgvg3Ct36F1ynSkZ2dDXEBUqBWihW)

![[media/Pasted image 20230924162744.png]](https://drive.google.com/uc?export=view&id=1XKdhAVdFrw-6Fg1Mv0BNxyU856UK5yaA)

```
當需要解壓的數據個數特別多 並且我們只需要使用其中的幾個 那麼可以打破上述的規則
*會自動接收多餘的數據 組織成列表賦值給後面的變數名
```
![[media/Pasted image 20230924162813.png]](https://drive.google.com/uc?export=view&id=1XLkR3uSy4o9PVsG-Mk4ZfUHaK_eLy5QG)

```
當數據值不準備使用的時候 可以使用下劃線作為變數名綁定
```
![[media/Pasted image 20230924163036.png]](https://drive.google.com/uc?export=view&id=1XPnZIlwsKPV_JO5iD599aBNAhlLQPKsa)

### 邏輯運算符

```python
'''主要配合條件一起使用'''
and		與
	and連接的多個條件必須全部成立 結果才成立

	1 > 2 and 4 < 8 and 10 < 1 and 1 == 2  如果條件中全部由and組成那麼判斷起來非常的簡單 只要發現一個不成立 結果就不成立      
    print(1 < 10 and 666)  # 666  成立
    print(1 < 10 and 2 < 8)  # True  成立
    print(111 and 222)  # 222  成立
    
    如果需要你準確的說出具體的結果值 那麼需要按照下列方式
    如果and左邊的條件是成立的 那麼就完全取決於右邊的條件
    右邊如果直接是數據值 那麼結果就是該數據值 如果是含有表達式 則為布爾值  


or		或
	or連接的多個條件只要有一個成立 結果就成立

   1 > 2 or 4 < 8 or 10 < 1 or 1 == 2   如果條件中全部由or組成那麼判斷起來非常的簡單 只要發現一個成立 結果就成立   
	# print(1 < 10 or 666)  # True
    # print(666 or 1 > 10)  # 666
    print(0 or False)  # False
    print(0 or 111)  # 111
    規律用and    


not		非
	取反
 	類似於說反話
	print(not 1)  # False  
	print(not 0)  # True
"""
三者混合使用的時候有優先順序之分 但是我們不需要記憶優先順序 應該通過代碼的形式提前規定好優先順序
	eg: 先乘除後加減 但是可以使用括弧來改變優先順序
	(3>4 and 4>3) or ((1==3 and 'x' == 'x') or 3 >3)
"""
```


``EX1：and``

![[media/Pasted image 20230924213932.png]](https://drive.google.com/uc?export=view&id=1Xyz3gB-X7v4DTCPqX4rSYxETeMR6sWy7)

![[media/Pasted image 20230924214104.png]](https://drive.google.com/uc?export=view&id=1Y7DNOYpHFD6iVck8oL2hOXKhJaU3trM0)

![[media/Pasted image 20230924214203.png]](https://drive.google.com/uc?export=view&id=1YNfbbQUaTTy_VEeH3cAFcBU-DQ0dlmPM)

![[media/Pasted image 20230924214240.png]](https://drive.google.com/uc?export=view&id=1YOQ6eHPHssCaAsVJQr8bRMF3ItJiA7Cy)

``EX2：or``

![[media/Pasted image 20230924214645.png]](https://drive.google.com/uc?export=view&id=1YOUNIG8-wKxetNZnv54w3kb5YY42XQ8x)

``EX3：not``

![[media/Pasted image 20230924214814.png]](https://drive.google.com/uc?export=view&id=1YQdjHEJalfKB5O57xkpmBgR27gq4wxwO)

```
三者混合使用的時候有優先順序之分 但是我們不需要記憶優先順序 應該通過代碼的形式提前規定好優先順序
```
![[media/Pasted image 20230924215046.png]](https://drive.google.com/uc?export=view&id=1YXoEsW0WnrPUO_2vqAq82fXXdV9GtTqA)

### 成員運算符

```python
判斷個體在不在群體內

# name_list = ['jimmy', 'kevin', 'oscar', 'jerry']
# print('tony' in name_list)  # False
# print('tony' not in name_list)  # True
# print('j' in name_list)  # False 列表最小單位是數據值 不能再細分

# s1 = 'hello world'
# print('d' in s1)  # 字串最小單位是單個單個的字元

d1 = {
      'username': 'jimmy',
      'pwd': 123
}
print('jimmy' in d1)  # False 字典成員運算只有鍵參與
print('username' in d1)  # True      'username' 'pwd'
```

``EX1：成員運算符``

列表
![[media/Pasted image 20230924215420.png]](https://drive.google.com/uc?export=view&id=1Yen-H1q_kfsgDzHLuXgiNxuhBl9Rtd5a)

字串
![[media/Pasted image 20230924215537.png]](https://drive.google.com/uc?export=view&id=1YjgP1oPtAnhSdC06jODS9DO-MfAV_MZL)

字典
![[media/Pasted image 20230924215657.png]](https://drive.google.com/uc?export=view&id=1YkrLiCXru6AmHIQ0q8gXucubplhFqJXc)

### 身份運算符

```python
"""
id()  返回一串數字 該數字可以看成是記憶體位址
"""
is	   判斷記憶體位址是否相同
==     判斷數據值是否相同

# l1 = [11, 22, 33, 44, 55, 66, 77, 88]
# l2 = [11, 22, 33, 44, 55, 66, 77, 88]
# print(l1 == l2)  # True
# print(id(l1))
# print(id(l2))
# print(l1 is l2)  # False

# 小整數池
i1 = 11
i2 = 11
print(i1 is i2)


s1 = 'jason jason jason'
s2 = 'jason jason jason'
print(s1 is s2)
不同的環境下可能優化的程度不一樣 

"""
了解
    值相同 内存地址可能不同
    内存地址相同 值肯定相同
"""
```

``EX1：身份運算符``

```
is	   判斷記憶體位址是否相同
==     判斷數據值是否相同
```
![[media/Pasted image 20230924220017.png]](https://drive.google.com/uc?export=view&id=1YlTxoqnPsqOOYuuzz7nwj10lKZjkRizV)


``EX2：不同的環境下可能優化的程度不一樣``

pycharm有額外做優化和解釋器出來結果不一樣


![[media/Pasted image 20230924220655.png]](https://drive.google.com/uc?export=view&id=1YsHUn77xVSBt2YNRLXbDM8Ag3zA9l5GU)

![[media/Pasted image 20230924220726.png]](https://drive.google.com/uc?export=view&id=1Yu6wBC4MUP1-NKV_3IcmT50yX064U83T)

### 練習題

```python
1.獲取使用者輸入並列印成下列格式
	 ------------ info of Jimmy -----------
    Name : Jimmy
    Age  : 18
    Sex  : male
    Job  : Teacher 
    ---------------- end -----------------
	 # 1.先制定一個列印的範本
    info_demo = """
        ------------ info of %s -------------
        Name : %s
        Age  : %s
        Job  : %s 
        ---------------- end -----------------
    """
    # 2.獲取用戶輸入
    username = input('username>>>:')
    age = input('age>>>:')
    job = input('job>>>:')
    # 3.格式化輸出
    print(info_demo % (username, username, age, job))
    
2.下列變數名v綁定的結果
	v1 = 1 or 3  # 1  
	v2 = 1 and 3  # 3  
	v3 = 0 and 2 and 1  # 0  
	v4 = 0 and 2 or 1  # 1 沒寫執行順序，是not->and->or  
	v5 = 0 and 2 or 1 or 4  # 1 沒寫執行順序，是not->and->or  
	v6 = 0 or False and 1  # False
```


``EX1：1.獲取使用者輸入並列印成下列格式``

![[media/Pasted image 20230924221852.png]](https://drive.google.com/uc?export=view&id=1ZD_kB5_uIwEm-F8j_JC4sRUqujPhpuby)

``EX2：2.下列變數名v綁定的結果``

![[media/Pasted image 20230924222521.png]](https://drive.google.com/uc?export=view&id=1ZDzI9mW1ffwb0sF06RyYHZMuolKfKUN5)


