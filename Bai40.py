numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

n = len(numbers)

first_half = numbers[:n // 2]
second_half = numbers[n // 2:]

print(" ".join(map(str, first_half)))

print(" ".join(map(str, second_half)))
