def print_last_five_squares():
    squares = []
    for i in range(1, 21):
        squares.append(i ** 2)
    last_five = squares[15::]
    a = squares[5::]
    print("5 phần tử cuối trong danh sách:", last_five, a)

print_last_five_squares()