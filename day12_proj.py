def data_cleaning_tool():
    """
    使用列表推导式和循环进行数据清洗
    """
    print("=== 数据清洗工具 ===")

    raw_data = [" apple "," BANANA","OrANge","123",""," ","grape","PEAR","melon"]

    print("原始数据:",raw_data)

    #1.去除前后空格
    trimmed_data = [item.strip() for item in raw_data]
    print("\n1.去除前后空格:",trimmed_data)

    #2.转换为小写
    lower_data = [item.lower() for item in trimmed_data]
    print("\n2.转换为小写:",lower_data)

    #3.过滤空字符串
    non_empty_data = [item for item in lower_data if item]
    print("\n3.过滤空字符串:",non_empty_data)

    alpha_only_data = [item for item in non_empty_data if item.isalpha()]
    print("\n4.只保留字母:",alpha_only_data)

    # 5. 统计每个水果的出现次数
    fruits_count = {}
    for fruit in alpha_only_data:
        fruits_count[fruit] = fruits_count.get(fruit,0) + 1

    print("\n5.统计水果数量:",fruits_count)


    # 6. 使用嵌套循环创建水果矩阵
    uniques_fruits = list(fruits_count.keys())
    print(f"\n6.水果矩阵({len(uniques_fruits)}x{len(uniques_fruits)})")

    for i in range(len(uniques_fruits)):
        for j in range(len(uniques_fruits)):
            if i == j:
                print(" - ",end = "")
            else:
                pair = f"{uniques_fruits[i]} +{uniques_fruits[j]}"
                print(f"{pair:>10}",end = "")
        print()
    print("\n")
    for i in range(len(uniques_fruits)):
        for j in range(len(uniques_fruits)):
            if i == j:
                print("  -  ", end="")  # 对角线
            else:
                pair = f"{uniques_fruits[i]}+{uniques_fruits[j]}"
                print(f"{pair:>10}", end="")
        print()

data_cleaning_tool()