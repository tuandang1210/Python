def Good_Password(n):
    if (len(n) < 8):
        return False
    has_upper = any(c.isupper() for c in n)
    has_lower = any(c.islower() for c in n)
    has_digit = any(c.isdigit() for c in n)

    return has_upper and has_lower and has_digit

user_password = input("Nhập mật khẩu: ")

if Good_Password(user_password):
    print("Mật khẩu tốt!")
else:
    print("Mật khẩu không tốt!")