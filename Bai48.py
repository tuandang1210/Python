def average(a, b, c):
    return (a + b + c) / 3

num1 = float(input("Nhập số thứ nhất: "))
num2 = float(input("Nhập số thứ hai: "))
num3 = float(input("Nhập số thứ ba: "))

avg = average(num1, num2, num3)
print(f"Giá trị trung bình của {num1}, {num2} và {num3} là: {avg}")
