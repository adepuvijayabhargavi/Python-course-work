'''
s='python'
 
for i in range(len(s)):
    for j in range (i+1,len(s)):
        print(s[i],s[j],sep='',end=' ')
       
l=[[1,2,3],[4,5,6],[7,8,9]]

sum=0
for i in l:
    for j in i:
        sum=sum+j
print(f'sum = {sum}')
 

d={
    '1234':{'pin':'4567','balance':2300},
    '2345':{'pin':'9876','balance':5300},
    '3456':{'pin':'5678','balance':6300},
    '4567':{'pin':'9876','balance':7300}
    
    }
for i in d:
    print("Account number:",i)
    print("pin:",d[i]['pin'])
    
for row in range (5):
    for col in range(5):
        print(col,end='')
    print()
    
n=int(input("Enter the size: "))
for row in range (n):
    for col in range(n):
        print('*',end=' ')
    print()
   
n=int(input("Enter the size: "))
for row in range (n):
    for col in range(n):
        print('#',end=' ')
    print()
   

n=int(input("Enter the size :"))
for row in range(n):
      for col in range (row+1):
          print('*',end=' ')
      print()

n=int(input("Enter the size :"))
for row in range(n):
      for j in range (n-row):
          print('*',end=' ')
      print()

n=int(input("Enter the size: "))
for row in range(n):
      for sp in range (n-row-1):
         print(' ',end=' ')
      for col in range(row+1):
         print('*',end=' ')
      print()
    
      

n=int(input("Enter the size: "))
for row in range(n):
      for sp in range(row):
          print(' ',end=' ')
      for col in range(n-row):
          print('*',end=' ')
      print()
      
n=int(input("Enter the size: "))
for row in range(n):
      for col in range(n):
        print((row+col)%2,end=' ')
      print()
      
     
n=int(input("Enter the size: "))
c=1
for row in range (n):
    for col in range(row+1):
        print(str(c).zfill(2),end=' ')
        c=c+1
    print()
   
n=int(input("Enter the size :"))
for row in range(n):
      for col in range (row+1):
          print('*',end=' ')
      print()
       
n=int(input("Enter the size :"))
for row in range(n):
      for col in range (row+1):
          print('*',end=' ')
      print()
      

n=int(input("Enter the size :"))
for row in range(n):
      for j in range (n-row):
          print('*',end=' ')
      print()
      
n=int(input("Enter the size :"))
for row in range(n):
      for j in range (n-row):
          print('*',end=' ')
      print()
      
n=5
for i in range(n):
      for j in range (i+1):
            print('*',end=' ')
      print()
      
n=5
for i in range(n):
      for j in range(i,n):
            print('*',end=' ')
      print()
      
n=5
for i in range (n):
      for j in range (i,n):
            print(' ',end=' ')
      for j in range(i+1):
            print('*',end=' ')
      print()
      
n=5
for i in range(n):
      for j in range(i+1):
            print(' ',end=' ')
      for j in range (i,n):
            print('*',end=' ')
      print()
      
n=5
for i in range(n):
      for j in range(i,n):
            print(' ',end=' ')
      for j in range(i+1):
            print('*',end=' ')
      for j in range(i):
            print('*',end=' ')
      print()
      
n=5
for i in range(n):
      for j in range(i+1):
            print(' ',end=' ')
      for j in range(i,n-1):
            print('*',end=' ')
      for j in range(i,n):
            print('*',end=' ')
      print()
      '''

            


