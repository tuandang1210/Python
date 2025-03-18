def tinh_nang_luong():
    M = float(input("Nhập khối lượng nước (gram): "))
    delta_T = float(input("Nhập sự thay đổi nhiệt độ (°C): "))

    C = 4.186
    Q = M * C * delta_T

    Q_kWh = Q * 2.777e-7

    cost = Q_kWh * 8.9

    print(f"Năng lượng cần thiết: {Q:.2f} Joules")
    print(f"Năng lượng tương đương: {Q_kWh:.6f} kWh")
    print(f"Chi phí điện: {cost:.2f} cent")

tinh_nang_luong()
