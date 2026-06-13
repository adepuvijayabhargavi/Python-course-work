'''
for i in range(1,11,1):
    print(i)
   
for i in range(1,21,1):
    if i % 2==0:
        print(i)
        
total=0        
for i in range (1,101,1):
    total=total+i

print(total)

num=int(input())
for i in range(1,11):
    print(num,"X",i,"=",num*i)
    
num=int(input())
fact=1
for i in range(1,num+1):
    fact=fact*i
print(fact)

text=input()
count=0
for ch in text:
    if ch.lower() in "aeiou":
        count=count+1
print("vowels:",count)

for i in range(1,6):
    print(str(i)*i)
    
for i in range (1,101):
    if i%3==0 and i%5==0:
        print(i)
        
total=0
for i in range(1,101):
    total=total+i
print("sum:",total)

for i in range (1,11):
    print(f"5*{i}={5*i}")
    
for i in range(1,11):
    print(i*i)
   
count=0
for i in range(1,51):
    count=count+1
print("count:",count)
 
n=int(input("Enter a number: "))
fact=1
for i in range(1,n+1):
      fact=fact*i
print("Factorial:", fact)

n=int(input("Enter a number: "))
total=0
for i in range(2,n+1,2):
      total=total+i
print("sum:",total)
'''
n=int(input())
for i in range(1,11):
    print(f"{n}X{i}={n*i}")
      
