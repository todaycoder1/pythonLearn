count = 0

while count < 5:
    print(count)
    count += 1


password = ""
while password != "secret":
    password = input("请输入密码:")
print("密码正确")


while True:
    user_input = input("请输入命令(按quit退出)")
    if user_input == "quit":
        break
    print("执行命令")

number = 0
while number < 10:
    number += 1
    if number % 2 == 0:
        continue
    print(number)


def process_number():
    numbers = []
    total = 0

    while total < 100:
        try:
            num = int(input("请输入数字(输入0结束):"))
            if num == 0:
                break
            numbers.append(num)
            total += num
            print(f"当前输入的数字为:{num}")
            print(f"当前输入的数字和:{total}")
        except:
            print("输入错误，请重新输入")
    
    print(f"最终输入结果为：{numbers}，总和为：{total}")


process_number()




# 6. 循环的else子句
def find_number(target):
    numbers = [1,3,5,7,9]
    index = 0

    while index < len(numbers):
        if numbers[index] == target:
            print(f"找到目标数字:{target}")
            break
        index += 1
    else:
        print(f"没有找到目标数字:{target}")

    


find_number(10)