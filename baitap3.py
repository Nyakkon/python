#sử dụng if else
# Viết chương trình Python tính giá trị trung bình (avg) của ba biến a, b, c nhập từ bàn phím (a, b, c là ba số tự nhiên) với điều kiện như sau:

# Nếu avg > a và avg > b thì hiển thị The average value is greater than both a and b
# Nếu avg > a và avg > c thì hiển thị The average value is greater than both a and c
# Nếu avg > b và avg > c thì hiển thị The average value is greater than both b and c
# Nếu avg chỉ lớn hơn a thì hiển thị The average value is greater than a
# Nếu avg chỉ lớn hơn b thì hiển thị The average value is greater than b
# Nếu avg chỉ lớn hơn c thì hiển thị The average value is greater than c
# Ví dụ:

# Nếu a = 10, b = 20, c = 20 thì màn hình hiển thị The average value is greater than a 
# Giải thích: avg = (10+20+20)/3 = 20 nên avg chỉ lớn hơn a.

# Dùng input()
a = int(input("Nhập giá trị của a: "))
b = int(input("Nhập giá trị của b: "))
c = int(input("Nhập giá trị của c: "))

avg = (a + b + c) / 3

if avg > a and avg > b:
    print("The average value is greater than both a and b")
elif avg > a and avg > c:
    print("The average value is greater than both a and c")
elif avg > b and avg > c:
    print("The average value is greater than both b and c")
elif avg > a:
    print("The average value is greater than a")
elif avg > b:
    print("The average value is greater than b")
elif avg > c:
    print("The average value is greater than c")
