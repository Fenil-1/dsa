num = input()

l1=list(num)
s1 = set(l1)

for i in range(len(num),0,-1):
    copy = num[:i]
    rev = copy[::-1]
    if len(s1)== 1:
        print(0)
        break
    if rev != num :
        print(len(rev))
        break

