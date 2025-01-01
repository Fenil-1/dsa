num = int(input())
fin=0
for i in range(num):
    string = input()
    l1=string.split()
    count=0
    for j in range(len(l1)):
        if l1[j]=="1":
            count+=1
    
    if count>=2:
        fin+=1

print(fin)
