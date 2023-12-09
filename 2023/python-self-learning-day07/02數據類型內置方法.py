# 整型內建方法與操作

# res = int(11.11) # 11
# res = int(11.57) # 11
# res = int('11') # 11
# res = int('11.11') # 字符串中必須是純數字才可以轉 報錯
# print(res, type(res))

# name = input('username>>>:') # username>>>:jimmy
# # print('name') # name
# print(name) # jimmy


# print(bin(100))  # 0b1100100
# print(oct(100))  # 0o144
# print(hex(100))  # 0x64

# print(int(0b1100100))
# print(int(0o144))
# print(int(0x64))

# print(int("0b1100100")) # ValueError: invalid literal for int() with base 10: '0b1100100'
# print(int("0o144"))
# print(int("0x64"))

# print(int("0b1100100", 2))
# print(int("0o144", 8))
# print(int("0x64", 16))

# 3.python自身對數字的敏感度較低(精確度低)
# s1 = 10.5
# s2 = 2.1
# print(s1 * s2)  # 22.05 這還算精確
#
# s1 = 1.1
# s2 = 1
# print(s1 - s2)  # 0.10000000000000009


# 浮點型內建方法與操作
# res = float(11) # 11.0
# res = float('11') # 11.0
# res = float('11.11') # 11.0
# res = float('1.1.1.1') # 不行
# res = float('abc')  # 不行
# print(res, type(res))

### 字串內建方法與操作

# res = str(11)
# print(res, type(res))  # 11 <class 'str'>
# res1 = str(11.11)
# print(res1, type(res1))  # 11.11 <class 'str'>
# res2 = str('hello')
# print(res2, type(res2))  # hello <class 'str'>
# res3 = str([1, 2, 3, 4])
# print(res3, type(res3))  # [1, 2, 3, 4] <class 'str'>
# res4 = str({'name': 'jimmy', })
# print(res4, type(res4))  # {'name': 'jimmy'} <class 'str'>
# res5 = str((1, 2, 3, 4, 5))
# print(res5, type(res5))  # (1, 2, 3, 4, 5) <class 'str'>
# res6 = str({1, 2, 3, 4, 5})
# print(res6, type(res6))  # {1, 2, 3, 4, 5} <class 'str'>
# res7 = str(True)
# print(res7, type(res7))  # True <class 'str'>

# s1 = 'helloworld'
# print(s1[-1:-5])  # 預設的順序是從左往右，無值取出
# print(s1[-1:-5:-1])  # 從右到左，間隔1，dlro
# print(s1[::2])
# 5.移除字串首尾指定的字元


# res = '  jimmy  '
# print(len(res))
# print(len(res.strip()))  # 括號內不寫 默認移除首尾的空格

# res1 = '$$jim$my$$'
# print(res1.strip('$'))  # jim$my


# 6.切割字串中指定的字元
# res = 'jimmy|123|read'
# print(res.split('|'))  # ['jimmy', '123', 'read']  該方法的處理結果是一個列表
# name, pwd, hobby = res.split('|') # 解壓賦值
# print(name, pwd, hobby)


# 7.字串格式化輸出
# res = 'my name is {} my age is {}'.format('jimmy', 123)
# print(res)

# res = 'my name is {0} my age is {1} {0} {0} {1}'.format('jimmy', 123)
# print(res)

# res = 'my name is {name1} my age is {age1} {name1} {age1} {name1} '.format(name1='jimmy', age1=123)
# print(res)

# name = input('username>>>:')
# age = input('age>>>:')
# res = f'my name is {name} my age is {age}'
# print(res)

# res = 'hElLO WorlD 666'
# print(res.upper())  # HELLO WORLD 666
# print(res.lower())  # hello world 666

# code = '8Ja6Cc'
# print('展示給用戶看的圖片驗證碼', code)
# confirm_code = input('請輸入驗證碼').strip()
# if confirm_code.upper() == code.upper():
#     print('驗證碼正確')


# res = 'hello world'
# print(res.isupper())  # 判斷字串是否是純大寫  False
# print(res.islower())  # 判斷字串是否是純小寫  True


# 2.判斷字串中是否是純數字
# res = 'jimmy'  # False
# res = '123'  # True
# res = ''  # False
# print(res.isdigit())
# guess_age = input('guess_age>>>:').strip()
# if guess_age.isdigit():
#     guess_age = int(guess_age)
# else:
#     print('年齡都不知道怎麼輸嗎???')

# guess_age >> >: a
# 年齡都不知道怎麼輸嗎???

# guess_age>>>:123


# 3.替換字串中指定的內容
# res = 'my name is jimmy jimmy jimmy jimmy jimmy'
# print(res.replace('jimmy', 'tonySB'))  # my name is tonySB tonySB tonySB tonySB tonySB
# print(res.replace('jimmy', 'tonySB', 1))  # my name is tonySB jimmy jimmy jimmy jimmy  從左往右替換指定個數內容


# 4.字串的拼接
# ss1 = 'hello'
# ss2 = 'world'
# print(ss1 + '$$$' + ss2)  # hello$$$world
# print(ss1 * 10)  # hellohellohellohellohellohellohellohellohellohello
# print('|'.join(['jimmy', '123', 'read', 'JDB']))  # jimmy|123|read|JDB
# print('|'.join(['jimmy', 123]))  # 參與拼接的數據值必須都是字串


# 5.統計指定字元出現的次數
# res = 'hello world'
# print(res.count('l'))  # 3


# 6.判斷字串的開頭或者結尾
# res = 'jimmy say hello'
# print(res.startswith('jimmy'))  # True
# print(res.startswith('j'))  # True
# print(res.startswith('jim'))  # True
# print(res.startswith('m'))  # False
# print(res.startswith('mmy'))  # False
# print(res.startswith('say'))  # False
# print(res.endswith('o'))  # True
# print(res.endswith('llo'))  # True
# print(res.endswith('hello'))  # True


# 7.其他方法補充
# res = 'helLO wORld hELlo worLD'
# print(res.title())  # Hello World Hello World (每個單字開頭都大寫)
# print(res.capitalize())  # Hello world hello world (開頭大寫)
# print(res.swapcase())  # HELlo WorLD HelLO WORld (大小寫互換)
# print(res.index('O'))  # 找索引位置為多少 4
# print(res.find('O'))
# print(res.index('c'))  # 找不到直接報R錯
# print(res.find('c'))  # 找不到默認返回-1
# print(res.find('LO'))  # 3


# print(list('hello'))
# print(list({'name': 'jimmy', 'pwd': 123}))
# print(list((1, 2, 3, 4)))
# print(list({1, 2, 3, 4, 5}))

# 2.需要掌握的方法
l1 = [111, 222, 333, 444, 555, 666, 777, 888]

# 1.索引取值(正負數)
# print(l1[0])
# print(l1[-1])

# 2.切片操作
# print(l1[0:5])
# print(l1[:])

# 3.間隔數 方向  與字串講解操作一致
# print(l1[::-1])  # [888, 777, 666, 555, 444, 333, 222, 111]

# 4.統計列表中數據值的個數
# print(len(l1))  # 8

# 5.數據值修改
# l1[0] = 123
# print(l1)  # [123, 222, 333, 444, 555, 666, 777, 888]

# 6.列表添加數據值
# 方式1:尾部追加數據值
# l1.append('吃飯')
# print(l1)  # [111, 222, 333, 444, 555, 666, 777, 888, '吃飯']
# l1.append(['jimmy', 'kevin', 'jerry'])
# print(l1)  # [111, 222, 333, 444, 555, 666, 777, 888, ['jimmy', 'kevin', 'jerry']]

# 方式2:任意位置插入數據值
# l1.insert(0, 'jimmy')  # ['jimmy', 111, 222, 333, 444, 555, 666, 777, 888]
# print(l1)
# l1.insert(1, [11, 22, 33, 44])
# print(l1)  # [111, [11, 22, 33, 44], 222, 333, 444, 555, 666, 777, 888]

# 方式3:擴展列表 合併列表
# ll1 = [11, 22, 33]
# ll2 = [44, 55, 66]
# print(ll1 + ll2)  # [11, 22, 33, 44, 55, 66]

# print(ll1 + ll2)  # [11, 22, 33, 44, 55, 66]
# ll1.extend(ll2)  # for循環+append

# 7.刪除列表數據
# 方式1:通用的刪除關鍵字del
# del l1[0]
# print(l1)

# 方式2:remove
# l1.remove(444)  # 括號內填寫數據值
# print(l1)

# 方式3:pop
# l1.pop(3)  # 括號內填寫索引值
# print(l1)
# l1.pop()  # 默認尾部彈出數據值
# print(l1)
# res = l1.pop(3)
# print(res)  # 444
# res1 = l1.remove(444)
# print(res1)  # None

# 8.排序
# ss = [54, 99, 55, 76, 12, 43, 76, 88, 99, 100, 33]
# ss.sort()  # 預設是升序
# print(ss)  # [12, 33, 43, 54, 55, 76, 76, 88, 99, 99, 100]
# ss.sort(reverse=True)
# print(ss)  # 改為降序 [100, 99, 99, 88, 76, 76, 55, 54, 43, 33, 12]

# 9.統計列表中某個數據值出現的次數
# print(l1.count(111))  # 1

# 10.顛倒列表順序
# l1.reverse()
# print(l1)  # [888, 777, 666, 555, 444, 333, 222, 111]





