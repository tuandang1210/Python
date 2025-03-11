def compare_strings(s1, s2):
    if len(s1) > len(s2):
        print(s1)
    elif len(s2) > len(s1):
        print(s2)
    else:
        print(s1)
        print(s2)

str1 = input("Nhập chuỗi thứ nhất: ")
str2 = input("Nhập chuỗi thứ hai: ")

compare_strings(str1, str2)
