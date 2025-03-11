numbers = []

while True:
    line = input("Nhập một số nguyên (hoặc nhập dòng trống để kết thúc): ")
    if line == "":
        break
    numbers.append(int(line))

negatives = []
zeros = []
positives = []

for n in numbers:
    if n < 0:
        negatives.append(n)
    elif n == 0:
        zeros.append(n)
    else:
        positives.append(n)

result = negatives + zeros + positives

print("Kết quả:", " ".join(map(str, result)))
