x=int(input("Enter a number : "))
y=x
revnum=0
while x>0:
    rem=x%10  #extracts last digit
    revnum=revnum*10+rem #reversed number print
    x=x//10 #removes the last digit
print(type(revnum))

if revnum==y:
    print("Yes it's a palindrome")
else:
    print("No it's not a palindrome")