#Viết một chươg trình yêu cầu người dùng nhập vào cân nặng kg (sử dụng float) và chiều cao (m), sau đó tính chỉ số BMI và in ra thông báo tương ứng
# bmi < 18.5 (Dưới chuẩn)
# 18.5 nhỏ hơn hoặc bằng bmi nhỏ hơn 25 (Bình thưởng)
# 25 nhỏ hơn hoặc bằng bmi nhỏ hơn 30 (Thừa cân)
# Trường hợp còn lại = Béo phì

weight = float(input("Nhập cân nặng của bạn: "))
height = float(input("Nhập chiều cao của bạn: "))

bmi = weight / (height**2)


if bmi < 18.5:
    print("Dưới chuẩn")

elif bmi <= 25:
    print("BMI của bạn là", bmi, "- Bình thường")
elif 25 < bmi < 30:
    print("Thừa cân")
else:
    print("BMI của bạn là", bmi, "- Béo phì")
    
