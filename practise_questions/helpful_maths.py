num = input()
l1= num.split("+")

one=0
two=0
three=0


l2=[]
for i in l1:
    if i=="1":
        one+=1
    elif i=="2":
        two+=1
    elif i=="3":
        three+=1
for x in range(one):
    l2.append("1")
for y in range(two):
    l2.append("2")
for z in range(three):
    l2.append("3")    

for final in range(len(l2)):
    if final<len(l2)-1:
        print(l2[final],end="+")
    else:
        print(l2[final])
    
    
        

