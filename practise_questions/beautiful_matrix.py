
for i in range(5):
    num = input()
    l1= num.split()
    # print(l1)
    for j in range(5):
        if l1[j] == "1":
            final = abs(2-i) + abs(2-j)
            
print(final)