def rax(num,d,i):
    if i == 0:
        print(d)
    else:
        d+=num[i-1]
        i-=1
        rax(num,d,i)
num=[1,2,3,4,5,6,3]
d=0
i=len(num)
rax(num,d,i)
