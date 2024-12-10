num=input()
l1=num.split()
string=input()
l2=string.split()
index=int(l1[-1])
chintu=int(l2[index-1])
count=0
if chintu==0:
    chintu=1
for i in range(len(l2)):
    if int(l2[i])>=chintu:
        count+=1

print(count)