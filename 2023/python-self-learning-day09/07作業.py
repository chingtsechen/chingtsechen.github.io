# 1.編寫簡易版本的拷貝工具
#      自己輸入想要拷貝的數據路徑 自己輸入拷貝到哪個地方的目標路徑
#      任何類型數據皆可拷貝
#      ps:個別電腦C槽文件由於權限問題可能無法拷貝 換其他盤嘗試即可





# 2.利用文件充當資料庫編寫用戶登錄、註冊功能
#   檔案名稱:userinfo.txt
#   基礎要求:
#          用戶註冊功能>>>:文件內添加用戶數據(使用者名稱、密碼等)
#        用戶登錄功能>>>:讀取文件內用戶數據做校驗
#       ps:上述功能只需要實現一次就算過關(單用戶) 文件內始終就一個用戶資訊
#   拔高要求:
#        用戶可以連續註冊
#       用戶可以多帳號切換登入(多用戶)  文件內有多個用戶資訊
#       ps:思考多用戶數據情況下如何組織文件內數據結構較為簡單
#     提示:本質其實就是昨天作業的第二道題 只不過資料庫由數據類型變成文件