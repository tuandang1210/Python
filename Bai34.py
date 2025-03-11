decimal = int(input("Nhập một số nguyên: "))

if decimal == 0:
    binary = "0"
else:
    binary = ""
    n = decimal
    while n > 0:
        remainder = n % 2
        binary = str(remainder) + binary
        n = n // 2

print(f"Số {decimal} chuyển thành nhị phân là: {binary}")
