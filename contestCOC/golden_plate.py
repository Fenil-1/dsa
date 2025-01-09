num = input()
l1 = num.split()
count=0
row = int(l1[0])
column = int(l1[1]) 
for i in range(int(l1[2])):
    count += (row *2) + (((column)-2)*2)
    row -=4
    column -=4
    
print(count)
