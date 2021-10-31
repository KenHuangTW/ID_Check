import tkinter as tk
from ID_Checker.ID import check_id_number

# 主視窗建立以及設定
win = tk.Tk()
win.title("ID Checker")  # 標題
win.geometry("600x200")  # 大小
win.resizable(False, False)  # 禁止縮放
win.iconbitmap(r"C:\Users\wtf81\PycharmProjects\pythonProject\ID_Checker\nobody.ico")  # 程式圖示
win.config(bg="skyblue")  # 主視窗背景顏色

# 根據輸入結果來判斷真偽
54f6dsa465f4asd6f465

def button_command():
    id_number = en_id.get()  # 取得輸入的資料
    check_result = check_id_number(id_number)
    if check_result == "Conform" or check_result == "符合":
        def change_t():
            result.config(text="符合標準!!\nTure ID", fg="Green")
    elif check_result == "Error" or check_result == "不符合":
        def change_f():
            result.config(text="不是真正的身分證字號!!\nFake ID!!", fg="Red")
    elif check_result == "格式錯誤!!!":
        def change_e():
            result.config(text="資料格式錯誤!!", fg="Orange")
    elif check_result == "非正確身分證字號，請重新輸入":
        def change_n():
            result.config(text="身份證字號格式錯誤", fg="Orange")


# 輸入身分證
en_id = tk.Entry(width="15")
en_id.pack()

# 建立按鈕
btn = tk.Button(text="Check ID Now", command=button_command())
btn.config(bg="Gray", width="12", height="2")
btn.pack()

# 介面上的文字
txt = "This is ID Checker\n I can check Taiwanese ID number and foreigner's in Taiwanese ID number"
lab = tk.Label(bg="skyblue", fg="Black", text=txt, width="80", height="5")
lab.pack()
result = tk.Label(bg="skyblue", fg="Black", text="Result", font="1")
result.pack()

# 常駐主視窗
win.mainloop()