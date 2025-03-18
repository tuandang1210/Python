import math


def tinh_dien_tich_tam_giac_deu():
    a = float(input("Nhập cạnh tam giác đều: "))

    S = a ** a * math.sqrt(3) / 4

    print(f"Diện tích tam giác đều theo công thức Heron: {S:.2f}")

tinh_dien_tich_tam_giac_deu()
