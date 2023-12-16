# 我自己寫的
# 1.最佳化員工管理系統
# emp_data_dict = {}
# while True:
#     print("""
#     1.創建員工資訊
#     2.查看單個員工
#     3.查看所有員工
#     4.修改員工薪資
#     5.刪除員工資訊
#     """)
#     choice = input("請輸入選項(q)：")
#     if choice == 'q':
#         break
#     # 1.創建員工資訊
#     if choice == "1":
#         while True:
#             emp_id = input("請輸入創建的員工ID(q)：").strip()
#             if emp_id == 'q':
#                 break
#             if not emp_id.isdigit():
#                 print("員工ID必須是純數字!")
#                 continue
#             if emp_id in emp_data_dict:
#                 print("員工ID已存在!")
#                 continue
#             emp_name = input("請輸入員工姓名：").strip()
#             emp_age = input("請輸入員工年齡：").strip()
#             emp_job = input("請輸入員工職位：").strip()
#             emp_salary = input("請輸入員工薪資：").strip()
#             tmp_emp_dict = {}
#             tmp_emp_dict['emp_id'] = emp_id
#             tmp_emp_dict['name'] = emp_name
#             tmp_emp_dict['age'] = emp_age
#             tmp_emp_dict['job'] = emp_job
#             tmp_emp_dict['salary'] = emp_salary
#             emp_data_dict[emp_id] = tmp_emp_dict
#             print(f'員工{emp_name}創建完成')
#     # 2.查看單個員工
#     elif choice == "2":
#         while True:
#             choice_id = input("請輸入要查看的員工ID(q)：").strip()
#             if choice_id == 'q':
#                 break
#             if not choice_id.isdigit():
#                 print("員工ID必須是純數字!")
#                 continue
#             if choice_id not in emp_data_dict:
#                 print("員工ID不存在!")
#                 continue
#             emp_choice_dict = emp_data_dict[choice_id]
#             print(f"""
#             員工編號：{emp_choice_dict['emp_id']}
#             員工姓名：{emp_choice_dict['name']}
#             員工年齡：{emp_choice_dict['age']}
#             員工職位：{emp_choice_dict['job']}
#             員工薪資：{emp_choice_dict['salary']}
#             """)
#     # 3.查看所有員工
#     elif choice == "3":
#         for value in emp_data_dict.values():
#             print(f"""
#             員工編號：{value['emp_id']}
#             員工姓名：{value['name']}
#             員工年齡：{value['age']}
#             員工職位：{value['job']}
#             員工薪資：{value['salary']}
#             """)
#     # 4.修改員工薪資
#     elif choice == "4":
#         while True:
#             choice_id = input("請輸入要修改的員工ID(q)：").strip()
#             if choice_id == 'q':
#                 break
#             if not choice_id.isdigit():
#                 print("員工ID必須是純數字!")
#                 continue
#             if choice_id not in emp_data_dict:
#                 print("員工ID不存在!")
#                 continue
#             change_salary = input("請輸入要修改的薪資：").strip()
#             if not change_salary.isdigit():
#                 print("薪資必須是純數字!")
#                 continue
#             user_dict = emp_data_dict[choice_id]
#             user_dict['salary'] = change_salary
#             emp_data_dict[choice_id] = user_dict
#             emp_choice_dict = emp_data_dict[choice_id]
#             print(f"""
#             員工編號：{emp_choice_dict['emp_id']}
#             員工姓名：{emp_choice_dict['name']}
#             員工年齡：{emp_choice_dict['age']}
#             員工職位：{emp_choice_dict['job']}
#             員工薪資：{emp_choice_dict['salary']}
#             """)
#     # 5.刪除員工資訊
#     elif choice == "5":
#         while True:
#             choice_id = input("請輸入要刪除的員工ID(q)：").strip()
#             if choice_id == 'q':
#                 break
#             if not choice_id.isdigit():
#                 print("員工ID必須是純數字!")
#                 continue
#             if choice_id not in emp_data_dict:
#                 print("員工ID不存在!")
#                 continue
#             del emp_data_dict[choice_id]
#             print(f'員工ID：{choice_id}已刪除')
#     # 輸入非1~5 選項
#     else:
#         print("無效的選項")



# 我自己寫的
# 2.去重下列列表並保留數據值原來的順序
#   eg: [1,2,3,2,1] 去重之後 [1,2,3]
# l1 = [2, 3, 2, 1, 2, 3, 2, 3, 4, 3, 4, 3, 2, 3, 5, 6, 5]
#
# new_list = []
# for i in l1:
#     if i not in new_list:
#         new_list.append(i)
# print(new_list)


# 我自己寫的
# 3.有如下兩個集合，pythons是報名python課程的學員名字集合，linuxs是報名linux課程的學員名字集合
# 　　pythons={'jimmy','oscar','kevin','ricky','gangdan','biubiu'}
# 　　linuxs={'kermit','tony','gangdan'}
# 　　1. 求出即報名python又報名linux課程的學員名字集合
# 　　2. 求出所有報名的學生名字集合
# 　　3. 求出只報名python課程的學員名字
# 　　4. 求出沒有同時這兩門課程的學員名字集合

# pythons={'jimmy','oscar','kevin','ricky','gangdan','biubiu'}
# linuxs={'kermit','tony','gangdan'}
# print(pythons | linuxs)  # {'kermit', 'kevin', 'tony', 'jimmy', 'ricky', 'gangdan', 'oscar', 'biubiu'}
# print(pythons & linuxs)  # {'gangdan'}
# print(pythons - linuxs)  # {'kevin', 'jimmy', 'ricky', 'oscar', 'biubiu'}
# print(pythons ^ linuxs)  # {'kermit', 'kevin', 'tony', 'jimmy', 'ricky', 'oscar', 'biubiu'}


# 我自己寫的
# 4.統計列表中每個數據值出現的次數並組織成字典展示
#   eg: l1 = ['jimmy','jimmy','kevin','oscar']
#       結果:{'jimmy':2,'kevin':1,'oscar':1}
#   真實數據
# l1 = ['jimmy', 'jimmy', 'kevin', 'oscar', 'kevin', 'tony', 'kevin']
#
# new_dict = {}
# for name in l1:
#     if name in new_dict:
#         new_dict[name] += 1
#     else:
#         new_dict[name] = 1
# print(new_dict)