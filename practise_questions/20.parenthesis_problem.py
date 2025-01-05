###############CONCEPT###############
# stack=[]

# def display(stack):
#     for i in range(len(stack)-1,-1,-1):
#         print(stack[i])
# while True:
#     print('''***start***   1- append
#                            2- pop ''')
    
#     num=int(input("ENTER 1,2,3,4"))

#     if num==1:
#         inp=input("enter to APpend")
#         stack.append(inp)

#     elif num==2:
#         stack.pop()


#     elif num==3:
#         display(stack)

#     elif num==4:
#         break




s= input("brackets")
st=[]
st.append(s[0])
for i in range(1,len(s)):
    if st and (st[-1]=="(" and s[i]==")" or st[-1]=="[" and s[i]=="]" or st[-1]=="{" and s[i]=="}"):
        st.pop()     
    else:   
        st.append(s[i])   
if st==[]:
    print("pass")
else:
    print("fail")





