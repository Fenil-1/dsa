
def fibonacci(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        return fibonacci(num - 1) + fibonacci(num - 2)
n=int(input("enter to series till the number you want : "))
for i in range(n):
    print(fibonacci(i))
