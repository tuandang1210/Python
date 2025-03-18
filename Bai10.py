
def tinh_dien_tich_phong():
    chieu_dai = float(input("Nhập chiều dài của căn phòng (m): "))
    chieu_rong = float(input("Nhập chiều rộng của căn phòng (m): "))

    dien_tich = chieu_dai * chieu_rong

    print(f"Diện tích căn phòng: {dien_tich:.2f} mét vuông")

tinh_dien_tich_phong()
