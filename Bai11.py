
def tinh_dien_tich_canh_dong():
    chieu_dai = float(input("Nhập chiều dài của cánh đồng (m): "))
    chieu_rong = float(input("Nhập chiều rộng của cánh đồng (m): "))

    dien_tich_m2 = chieu_dai * chieu_rong
    dien_tich_acre = dien_tich_m2 / 43560

    print(f"Diện tích cánh đồng: {dien_tich_acre:.4f} mẫu Anh")

tinh_dien_tich_canh_dong()