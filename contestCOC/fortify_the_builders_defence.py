num = int(input())

for z in range(num) :   
    matrix = []
    s=int(input())    
    for row in range(s):
        a = []
        # A for loop for column entries
        for column in range(s):   
            a.append((input()))
        matrix.append(a)

    for row in range(s):
        for column in range(s):
            print(matrix[row][column], end=" ")
        print()
  
print(matrix)