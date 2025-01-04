num = int(input())
str= input()
l1 = list(str)
st = []
count=0

for i in range(num):
    if i==0:
        st.append(l1[i])
    else:
        if l1[i] == l1[i-1]:
            count+=1
        else:
            st.append(l1[i])
print(count)
    