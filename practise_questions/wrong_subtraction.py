s = input()
l1 = s.split()
num = int(l1[0])
for i in range(int(l1[1])):
    if num%10 == 0 :
        num = num // 10
    else:
        num-=1
print(num)
