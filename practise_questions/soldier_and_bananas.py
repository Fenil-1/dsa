num = input()
l1 = num.split()
sum = 0
for i in range(1,1+int(l1[2])):
    sum += int(l1[0])*i

borrow = sum - int(l1[1])
if borrow < 0:
    borrow = 0
print(borrow)