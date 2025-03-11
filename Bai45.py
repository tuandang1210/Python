def print_first_five_squares():
    squares = []
    for i in range(1, 21):
        squares.append(i ** 2)
    first_five = squares[0:5]
    print("5 phần tử đầu tiên trong danh sách:", first_five)

print_first_five_squares()
