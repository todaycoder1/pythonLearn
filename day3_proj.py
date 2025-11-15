def grade_management_system():
    students = []
    grades = []

    while True:
        print("\n===学生成绩管理系统===")
        print("1.添加学生成绩")
        print("2.查询所有成绩")
        print("3.查找学生成绩")
        print("4.删除学生成绩")
        print("5.退出系统")


        in_val = input("请选择操作：")

        print("type(in_val):",type(in_val))

        if in_val == "1":
            name = input("请输入学生姓名：")
            grade = input("请输入学生成绩：")
            students.append(name)
            grades.append(float(grade))
            print(f"成功添加{name}的成绩:{grade}")
        elif in_val == "2":
            print(f"所有学生成绩：")
            for i in range(len(students)):
                print(f"{students[i]}的成绩是：{grades[i]}")
            
        elif in_val == "3":
            name = input("请输入学生姓名：")
            if name in students:
                idx = students.index(name)
                print(f"{name}的分数是：{grades[idx]}")
            else:
                print(f"没有找到{name}")

        elif in_val == "4":
            name = input("请输入学生姓名：")
            if name in students:
                idx = students.index(name)
                students.pop(idx)
                grades.pop(idx)
            else:
                print(f"没有找到{name}")

        elif in_val == "5":
            print("感谢使用学生成绩管理系统")
            break   

        else:
            print("无效的操作") 

grade_management_system()

            