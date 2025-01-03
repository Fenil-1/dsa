num = input()
l1= num.split()
x=1
count=1
limakweight = int(l1[0])
bobweight = int(l1[1])
while(x<=(2*bobweight)/(3*limakweight)):
    limakweight*=3
    bobweight*=2
    count+=1

print(count)
