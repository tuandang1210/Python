import sys

def is_perfect_number(n):
    total = 0
    for i in range(1, n):
        if n % i == 0:
            total += i
    return total == n

n = int(input("Nhập số nguyên dương: "))
if n <= 0 or n > 10000:
    sys.exit("Lỗi: Giá trị không hợp lệ, chương trình kết thúc.")
if is_perfect_number(n):
    print(f"{n} là số hoàn hảo!")
else:
    print(f"{n} không phải là số hoàn hảo!")
