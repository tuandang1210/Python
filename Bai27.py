sides = int(input("Nhập số cạnh của hình: "))

if 3 <= sides <= 10:
    shape_names = {
        3: "hình tam giác",
        4: "hình tứ giác",
        5: "hình ngũ giác",
        6: "hình lục giác",
        7: "hình thất giác",
        8: "hình bát giác",
        9: "hình cửu giác",
        10: "hình thập giác"
    }
    print(f"Số cạnh {sides} là {shape_names[sides]}.")
else:
    print("Số cạnh không hợp lệ. Vui lòng nhập số từ 3 đến 10.")