letter = input("Nhập một chữ cái: ").lower()

if letter in ('a', 'e', 'i', 'o', 'u'):
    print(letter + " là một nguyên âm.")
elif letter == 'y':
    print(f"{letter} có thể là nguyên âm hoặc phụ âm.")
elif letter.isalpha() and len(letter) == 1:
    print(f"{letter} là một phụ âm.")
else:
    print("Vui lòng nhập một chữ cái hợp lệ.")