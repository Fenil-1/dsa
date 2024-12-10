num = int(input())

for i in range(num):

    a=input()
    l1=a.split()
    first=0
    second=0
    sumit=0
    for j in range(2):
        for k in range(2,4):
            if l1[j]>l1[k]:
                first+=1
            elif l1[j]< l1[k]:
                -=1
        if count>0:
            sumit+=1
    print(sumit)       


    
    # choice=0
    
    # # for j in range(2):
    # if int(l1[0])>int(l1[2]) and int(l1[1])>int(l1[3]):
    #     choice+=2
        
    
    # if int(l1[1])>int(l1[2]) and int(l1[0])>int(l1[3]):
    #     choice+=2   
    
    # print(choice)