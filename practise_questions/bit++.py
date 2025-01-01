num = int(input())
x=0

for i in range(num):
    string = input()
    l1=list(string)
    if l1[1]=="+":
        x+=1
    elif l1[1]=="-":
        x-=1
print(x)

    
   


