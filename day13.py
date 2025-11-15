

def calculate_area(width,height):
    """计算矩形面积"""
    return width * height

print(f"面积1:{calculate_area(5,10)}")


def say_hello():
    """打招呼函数 - 这是字符串文档"""
    print("你好！")

say_hello()


def greet(name):
    """打招呼函数"""
    print(f"你好，{name}！")

greet("小王")
greet("alice")

#带返回值的函数

def add(a,b):
    """求和函数"""
    result = a +b 
    return result

total = add(1,2) + add(5,5)
print(total)    

def no_return():
    """无返回值的函数"""
    print("我没有返回值")

result =  no_return()
print(result)

#函数参数

def introduce(name,age,city):
    """自我介绍"""
    print(f"我叫{name}，今年{age}岁，来自{city}")


introduce("小明",22,"BeiJing")
introduce(20,"小明","BeiJing")
introduce(20,"小明",20)


#默认参数
def greet(name,greeting = "你好"):
    """打招呼函数，可以自定义问候语"""
    print(f"{greeting},{name}")

greet("alex","吃饭没")
greet("zhangsan")


# def wrong(greting = "hello",name):
#     """错误参数顺序"""
#     print(f"{greting},{name}")

def order_coffee(size,sugar,milk):
    """点咖啡"""
    print(f"点一杯{size}杯,{sugar}糖，{'加' if milk else '不加'}奶的咖啡。")

order_coffee("大","少",True)
order_coffee(sugar="少",size="大",milk=False)
order_coffee(True,1,True)

def sum_all(*numbers):
    """计算任意数量数字的和"""
    total = 0
    for num in numbers:
        total += num

    return total

print(sum_all(1,2,3))
print(sum_all(1,2,3,4,5))

def show_args(*args):
    print(f"args的类型:{type(args)}")
    print(f"args的值:{args}")

show_args(1,2,3)

def make_pizza(size,*toppings):
    """制作披萨"""
    print(f"\n指针一个{size}寸的披萨，添加的配料有：")
    for topping in toppings:
        print(f" - {topping}")

make_pizza(6,"培根","蘑菇","洋葱")


#任意关键字参数 **kwargs

def build_profile(name,age,**other_info):
    """创建用户档案"""
    profile = {
        "name":name,
        "age":age
    }

    for key,value in other_info.items():
        profile[key] = value
    return profile

user = build_profile("小明",22,city="北京",hobby="football")

print(user)

def show_kwargs(**kwargs):
    print(f"kwargs的类型:{type(kwargs)}")
    print(f"kwargs的值:{kwargs}")

show_kwargs(name="小米",age=21)

def complex_function(pos1,pos2,default1 = "默认值",*args,key1,key2 = "默认值",**kwargs):
    """展示各种参数的组合"""
    print(f"位置参数:{pos1},{pos2}")
    print(f"默认参数:{default1}")
    print(f"可变参数:{args}")
    print(f"关键字参数:{key1},{key2}")
    print(f"可变关键字参数:{kwargs}")

complex_function(1,2,23,555,"test1","test2",key1 = "key1",f1 = "f1",f2 = "f2")

def args_test(args1,args2,default1 = "默认值",*args,args3):
    print(f"args1:{args1}")



global_var = "我是全局变量"

def test_scope():
    """测试作用域"""
    local_var = "我是局部变量"
    print(f"全局变量:{global_var}")
    print(f"局部变量:{local_var}")


test_scope()


count = 0
def increment():
    global count
    count += 1

print(count)

increment()
print(count)

increment()
print(count)



square_lambda = lambda x:x**2

print(square_lambda(5))

def get_score(student):
    return student["score"]

students = [{"name":"小王","score":90},{"name":"小张","score":80}]

sorted_students = sorted(students,key=get_score,reverse=True)
print(sorted_students)

sorted_students_lambda = sorted(students,key = lambda s:s['score'])
print(sorted_students_lambda )



numbers = [1,2,3,4,5,6,7,8,9,10]
even_numbers = list(filter(lambda x:x%2==0,numbers))
print(even_numbers)


large_numbers = list(filter(lambda x:x>5,numbers))
print(large_numbers)
    

#递归
def factorial(n):

    #1.基准条件（停止条件）- 必须有！
    if n <= 1:
        return 1
    

    # 2. 递归调用（向基准条件靠近）
    # 3. 使用递归结果
    return n *factorial(n-1)

print(factorial(5))

def power(base,exponent):
    if exponent == 0:
        return 1
    return base * power(base,exponent-1)

print(power(2,5))