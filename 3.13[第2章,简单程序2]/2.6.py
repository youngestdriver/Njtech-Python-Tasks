num=int(input("请输入三位整数"))
bai=num//100
shi=(num%100)//10
ge=(num%10)//1
num_re=ge*100+shi*10+bai
print("这个三位数的反序数为:{}".format(num_re))

#print(bai) 百位
#print(shi) 十位
#print(ge)  个位