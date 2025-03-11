numbers = input("Nhập các số, cách nhau bằng dấu phẩy: ")

number_list = [int(num.strip()) for num in numbers.split(",")]

odd_numbers = [num for num in number_list if num % 2 != 0]

print("Các số lẻ là:", ", ".join(map(str, odd_numbers)))
