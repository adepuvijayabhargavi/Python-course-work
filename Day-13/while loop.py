'''
i=1
while i<=10:
    print(i)
    i=i+1
    
i=10
while i>=1:
    print(i)
    i=i-1
    
i=2
while i<=20:
    print(i)
    i=i+2
    
i=1
while i<=20:
    print(i)
    i=i+2
    
i=1
total=0
while i<=10:
    total=total+i
    i=i+1
print(total)

i=1
while i <= 5:
    print("5 x",i,"=",5*i)
i=i+1

num=int(input("Enter a number:"))
count=0
while num>0:
    count=count+1
    num=num//10
print("digits:",count)

'''
num=int(input())
rev=0
while num>0:
    digit=num%10
    rev=rev*10+digit
    num=num//10
print("Reverse:",rev)
