def tinh_tong_tien():
    chi_phi = float(input("Nhập chi phí bữa ăn (VNĐ): "))

    thue = chi_phi * 0.05
    tien_boa = chi_phi * 0.18
    tong_tien = chi_phi + thue + tien_boa

    print(f"Tiền thuế: {thue:.2f} VNĐ")
    print(f"Tiền boa: {tien_boa:.2f} VNĐ")
    print(f"Tổng số tiền phải trả: {tong_tien:.2f} VNĐ")

tinh_tong_tien()
