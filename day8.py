age = 18
if age >= 18:
    print("You are an adult.")

print("程序继续运行")


temperature = 30
if temperature > 25:
    print("天气很热")
else:
    print("天气还不错")


a = 10
b = 20

print(a > b)
print(a >= b)
print(a < b)
print(a <= b)
print(a == b)
print(a != b)

score = 85
attendence = 0.9

if score >= 60 and attendence >= 0.8:
    print("你通过了考试")
else:
    print("你没有通过考试")

age = 16
patent_permission = True

if age >= 18 or patent_permission:
    print("你可以观看这部电影")
else:
    print("你不可以观看这部电影")

is_rainy = False
if not is_rainy:
    print("今天天气晴朗,可以出门")
else:
    print("今天下雨了,带伞")

income = 50000
credit_score = 700
employment = True

if (income >= 40000 and credit_score >= 650) or employment:
    print("贷款申请通过")
else:
    print("贷款申请被拒绝")