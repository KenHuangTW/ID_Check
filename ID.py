# 目的: 確定身分證字號是否符合行政院編碼規則
# 備註: 外籍人士的身分證字號有兩種，第一種為舊式兩碼英文，第二種為新式比照台灣國人辦理，但性別碼部分有所不同
#      ，目前有過渡期的狀況，所以必須將兩種情況納入。
# 備註2: 台灣舊式身分證字號已經被廢除，皆已全面換發


def check_id_number(id_number):
    # 這邊就先判斷第一碼是否為大寫英文字母, 用str.istitle會出現錯誤
    # 這邊先擋下第3 ~ 10碼輸入英文字母的狀況, 後面才做程式會出錯誤
    try:
        if type(id_number) != str:  # 檢驗使用者輸入的格式是否正確
            return "格式錯誤!!!"
        # 以下先判斷使用者是否輸入正確的身分證字號
        if id_number[0].isupper() != True or len(id_number) != 10 or id_number[2:9].isdigit() != True:
            return "非正確身分證字號，請重新輸入"
        male_or_female = {"1", "2", "8", "9"}  # 第二碼 - 性別碼的規則，8、9是外國人的
        foreigner_male_or_female = {"A", "B", "C", "D"}  # 外籍人士第二碼 - 性別碼的規則
        # 以下為有效身分證字號所需資料 #

        a = {"A": "10", "B": "11", "C": "12", "D": "13", "E": "14", "F": "15", "G": "16", "H": "17",  # 英文對應的數字
             "I": "34", "J": "19", "K": "20", "M": "21", "N": "22", "O": "35", "P": "23", "Q": "24",
             "R": "25", "S": "26", "T": "27", "U": "28", "V": "29", "W": "32", "X": "30", "Y": "31",
             "Z": "33"}

        if id_number[1].isupper():  # 判斷是否為外籍人士的舊款身分證字號
            f_one = a.get(id_number[0])  # 轉換第一個英文字母數值
            f_two = a.get(id_number[1])  # 轉換第二個英文字母數值
            foreigner_number_ten = int(f_one[0]) * 1 + int(f_one[1]) * 9 + int(f_two) * 8 + int(id_number[2]) * 7 + \
                                   int(id_number[3]) * 6 + int(id_number[4]) * 5 + int(id_number[5]) * 4 + \
                                   int(id_number[6]) * 3 + int(id_number[7]) * 2 + \
                                   int(id_number[8]) * 1 + int(id_number[9]) * 1
            d = foreigner_number_ten % 10  # 整除10代表為有效身分證字號
            if id_number[1] in foreigner_male_or_female or d == 0:  # 是否符合規範
                return "Conform"
            else:
                return "Error"
        else:  # 本國籍人士
            b = a.get(id_number[0])  # 取得數值
            number_ten = int(b[0]) * 1 + int(b[1]) * 9 + int(id_number[1]) * 8 + int(id_number[2]) * 7 + \
                         int(id_number[3]) * 6 + int(id_number[4]) * 5 + \
                         int(id_number[5]) * 4 + int(id_number[6]) * 3 + int(id_number[7]) * 2 + \
                         int(id_number[8]) * 1 + int(id_number[9]) * 1
            c = number_ten % 10  # 整除10代表為有效身分證字號
            if id_number[1] in male_or_female and id_number[2:10].isdigit and c == 0:  # 是否符合規範
                return "符合"
            else:
                return "不符合"
    except Exception as e:  # 預防錯誤，但目前常犯的錯誤已經都先寫在上面了
        pass