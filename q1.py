num = int(input())
h=0
m=0
for i in range(num):
    time = input()
    l1=time.split()
    h=int(l1[0])
    m=int(l1[1])
    rem= 1440 - ((h*60)+m)
    print(rem)