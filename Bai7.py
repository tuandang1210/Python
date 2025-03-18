import math

def tinh_dien_tich_tam_giac():
    a = float(input("Nhập cạnh a: "))
    b = float(input("Nhập cạnh b: "))
    c = float(input("Nhập cạnh c: "))
    A = float(input("Nhập góc A (độ): "))
    B = float(input("Nhập góc B (độ): "))
    C = float(input("Nhập góc C (độ): "))

    S1 = 0.5 * a * b * math.sin(math.radians(C))
    S2 = 0.5 * a * c * math.sin(math.radians(B))
    S3 = 0.5 * b * c * math.sin(math.radians(A))

    print(f"Diện tích tam giác theo công thức S = 1/2 * ab * sin(C): {S1:.2f}")
    print(f"Diện tích tam giác theo công thức S = 1/2 * ac * sin(B): {S2:.2f}")
    print(f"Diện tích tam giác theo công thức S = 1/2 * bc * sin(A): {S3:.2f}")

tinh_dien_tich_tam_giac()
