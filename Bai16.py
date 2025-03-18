import math

def tinh_toc_do_roi():
    d = float(input("Nhập độ cao (m): "))

    a = 9.8
    vi = 0

    vf = math.sqrt(vi ** 2 + 2 * a * d)

    print(f"Tốc độ khi chạm đất: {vf:.2f} m/s")

tinh_toc_do_roi()
