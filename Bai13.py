def tinh_tong_n():
    n = int(input("Nhập một số nguyên dương n: "))
    if n <= 0:
        print("Vui lòng nhập một số nguyên dương!")
        return

    tong = n * (n + 1) // 2

    print(f"Tổng của tất cả các số nguyên từ 1 đến {n} là: {tong}")

tinh_tong_n()
