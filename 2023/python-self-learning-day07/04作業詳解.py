# 2.基於字串充當資料庫完成用戶登錄(基礎練習)
#     data_source = 'jimmy|123'  # 一個用戶數據
#     獲取用戶使用者名稱和密碼 將上述數據拆分校驗用戶資訊是否正確

# 我自己寫
# username = input('username>>:')
# password = input('password>>:')
# data_source = 'jimmy|123'
# if username == data_source.split('|')[0] and password == data_source.split('|')[1]:
#     print('登入正確')
# else:
#     print('登入錯誤')

# 老師寫的
# 定義用戶真實數據
# data_source = 'jason|123'
# # 1.獲取使用者名稱和密碼
# username = input('username>>>:').strip()
# password = input('password>>>>:').strip()
# # 2.切割字串 獲取真實使用者名稱和密碼
# real_name, real_pwd = data_source.split('|')
# # 3.校驗使用者名稱和密碼是否正確
# if username == real_name and password == real_pwd:
#     print('登錄成功')
# else:
#     print('使用者名稱或密碼錯誤')


# 3.基於列表充當資料庫完成用戶登錄(拔高練習)  # 多個用戶數據
#     data_source = ['jimmy|123', 'kevin|321','oscar|222']

# 我自己寫
# username = input('username>>:')
# password = input('password>>:')
# data_source = ['jimmy|123', 'kevin|321','oscar|222']
# if username == data_source[0].split('|')[0] and password == data_source[0].split('|')[1]:
#     print('登入正確')
# elif username == data_source[1].split('|')[0] and password == data_source[1].split('|')[1]:
#     print('登入正確')
# elif username == data_source[2].split('|')[0] and password == data_source[2].split('|')[1]:
#     print('登入正確')
# else:
#     print('登入錯誤')

# 老師寫的
# data_source = ['jason|123', 'kevin|321', 'oscar|222']
# # 1.先獲取用戶輸入的使用者名稱和密碼
# username = input('username>>>:').strip()
# password = input('password>>>>:').strip()
# # 2.循環獲取列表中每一個真實數據
# for data in data_source:  # 'jason|123'   'kevin|321'
#     real_name, real_pwd = data.split('|')  # jason  123
#     if username == real_name and password == real_pwd:
#         print('登錄成功')
#         break
# else:
#     print('使用者名稱或密碼錯誤')
#
# data_source = ['jason|123', 'kevin|321', 'oscar|222']
# username = input('username>>>:').strip()
# password = input('password>>>:').strip()
# user_data = f'{username}|{password}'  # username + '|' + password
# if user_data in data_source:
#     print('登錄成功')
# else:
#     print('使用者名稱或密碼錯誤')

# 4.利用列表編寫一個員工姓名管理系統
#     輸入1執行添加使用者名稱功能
#     輸入2執行查看所有使用者名稱功能
#     輸入3執行刪除指定使用者名稱功能
#     '''分析 用戶輸入的不同 可以執行不同的代碼'''
#     ps: 思考如何讓程序循環起來並且可以根據不同指令執行不同操作
#     提示: 循環結構 + 分支結構

# 我自己寫
# all_user = []
# while True:
#     input_choice = input('添加使用者名稱，請輸入"1"\n查看所有使用者名稱，請輸入"2"\n刪除指定使用者名稱，請輸入"3"\n退出程序，請輸入"4"\n')
#     if input_choice == '1':
#         add_user = input('請輸入要添加使用者名稱>>:')
#         all_user.append(add_user)
#         print(f'添加{add_user}成功')
#     elif input_choice == '2':
#         print(f'查看所有使用者名稱: {all_user}')
#     elif input_choice == '3':
#         del_user = input('請輸入要刪除使用者名稱>>:')
#         if del_user in all_user:
#             all_user.remove(del_user)
#         else:
#             print(f'刪除{del_user}不存在')
#     elif input_choice == '4':
#         print("退出程序。")
#         break
#     else:
#         print('輸入不正確，請重新輸入')

# 老師寫的
# 1.先定義一個專門儲存使用者名稱的列表
data_list = []
# 2.添加循環結構
while True:
    # 3.先列印項目功能 供用戶選擇
    print("""
      1.添加用戶
      2.查看用戶
      3.刪除用戶    
      """)
    # 4.獲取用戶想要執行的功能編號
    choice_num = input('請輸入您想要執行的功能編號>>>:').strip()
    # 5.根據不同的功能編號執行不同的分支代碼
    if choice_num == '1':
        # 6.獲取用戶輸入的使用者名稱
        username = input('請輸入您的使用者名稱>>>:').strip()
        # 7.判斷當前使用者名稱是否已存在
        if username in data_list:
            print('使用者名稱已存在')
        else:
            # 8.列表添加使用者名稱
            data_list.append(username)
            print(f'使用者名稱{username}添加成功')
    elif choice_num == '2':
        # 9.循環列印每一個用戶數據
        for name in data_list:
            print(
                f"""
              ------------user info---------
              使用者名稱:{name}
              ------------------------------
              """)
    elif choice_num == '3':
        # 10.獲取用戶想要刪除的使用者名稱
        delete_username = input('請輸入您想要刪除的使用者名稱>>>:').strip()
        # 11.先判斷使用者名稱是否存在
        if delete_username in data_list:
            data_list.remove(delete_username)
            print(f'使用者名稱{delete_username}刪除成功')
        else:
            print('使用者名稱不存在!!!')
    else:
        print('很抱歉 暫時沒有您想要執行的功能編號')