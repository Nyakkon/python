#Bài 1: Viết một chương trình yêu cầu người dùng nhập tên của họ, sau đó in ra lời chào theo định dạng "xin chào, [Tên người dùng]"
name = input("Nhập tên của bạn : ")
print("xin chào",name)

#Bài 2: Nhập tên người dùng, tối đa 5 người dùng, sử dụng vòng lặp Zip để chào 5 người kèm độ tuổi và phải có input()
names= input("Tên người thứ 1: "), input("Tên người thứ 2: "), input("Tên người thứ 3: "), input("Tên người thứ 4: "), input("Tên người thứ 5: ")
ages=int(input("Năm sinh người thứ 1: ")), int(input("Năm sinh người thứ 2: ")), int(input("Năm sinh người thứ 3: ")), int(input("Năm sinh người thứ 4: ")), int(input("Năm sinh người thứ 5: "))
for name, age,in zip(names, ages):
    print("Xin chào,", name, "- Tuổi của bạn là", age)
#Bài 3: Sử dụng range(start, stop, step) và phải sử dụng input
start = int(input("Nhập giá trị bắt đầu: "))
stop = int(input("Nhập giá trị kết thúc: "))
step = int(input("Nhập bước nhảy: "))

for i in range(start, stop, step):
    print(i)
