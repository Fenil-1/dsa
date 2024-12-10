num=int(input())

for i in range(num):
    length=int(input())
    string=input()
    l1=list(string)
    for k in range(int(len(string)/2)):
        if l1[0]==l1[-1]:
            print(len(l1))
            break
        else:
            l1=l1[1:-1]
            
    if l1==[]:
        print(0)  
    elif len(l1)==1:
        print(1)


                