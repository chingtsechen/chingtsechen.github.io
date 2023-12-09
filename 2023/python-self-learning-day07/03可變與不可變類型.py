# s1 = '$$jimmy$$'
# l1 = [11, 22, 33]
# s1.strip('$')
# print(s1.strip('$'))  # jimmy
# print(s1)  # $$jimmy$$

# ret = l1.append(44)
# print(l1)  # [11, 22, 33, 44]
# print(ret)  # None


# 可變類型:值改變 記憶體地址不變
# l1 = [11, 22, 33]
# print(l1)      # [11, 22, 33]
# print(id(l1))  # 4335317568
# l1.append(44)
# print(l1)      # [11, 22, 33, 44]
# print(id(l1))  # 4335317568

# 不可變類型:值改變 記憶體地址肯定變
# res = '$$hello world$$'
# print(res)      # $$hello world$$
# print(id(res))  # 4339363504
# res.strip('$')
# print(res)      # $$hello world$$
# print(id(res))  # 4339363504