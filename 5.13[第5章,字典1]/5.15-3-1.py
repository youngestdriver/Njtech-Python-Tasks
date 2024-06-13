'''
假设字典dic_city中存放了每个人旅游过的城市，内容为
{"张三疯":["北京","成都"],"李沫绸":["上海","广州","兰州"],"慕容福":["太原","西安","济南","上海"]}。
试编写程序，根据用户输入的姓名，输出去过的城市。
样例1：
输入：
张三疯
输出：
张三疯去过2个城市，分别是北京、成都。
样例2：
输入：
张三丰
输出：
未查询到该姓名
'''
# 定义字典
dic_city = {
    "张三疯": ["北京", "成都"],
    "李沫绸": ["上海", "广州", "兰州"],
    "慕容福": ["太原", "西安", "济南", "上海"]
}

# 用户输入姓名
name = input()

# 检查姓名是否在字典中
if name in dic_city:
    # 获取去过的城市列表
    cities = dic_city[name]
    # 输出去过的城市数量和城市名称，使用.join()方法将城市列表转换为字符串
    print("{}去过{}个城市，分别是{}。".format(name, len(cities), "、".join(cities)))
else:
    # 若姓名不在字典中，则输出未查询到该姓名
    print("未查询到该姓名")
