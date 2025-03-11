def format_list(words):
    if not words:
        return ""
    elif len(words) == 1:
        return words[0]
    else:
        return ", ".join(words[:-1]) + " and " + words[-1]

words = input("Nhập danh sách các từ, cách nhau bởi dấu cách: ").split()

formatted_string = format_list(words)
print("Danh sách sau khi định dạng:", formatted_string)
