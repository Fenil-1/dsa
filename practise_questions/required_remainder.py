num = int(input())

for j in range(num):
    string = input()
    l1 = string.split()
    x = int(l1[0])
    y = int(l1[1])
    n = int(l1[2])
    
    if y > n: 
        print(0)
    else:
        k = n-(n%x) + y
        if k > n:
            k-=x 
        print(k)
