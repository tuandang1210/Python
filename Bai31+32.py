def caesar_cipher(message, shift, mode):
    result = ""
    for char in message:
        if char.isalpha():
            if char.isupper():
                base = ord('A')
            else:
                base = ord('a')

            if mode == 'encode':
                new_char = chr((ord(char) - base + shift) % 26 + base)
            elif mode == 'decode':
                new_char = chr((ord(char) - base - shift) % 26 + base)
            result += new_char
        else:
            result += char
    return result

choice = input("Chọn chức năng: mã hóa (E) hoặc giải mã (D): ").strip().lower()
message = input("Nhập tin nhắn: ")
shift = int(input("Nhập số ký tự dịch chuyển: "))

if choice == 'e':
    encoded_message = caesar_cipher(message, shift, 'encode')
    print("Tin nhắn đã được mã hóa:", encoded_message)
elif choice == 'd':
    decoded_message = caesar_cipher(message, shift, 'decode')
    print("Tin nhắn đã được giải mã:", decoded_message)
else:
    print("Chức năng không hợp lệ. Vui lòng chọn E để mã hóa hoặc D để giải mã.")
