

file1=open("/home/fenil/Desktop/exam_contest/exam_prep/lol.txt","w")
text=input("Enter some text to add in your text file > ")
data=file1.write(text)
file1.close()


file1=open("/home/fenil/Desktop/exam_contest/exam_prep/lol.txt","r")
text=file1.read()
l1=text.split()
s1=set(l1)
l2=list(s1)

def countunique():
    print(f"Total unique words : {len(s1)}")

def frequency():
    for i in range(len(l2)):
        count=0
        store=l2[i]
        for j in l1:
            if store==j:
                count+=1
        print(f"{store} : {count}")
def countVowels():
    count=0
    vow="aeiouAEIOU"
    for word in l1:
        for char in word:
            if char in vow:
                count+=1
    return count

def kundli():
    total=0
    for word in l1:
        total+=len(word)


    up=0
    for word in l1:
        for char in word:
            if char.isupper():
                up+=1
    low=0
    for word in l1:
        for char in word:
            if char.islower():
                low+=1

    print(f"TOTAL LOWER case {low}")
    print(f"TOTAL upper case {up}")
    print(f"TOTAL ALPHABETS {total}")
        
kundli()
# frequency()
# countunique()
# print(f"Total vowels are {countVowels()}")
file1.close()
