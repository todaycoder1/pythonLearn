
students = {'name':'John', 'age':21, 'courses':['Math', 'CompSci']}

empty_dict = {}
dict_from_list = dict([('name','Alice'), ('age',20)])  # Creating a dictionary from a list of tuples


print(students['name'])
print(students.get('age'))  # Using get() method to access age



print(students.keys())    # Get all keys
print(type(students.keys()))  # Type of keys view
print(students.values())  # Get all values
print(type(students.values()))  # Type of values view

print(students.get('height','40'))


print(students.items())  # Get all key-value pairs

print(students)

print(students.values())

print(dict_from_list)

students['age'] = 22  # Update age
students['height'] = 180  # Add new key-value pair
print(students) 


students.update({"name":"Mike", "age":23, "weight":75})  # Update multiple key-value pairs
print(students)

del students['age']
print(students)

students['agende'] = "womanw "
print(students)


students.pop('height')  # Remove key 'height'
print(students)


for key in students:
    print(key)  # Print each key
    print('---')
    print(students[key])
    print(f"{key}: {students[key]}")  # Print key and its value

for key,value in students.items():
    print(f"{key}: {value}")  # Print key and value using items()