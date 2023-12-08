# 1.計算1-100所有的數之和
# 我寫的(錯的)
# for i in range(1, 101):
#     i += i
# print(i)
# 2 + 4 + 6

# 老師寫的
# all_num = 0
# for i in range(1, 101):
#     all_num += i
# print(all_num)


# 2.判斷列表中數字2出現的次數
# 我寫的
# l1 = [11, 2, 3, 2, 2, 1, 2, 1, 2, 3, 2, 3, 2, 3, 4, 3, 2, 3, 2, 2, 2, 2, 3, 2]
# count = 0
# for i in l1:
#     if i == 2:
#         count += 1
# print(count)


# 老師寫
l1 = [11, 2, 3, 2, 2, 1, 2, 1, 2, 3, 2, 3, 2, 3, 4, 3, 2, 3, 2, 2, 2, 2, 3, 2]
# 1.先定義一個記錄數字2出現的計數器
count_num = 0
# 2.循環獲取列表中每一個數據值判斷是不是數字2
for i in l1:
    # 3.如果i綁定的數據值是2，則讓計數器自增1
    if i == 2:
        count_num += 1
# 4.等待for循環運行結束，打印計數器
print(count_num)

# 3.編寫程式碼自動生成所有頁網址(注意總共多少頁)
# 我寫的(錯的)
#     https://movie.douban.com/top250
# url = 'https://movie.douban.com/top%s'
# for i in range(1, 251):
#     print(url % i)


# 3.編寫程式碼自動生成所有頁網址(注意總共多少頁)
# https://movie.douban.com/top250?start=0&filter=
# https://movie.douban.com/top250?start=25&filter=
# https://movie.douban.com/top250?start=50&filter=

# base_url = 'https://movie.douban.com/top250?start=%s&filter='
# for i in range(0, 250, 25):
#     print(base_url % i)


# 4.編寫程式碼列印出下列圖形(ps:for循環嵌套)
# *****
# *****
# *****
# *****

# for i in range(4):  # 0 1 2 3        4次 4行
#     for j in range(5):  # 0 1 2 3 4  5次 5列
#         print('*', end='')
#     print() # 每次內層循環結束 換行
