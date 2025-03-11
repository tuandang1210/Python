numbers = []

while True:
    n = int(input("Nhập một số nguyên (nhập 0 để kết thúc): "))
    if n == 0:
        break
    numbers.append(n)

numbers.sort()

print("Các số đã nhập theo thứ tự tăng dần:")
for number in numbers:
    print(number)
