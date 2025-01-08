noi = int(input())
for i in range(noi):
    store = []
    num = input()
    l1 = num.split()
    ans1 = abs(int(l1[2])-1) + abs(int(l1[3])-1)
    ans2 = abs(int(l1[2])-int(l1[0])) + abs(int(l1[3])-int(l1[1]))
    ans3 = abs(int(l1[2])-1) + abs(int(l1[3])-int(l1[1]))
    ans4 = abs(int(l1[2])-int(l1[0])) + abs(int(l1[3])-1)
    store.append(ans1)
    store.append(ans2)
    store.append(ans3)
    store.append(ans4)
    print(max(store))
