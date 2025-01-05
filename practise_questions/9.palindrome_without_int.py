x=int(input("Enter a number : "))
y=x
revnum=0
while x>0:
    rem=x%10  
    revnum=revnum*10+rem 
    x=x//10 
print(type(revnum))

if revnum==y:
    print("Yes it's a palindrome")
else:
    print("No it's not a palindrome")