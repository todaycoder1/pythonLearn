


print("hello")


# print(undedined_variable) #name error


# "2" +2  #TypeError

  
# int("hello") #ValueError


# arr = [1, 2, 3]
# print(arr[6]) #IndexError


try:
    num = int(input("Enter a number: "))
    result = 100/num
    print(f"100 / {num} = {result}")
except ValueError:
    print("输入的不是有效数字")
except ZeroDivisionError:
    print("不能除以零")
except Exception as e:
    print(f"发生 错误：{e}")
else:
    print("计算成功")
finally:
    print("程序执行完毕")

def calculate_average(numbers):
    print(f"调试:输入的数据 = {numbers}")
    if not numbers:
        print("调试:空列表，返回0")
        return 0
    
    total = sum(numbers)
    count = len(numbers)
    print(f"调试:求和结果 = {total}, 数量 = {count}")
    

calculate_average((1,2,3))


def get_valid_input(promt,input_type=str,validation_func=None):
    while True:
        try:
            user_input = input(promt)
            if input_type != str:
                user_input = input_type(user_input)

            if validation_func and not validation_func(user_input):
                print("输入不符合要求，请重试。")
                continue

            return user_input
        except ValueError:
            print(f"请输入一个有效的{input_type.__name__}类型")
    
get_valid_input("我试试") #对于这个函数的运行有点疑问



def calulcate_discount(price,discount_rate):

    assert price >= 0 , "价格不能小于0"

    discount_price = price * (1-discount_rate)

    assert discount_price >= 0, "折扣价格不能小于0"
    assert discount_price <= price, "折扣价格不能大于原价"

    print(f"折扣价格：{discount_price}")
    return discount_price



try:
    print(calulcate_discount(100,0.2))
    print(calulcate_discount(-50,0.2))
except AssertionError as e:
    print(f"断言错误：{e}")


import pdb


def complex_calculation(data):
    print("Starting complex calculation...")

    #设置断点
    pdb.set_trace()

    total = 0
    count = 0

    for item in data:
        pdb.set_trace()

        if isinstance(item,(int,float)):
            total += item
            count += 1
        else:
            print(f"跳过非数字项：{item}")

    if count > 0:
        average = total / count
        print(f"平均值：{average}")
    else:
        print("没有有效的数字项")

    return average


test_data = [10,20,"invalid",30,40]
result = complex_calculation(test_data)