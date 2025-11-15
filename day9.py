

def check_weather(temperature,is_rainy):
    if temperature > 30:
        if is_rainy:
            return "闷热下雨天，建议室内活动"
        else:
            return "炎热晴天，注意防晒"
    elif temperature > 20:
        if is_rainy:
            return "温暖下雨天，适合散步"
        else:
            return "温暖晴天，适合户外活动"
    elif temperature > 10:
        if is_rainy:
            return "凉爽下雨天，建议带伞"
        else:
            return "凉爽晴天，适合运动"
    else:
        if is_rainy:
            return "寒冷下雨天，注意保暖"
        else:
            return "寒冷晴天，注意防寒"





print(check_weather(20,False))



def process_order(quantity,price,has_discount,is_vip):
    if quantity <= 0:
        return "错误：数量必须大于0"
    
    if price <= 0:
        return "错误：价格必须大于0"
    
    total = quantity * price

    if has_discount and is_vip:
        total *= 0.7
    elif has_discount:
        total *= 0.9
    elif is_vip:
        total *= 0.8
    

    return f"订单总金额: {total:.2f}元"

print(process_order(5,100,True,True))


def get_season(month):
    season_map = {"12":"冬季","1":"冬季","2":"冬季",
                  "3":"春季","4":"春季","5":"春季",
                  "6":"夏季","7":"夏季","8":"夏季",
                  "9":"秋季","10":"秋季","11":"秋季"}
    

    if month in season_map:
        return season_map[month]
    else:
        return "无效的月份输入"
    
print(get_season("4"))