def student_info_system():
    students = {} #创建一个空字典

    while True:
        print("\n===学生信息管理系统===")
        print("1. 添加学生信息")
        print("2.查看所有学生")
        print("3.查找学生信息")
        print("4.更新学习信息")
        print("5.删除学生信息")
        print("6.统计信息")
        print("7.退出系统")


        choice = input("请选择操作(1-7)：")

        if choice == "1":
            student_id = input("请输入学生学号：")
            if student_id in students:
                print("该学号已存在")
                continue

            name = input("请输入学生姓名：")
            age = input("请输入学生年龄：")
            major = input("请输入学生专业：")

            students[student_id] = {"name":name,"age":age,"major":major}
            print(f"添加学生信息成功：{students[student_id]}")

        elif choice == "2":
           print("所有学生信息：")
           for student_id in students:
               print(f"学号：{student_id}，信息：{students[student_id]}")

        elif choice == "3":
            student_id = input("请输入学生学号：")
            if student_id in students:
                print(f"学号：{student_id}，信息：{students[student_id]}")
            else:
                print("没有找到该学生，查无此人")

        elif choice == "4":
            student_id = input("请输入要更新的学生学号：")
            if student_id in students:
                name = input("请输入学生姓名：")
                age = input(f"年龄[{students[student_id]['age']}]:")  or students[student_id]["age"]
                major = input(f"专业[{students[student_id]['major']}]:") or students[student_id]["major"]

                students[student_id] = {"name":name,"age":age,"major":major}
            else:
                print("没有找到该学生，查无此人")

        elif choice == "5":
            student_id = input("请输入要删除的学生学号：")
            if student_id in students:
                students.pop(student_id)
                print("删除成功")
            else:
                print("没有找到该学生，查无此人")

        elif choice == "6":
            print(f"学生总数：{len(students)}")

        elif choice == "7":
            print("感谢使用学生信息管理系统")
            break   
        else:
            print("无效的选择，请重新输入")


student_info_system()