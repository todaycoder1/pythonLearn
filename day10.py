

fruits = ['apple', 'banana', 'cherry', 'grape']

for fruit in fruits:
    print("水果:", fruit)


for c in "hello":
    print("字母:", c)

for i in range(5):
    print(i)


print("----")
for i in range(2,6):
    print(i)

print("reverse ---")
for i in range(10,1,-1):
    print(i)

students = {"Alice": 85, "Bob": 92, "Charlie": 78}


for name in students:
    print(name, "的分数是", students[name])
print("key,value----")
for name,score in students.items():
    print(name, "的分数是", score)


for value in students.values():
    print("分数:", value)


for index,fruit in enumerate(fruits):
    print("索引:", index, "水果:", fruit)

for index,fruit in enumerate(fruits,start=1):
    print(f"第{index}个水果是 {fruit}")

names = ["Alice", "Bob", "Charlie"]
scores = [85, 92, 78]
for name,scores in zip(names,scores):
    print(name,"的分数是",scores)
    