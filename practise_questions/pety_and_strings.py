str1=input().lower()
str2=input().lower()
count=0

abcd = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
if str1==str2:
    print(0)
    
for i in range(len(str1)):
    if str1[i]!=str2[i]:
        for j in abcd:
            if str1[i]==j:
                print(-1)
                break
            if str2[i]==j:
                print(1)
                break
        break
              
         
    
    
    