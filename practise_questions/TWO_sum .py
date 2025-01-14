l1 = list(input())
target = int(input())
st=[]
for i in range(len(l1)):
    for j in range(i+1,len(l1)):
        if int(l1[i])+ int(l1[j]) == target:
            st.append(i)
            st.append(j)
            break
print(st)