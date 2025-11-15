import sys
import time


my_list = ["abc",2,3,4,5]
my_tuple = ("abc",2,3,4,5)


print(f"list's memory: {sys.getsizeof(my_list)} bytes ")
print("my_tuple's type:", type(my_tuple))
print(f"tuple's memory: {sys.getsizeof(my_tuple)} bytes ")


friends = {"小明","小红","小刚","小黑","小明"}
print("friends:", friends)
print("friends' type:", type(friends))


visitor_ips = ["192.168.1.1", "192.168.1.2", "192.168.1.1", "192.168.1.3"]
unique_ips = set(visitor_ips)
print("type of unique_ips:", type(unique_ips))
print("unique visitor IPs:", unique_ips)


set_a = {1,2,3,4,5,6,7,8,9}
set_b = {4,5,6,7,8,9,10,11,12}


set_c = set_a | set_b
print("set_c:", set_c)


set_d = set_a & set_b
print("set_d:", set_d)

set_e = set_a - set_b
print("set_e:", set_e)

set_f = set_a ^ set_b
print("set_f:", set_f)


my_list = [1,2,3,4,5]
print("list",my_list[1:4])

my_dict = {"a":1, "b":2, "c":3}
my_tuple = (2,3,4,1,2,3)
my_set = {1,2,3,4,5,6}

print("type of my_dict:", type(my_dict))
print("type of my_tuple:", type(my_tuple))
print("type of my_set:", type(my_set))