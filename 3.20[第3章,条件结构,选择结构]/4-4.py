km=float(input())
if km<=0:
    print("千米数输入错误，请重新输入：")
elif km<=3:
    print("您需要支付10元车费！")
elif km<=10:
    cost=10+(km-3)*1.2
    print("您需要支付{:.1f}元车费".format(cost))
else:
    cost=18.4+(km-10)*1.5
    print("您需要支付{:.1f}元车费".format(cost))