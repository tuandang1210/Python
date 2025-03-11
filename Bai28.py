month = int(input("Nhập tháng : "))

days_in_month = {
    1: "31 ngày",
    2: "28 hoặc 29 ngày",
    3: "31 ngày",
    4: "30 ngày",
    5: "31 ngày",
    6: "30 ngày",
    7: "31 ngày",
    8: "31 ngày",
    9: "30 ngày",
    10: "31 ngày",
    11: "30 ngày",
    12: "31 ngày"
}

if month in days_in_month:
    print(f"tháng {month} có {days_in_month[month]}.")
else:
    print("tháng không hợp lệ. Vui lòng nhập lại.")
