def is_palindrome(s):
    s = s.strip()
    for i in range(len(s) // 2):
        if s[i] != s[len(s) - 1 - i]:
            return False
    return True

user_input = input("Nhập một chuỗi: ")

if is_palindrome(user_input):
    print(f"Chuỗi '{user_input}' là Palindrome.")
else:
    print(f"Chuỗi '{user_input}' không phải là Palindrome.")
