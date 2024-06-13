print("老师好，这题我想到了三种算法，但是他们的结果从-2位小数开始不同...不知道哪种更正确，就都码上了（实在没法解释")
#算法1
power_up=power_down=1
power_up=(power_up*(1+0.01))**365
power_down=(power_down*(1-0.01))**365
print("算法1：")
print("天天向上：{}".format(power_up))
print("天天向下：{}".format(power_down))

#算法2
power_up=power_down=1
for i in range(365):
    power_up = power_up*1.01
    power_down = power_down*0.99
print("算法2：")
print("天天向上：{}".format(power_up))
print("天天向下：{}".format(power_down))

#算法3
power_up=power_down=1
for i in range(365):
    power_up += power_up*0.01
    power_down -= power_down*0.01
print("算法3：")
print("天天向上：{}".format(power_up))
print("天天向下：{}".format(power_down))
