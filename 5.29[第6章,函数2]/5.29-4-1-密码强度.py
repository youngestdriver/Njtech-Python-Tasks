'''
定义函数f, 计算密码强度。并输入调用函数表达式进行测试。
密码强度计算规则（满足其中一条，密码强度增加一级）: 
1、有数字
2、有大写字母
3、有小写字母
4、位数不少于8位
样例: 
输入: f("123Abc456")
输出: 密码强度4级
'''
def f(str_mima):
    mima=0

    if any(word.isdigit() for word in str_mima):
        mima+=1
    
    if any(word.isupper() for word in str_mima):
        mima+=1

    if any(word.islower() for word in str_mima):
        mima+=1

    if len(str_mima)>=8:
        mima+=1

    return(mima)

a=eval(input())
print("密码强度{}级".format(a))

    # for i in [1,2,3,4,5,6,7,8,9,0]:
    #     if str(i) in str_mima:
    #         mima+=1
    #         break

    # if (word>="A" and word<="Z" for word in str_mima):
    #     mima+=1

    # if (word>="a" and word<="z" for word in str_mima):
    #     mima+=1
