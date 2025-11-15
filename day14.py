
import math

#使用时候要加模块前缀
print(math.pi)
print(math.sqrt(16))


print(math.ceil(4.2))


#导入特定函数 不需要前缀
from math import sqrt,pi,sqrt
print(pi)


#自己定义sqrt
def sqrt(x):
    return "我的sqrt"

print(sqrt(16))

#使用别名
import math as m
print(m.sqrt(16))

#长模块经常使用别名
import matplotlib.pyplot as plt


#函数别名
from math import factorial as fact
print(fact(5))


import random

# 随机整数

dice = random.randint(1,6)
print(f"type(dice):{type(dice)}")
print(f"骰子点数:{dice}")

# 随机浮点数
score = random.random() #0.0-1.0之间
print(f"type(score):{type(score)}")
print(f"随机分数:{score}")

score_100 = random.uniform(0,100) #0.0-100.0
print(f"type(score_100):{type(score_100)}")
print(f"随机分数:{score_100}")


# 3.随机选择
colors = ["红色","黄色","蓝色","绿色"]
lucky_color = random.choice(colors)
print(f"type(lucky_color):{type(lucky_color)}")
print(f"幸运颜色:{lucky_color}")

#4.随机抽样(不重复)
winners = random.sample(["小王","小李","小张","小赵","小孙","小李"],3)
print(f"type(winners):{type(winners)}")
print(f"中奖人员:{winners}")

cards = ['A', 'K', 'Q', 'J', '10']
random.shuffle(cards) #直接修改原列表
print(f"洗牌后:{cards}")


def generate_code(length=6):
    "生成数字验证码"
    code = ""
    for _ in range(length):
        code += str(random.randint(0,9))

    return code

print(generate_code())

import string

def generage_password(length=8):
    """生成包含数字的密码"""
    characters = string.ascii_letters +string.ascii_letters
    password = ''.join(random.choice(characters) for _ in range(length))
    return password
print(generage_password())



from datetime import datetime,date,time,timedelta

#获取当前时间
now = datetime.now()
print(f"现在:{now}")




# 2. 格式化输出
formatted = now.strftime("%Y年%m月%d日 %H:%M:%S")
print(formatted)  # 2025年11月12日 14:30:25

# 3. 获取各部分
print(f"年: {now.year}")
print(f"月: {now.month}")
print(f"日: {now.day}")
print(f"星期: {now.weekday()}")  # 0=周一, 6=周日

# 4. 创建特定日期
birthday = datetime(2000, 5, 20, 10, 30)
print(f"生日: {birthday}")


new_year = datetime(2026, 1, 1)
days_until = (new_year - now).days

print(f"距离2026年的天数: {days_until}")

def calculate_age(birth_date):
    """计算年龄"""
    today = datetime.now()
    age = today.year - birth_date.year

    if (today.month ,today.day) < (birth_date.month, birth_date.day):
        age -= 1

    return age

print(f"年龄:{calculate_age(datetime(1998,8,20))}")


def countdown_days(target_date,event_name):
    """倒计时"""
    today = datetime.now()
    day_left = (target_date - today).days
    print(f"距离{event_name}还有{day_left}天")

countdown_days(datetime(2026,1,1),"元旦")