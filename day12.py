numbers = [1,2,3,4,5]

squares = [x**2 for x in numbers]
print(squares)

even_squares = [x**2 for x in numbers if x%2==0]
print(even_squares)

labes = ["偶数" if x%2 == 0 else "奇数" for x in numbers]
print(labes)

matrix = [[1,2,3],[4,5,6],[7,8,9]]
flattened = [num for row in matrix for num in row]
print(flattened)


squares_dict = {x: x**2 for x in range(1,6)}
print(squares_dict)

uniques_squares = {x**2 for x in [1,2,3,4,3,2,5,6]}
print(uniques_squares)


for i in range(3):
    for j in range(2):
        print(f"i={i},j={j}")


matrix = [[1,2,3],[4,5,6],[7,8,9]]

print("矩阵内容:")
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        print(f"matrix[{i}][{j}] = {matrix[i][j]}",end =" ")
    print()


def print_pattern(n):
    "打印三角形图案"
    for i in range(1,n+1):
        for j in range(i):
            print("*",end=" ")
        print()

print_pattern(5)