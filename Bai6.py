import math

def tinh_the_tich_hinh_tru():
    r = float(input("Nhập bán kính đáy (r): "))
    h = float(input("Nhập chiều cao (h): "))

    V = math.pi * r ** 2 * h
    print(f"Thể tích hình trụ là: {V:.2f}")


# Gọi hàm để chạy chương trình
tinh_the_tich_hinh_tru()
