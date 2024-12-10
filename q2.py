num = int(input())

for z in range(num):
    
    tp=int(input())
    elements=input()
    f=elements.split()

    maxi=0
    i=0
    while(i<len(f)):
        if maxi>int(f[i]):
            maxi=maxi
        else:
            maxi=int(f[i])
        i+=1
    
    j=0
    mini=maxi  
    while(j<len(f)):
        if int(f[j])>mini:
            mini=mini
        else:
            mini=int(f[j])
        j+=1

    print(maxi - mini)
    