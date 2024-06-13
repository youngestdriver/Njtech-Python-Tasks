x=eval(input())
if x<0:
    y=0
elif x<5:
    y=x
elif x<10:
    y=3*x-5
elif x<20:
    y=0.5*x-2
else:
    y=0
print(y)