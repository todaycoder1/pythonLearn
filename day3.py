fruits = ["apple", "banana", "cherry", "strawberry", "kiwi"]

print(fruits[0])
# print(fruits[5]) 越界访问会报错
print(fruits[-5])
# print(fruits[-6]) 越界访问会报错


print(fruits[1:4])
print(fruits[:4])
print(fruits[6:])
print(fruits[-1:4])
print(fruits[-4:-1])
print(fruits[-4:3])


print(fruits[3:2])


print(fruits[::])


print(fruits[1:4:-1])


fruits.append("orange")
print(fruits)


fruits.insert(1, "grape")
print(fruits)

fruits.remove("banana")
print(fruits)   

fruits.insert(0, "banana")
print(fruits)

poped = fruits.pop()
print("popped fruit:", poped)

fruits.sort()
print("sorted fruits:", fruits)



fruits.reverse()
print("reversed fruits:", fruits)   

fruits.sort(reverse=True)
print("reverse sorted fruits:", fruits)


print("number of fruits:", len(fruits))