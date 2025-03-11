words = []

while True:
    word = input("Nhập một từ (nhập dòng trống để kết thúc): ")
    if word == "":
        break
    if word not in words:
        words.append(word)

print("\nCác từ đã nhập (loại bỏ trùng lặp):")
for w in words:
    print(w)

