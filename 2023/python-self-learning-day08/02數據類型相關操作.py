# print(dict([('name', 'pwd'), ('jimmy', '123')]))

# user_dict = {
#     'username': 'jimmy',
#     'password': 123,
#     'hobby': ['read', 'music', 'run']
# }

# 1.按k取值(不推薦使用)
# print(user_dict['username'])  # jimmy
# print(user_dict['phone'])  # k不存在會直接報錯

# 2.按內建方法get取值(推薦使用)
# print(user_dict.get('username'))  # jimmy
# print(user_dict.get('age'))  # None
# print(user_dict.get('username', '沒有喲 嘿嘿嘿'))  # jimmy   鍵存在的情況下獲取對應的值
# print(user_dict.get('phone', '沒有喲 嘿嘿嘿'))  # 鍵不存在默認返回None 可以通過第二個參數自訂

# 3.修改值數據
# print(id(user_dict))
# user_dict['username'] = 'tony'  # 鍵存在則修改對應的值
# print(id(user_dict))
# print(user_dict)

# 4.新增鍵值對
# user_dict['age'] = 18  # 鍵不存在則新增鍵值對
# print(user_dict)

# 5.刪除數據
# del user_dict['username']
# print(user_dict)  # {'password': 123, 'hobby': ['read', 'music', 'run']}
# res = user_dict.pop('password')
# print(user_dict)  # {'username': 'jimmy', 'hobby': ['read', 'music', 'run']}
# print(res)  # 123

# 6.統計字典中鍵值對的個數
# print(len(user_dict))  # 3

# 7.字典三劍客
# print(user_dict.keys())  # 一次性獲取字典所有的鍵 dict_keys(['username', 'password', 'hobby'])
# print(user_dict.values())  # 一次性獲取字典所有的值 dict_values(['jimmy', 123, ['read', 'music', 'run']])
# print(user_dict.items())  # 一次性獲取字典的鍵值對數據  dict_items([('username', 'jimmy'), ('password', 123), ('hobby', ['read', 'music', 'run'])])
# for k, v in user_dict.items():
#     print(k, v)


# 8.補充說明
# print(dict.fromkeys(['name', 'pwd', 'hobby'], 123))  # 快速生成值相同的字典  # {'name': 123, 'pwd': 123, 'hobby': 123}
# res = dict.fromkeys(['name', 'pwd', 'hobby'], [])
# print(res)  # {'name': [], 'pwd': [], 'hobby': []}
# res['name'].append('jimmy')
# res['pwd'].append(123)
# res['hobby'].append('study')
# print(res)  # {'name': ['jimmy', 123, 'study'], 'pwd': ['jimmy', 123, 'study'], 'hobby': ['jimmy', 123, 'study']}
'''當第二個公共值是可變類型的時候 一定要注意 通過任何一個鍵修改都會影響所有'''

# res = user_dict.setdefault('username', 'tony')
# print(user_dict, res)  # 鍵存在則不修改 結果是鍵對應的值  # {'username': 'jimmy', 'password': 123, 'hobby': ['read', 'music', 'run']} jimmy
# res = user_dict.setdefault('age', 123)
# print(user_dict, res)  # 存不存在則新增鍵值對 結果是新增的值  # {'username': 'jimmy', 'password': 123, 'hobby': ['read', 'music', 'run'], 'age': 123} 123
# user_dict.popitem()  # 彈出鍵值對 後進先出


# t1 = (11, 22, 33, 44, 55, 66)
# 4.統計元組內數據值的個數
# print(len(t1))
# 5.統計元組內某個數據值出現的次數
# print(t1.count(11))  # 1
# 6.統計元組內指定數據值的索引值
# print(t1.index(22))  # 1
# 7.元組內如果只有一個數據值那麼逗號不能少
# 8.元組內索引綁定的記憶體地址不能被修改(注意區分 可變與不可變)
# 9.元組不能新增或刪除數據


# print(set('hello'))
# print(set([11, 22, 33]))
# print(set([11, [11, 22], 33]))


# 3.去重
# s1 = {11, 22, 11, 22, 22, 11, 222, 11, 22, 33, 22}
# print(s1)  # {33, 11, 222, 22}
# l1 = [11, 22, 33, 22, 11, 22, 33, 22, 11, 22, 33, 22]
# s1 = set(l1)
# l1 = list(s1)
# print(l1)  # [33, 11, 22]
'''集合的去重無法保留原先數據的排列順序'''

# f1 = {'jimmy', 'tony', 'jerry', 'oscar'}  # 用戶1的好友列表
# f2 = {'jack', 'jimmy', 'tom', 'tony'}  # 用戶2的好友列表
# 1.求兩個人的共同好友
# print(f1 & f2)  # {'jimmy', 'tony'}
# 2.求用戶1獨有的好友
# print(f1 - f2)  # {'jerry', 'oscar'}
# 3.求兩個人所有的好友
# print(f1 | f2)  # {'jimmy', 'jack', 'tom', 'tony', 'oscar', 'jerry'}
# 4.求兩個人各自獨有的好友
# print(f1 ^ f2)  # {'oscar', 'tom', 'jack', 'jerry'}
# 5.父集 子集
# print(f1 > f2)  # False  # f1 是否都包含 f2
# print(f1 < f2)  # False  # f2 是否都包含 f1



