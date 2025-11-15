


students = [{"name":"zhangsan","scores":{"English":20,"Math":150}},{"name":"lisi","scores":{"English":120,"Math":50}}]

print(students[0].items())
print(students[0]["name"])
print(students[0]["scores"]["Math"])
print(students[0]["scores"].keys())
print(students[0].keys())




class_info = {"class_name":"Python 班","students":["zhangsan","lisi"]}

print(class_info["students"])
print(class_info["students"][0])

math_high = [stu for stu in students if stu["scores"]["Math"] >100]
print(math_high)


English_score = sorted(students,key=lambda x:x["scores"]["English"],reverse=True)
print(English_score)