num = int(input())

for i in range(num):
    string=input()
    if len(string)<=10:
        print(string)
    else:
        f=string[0]
        val=str(len(string)-2)
        l=string[-1]
        print(f+val+l)