import random

def generate_password():
    length = random.randint(7, 10)
    password = "".join(chr(random.randint(33, 126)) for _ in range(length))
    return password

print("Mật khẩu ngẫu nhiên được tạo:", generate_password())
