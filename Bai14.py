import math

def tinh_toan_hai_so():
    a = int(input("Nhập số nguyên a: "))
    b = int(input("Nhập số nguyên b: "))

    tong = a + b
    print(f"Tổng (a + b) = {tong}")

    hieu = a - b
    print(f"Hiệu (a - b) = {hieu}")

    tich = a * b
    print(f"Tích (a * b) = {tich}")

    if b != 0:
        thuong = a / b
        print(f"Thương (a / b) = {thuong}")
    else:
        print("Không thể chia cho 0, không tính được thương!")

    if b != 0:
        phan_du = a % b
        print(f"Phần dư (a % b) = {phan_du}")
    else:
        print("Không thể chia cho 0, không tính được phần dư!")

    if a > 0:
        log_a = math.log(a,10)
        print(f"log10(a) = {log_a}")
    else:
        print("Không thể tính log10(a) vì a không lớn hơn 0!")

    luy_thua = a ** b
    print(f"a^b = {luy_thua}")

tinh_toan_hai_so()
