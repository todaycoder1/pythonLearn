

# name = input("请输入你的名字：")
# print("你好, " + name + "!")


# print(f"welcome {name} to python world!")

# age = int(input("请输入你的年龄："))
# print(f"{name}，你今年{age}岁")


values = input("请输入三个用逗号分隔的数字：")
print("type:",type(values))
print("values:",values)
print("values[0]:",values[0])
print("values[2]:",values[2])


numbers = values.split(" ")
print("numbers:",numbers)
print("type:",type(numbers))

print("numbers[0]:",numbers[0])


text = "apple,,banana,cherry"
fruits = text.split(",")
print(fruits)
print("types(fruits):",type(fruits))
print("len(fruits):",len(fruits))

for fruit in fruits:
    print(fruit)



text = "apple,,banana,orange"
result = text.split(',')
print(result)


text = ",apple,banana,orange,"
result =  text.split(",")
print(result)


text = "apple  banana orange"
result = text.split()
print(result)


with open("diary.txt","w",encoding="utf-8") as file:
    file.write("this is my first diary\n")
    # file.read()  # 这里会报错，因为文件是以写模式打开的，不能读取内容
    file.write("今天学习了Python输入输出\n")

with open("diary.txt","r",encoding="utf-8") as file:
    context = file.read()
    print("文件内容:")
    print(context)

with open("diary.txt","r",encoding="utf-8") as file:
    lines = file.readlines()
    for line in lines:
        print("行内容:",line.strip())  # 使用strip()去除行末的换行符

with open("diary.txt","a",encoding="utf-8") as file:
    file.write("今天学习了文件操作\n")
    file.write("这是追加的内容\n")
 