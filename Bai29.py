
a = float(input("Nhập độ dài cạnh thứ nhất: "))
b = float(input("Nhập độ dài cạnh thứ hai: "))
c = float(input("Nhập độ dài cạnh thứ ba: "))

if a + b <= c or a + c <= b or b + c <= a:
    print("Ba cạnh không tạo thành một tam giác hợp lệ!")
else:
    if a == b == c:
        print("Đây là tam giác đều.")
    elif a == b or a == c or b == c:
        print("Đây là tam giác cân.")
    else:
        print("Đây là tam giác thường (không có cạnh nào bằng nhau).")