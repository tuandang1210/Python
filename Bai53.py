def get_all_sublists(lst):
    sublists = [[]]
    n = len(lst)
    for i in range(n):
        for j in range(i + 1, n + 1):
            sublists.append(lst[i:j])
    return sublists

input_string = input("Nhập các số cách nhau bởi dấu cách: ")
str_list = input_string.split()
int_list = [int(x) for x in str_list]
result = get_all_sublists(int_list)
print(f"Các danh sách con của {int_list}:")
for sub in result:
    print(sub)
