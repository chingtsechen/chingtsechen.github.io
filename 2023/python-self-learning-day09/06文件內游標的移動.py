# he天氣這麼冷 腦袋都凍了 不想學習了
# he天氣這麼冷 腦袋都凍了 不想學習了
# he天氣這麼冷 腦袋都凍了 不想學習了

# with open(r'a.txt', 'r', encoding='utf8') as f:
#     print(f.read(3))
#     print(f.read(3))

# with open(r'a.txt', 'rb') as f:
#     print(f.read(5).decode('utf8'))  # 二進制模式下 3 是字節的意思  # he天
#     print(f.read(3).decode('utf8'))  # 氣

with open(r'a.txt', 'rb') as f:
    print(f.read())
    f.seek(0,0)
    print(f.read())
    f.seek(0, 0)
    print(f.read())
    # print(f.read(2).decode('utf-8'))
    # f.seek(-6, 2)
    # print(f.tell())  # 返回游標距離文件開頭產生的位元組數
    """
    seek(offset, whence)
        offset是位移量 以位元組為單位
        whence是模式   0  1  2
            0是基於文件開頭
                文本和二進位制模式都可以使用
            1是基於當前位置
                只有二進位制模式可以使用
            2是基於文件末尾
                只有二進位制模式可以使用
    """
    # print(f.read(3).decode('utf-8'))
