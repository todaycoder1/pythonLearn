def user_login_system():
    """
    使用while循环实现用户登录系统
    """

    print("欢迎来到用户登录系统")

    users = {
        "admin":{"password":"123456","role":"管理员"},
        "user1":{"password":"password","role":"普通用户"},
        "test":{"password":"test123","role":"测试用户"}
    }


    logged_in_user = None
    login_attempts = 0
    max_attempts = 3

    while logged_in_user is None and login_attempts < max_attempts:
        username = input("请输入用户名:")
        password = input("请输入密码:")

        if username in users and users[username]['password'] == password:
            logged_in_user = username
            print(f"用户{username}登录成功")
        else:
            login_attempts += 1
            remaining_attempts = max_attempts - login_attempts

            if remaining_attempts > 0:
                print(f"❌ 登录失败! 还有{remaining_attempts}次机会")
            else:
                print("❌ 登录失败次数过多，系统锁定!")
                return
        
    # 登录成功后的菜单系统
    while logged_in_user:
        print(f"\n=== 欢迎用户{logged_in_user} ===")
        print("1. 查看个人信息")
        print("2. 修改密码")
        print("3. 查看所有用户")
        print("4. 退出登录")
        print("5. 退出系统")

        choice = input("请选择操作:")


        if choice == "1":
            user_info = users[logged_in_user]
            print(f"用户名:{logged_in_user}")
            print(f"角色：{user_info['role']}")

        elif choice == "2":
            old_password = input("请输入旧密码:")
            if old_password == users[logged_in_user]['password']:
                new_password = input("请输入新密码:")
                confirm_password = input("请确认新密码:")

                if new_password == confirm_password:
                    users[logged_in_user]['password'] = new_password
                    print("✅ 密码修改成功")
                else:
                    print("❌ 新密码与确认密码不一致")
            else:
                print("❌ 旧密码错误")

        elif choice == "3":
            if users[logged_in_user]['role'] == "管理员":
                print("\n=== 所有用户 ===")
                for username,user_info in users.items():
                    print(f"用户名:{username},角色:{user_info['role']}")
            else:
                print("❌ 权限不足! 只有管理员可以查看所有用户")

        elif choice == "4":
            logged_in_user = None
            print("✅ 退出登录成功")

        elif choice == "5":
            print("感谢使用，再见!")
            break

        else:
            print("❌ 无效选择!")



user_login_system()

