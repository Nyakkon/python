#bai1
number = int(input("Nhập một số: "))
total = 0
i = 1

while i <= number:
    total += i
    i += 1

print("Tổng các số từ 1 đến", number, "là:", total)
