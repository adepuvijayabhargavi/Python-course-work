'''
#pattern of A
n=int(input("Enter the size: "))
m=n//2
for i in range(n):
      for j in range(n):
          if i==0 or j==0 or i ==m  or j == n-1:
               print('*',end=' ')
          else:
              print(' ',end=' ')
      print()
      
#pattern of B
n=int(input("Enter the size: "))
m=n//2
for i in range(n):
      for j in range(n):
          if i==0 or j==0 or i ==m  or j == n-1 or  i==n-1:
               print('*',end=' ')
          else:
              print(' ',end=' ')
      print()
      
#pattern of C
n=int(input("Enter the size: "))
m=n//2
for i in range(n):
      for j in range(n):
          if i==0 or j==0 or  i==n-1:
               print('*',end=' ')
          else:
              print(' ',end=' ')
      print()
      
#pattern of D  
n=int(input("Enter the size: "))
m=n//2
for i in range(n):
      for j in range(n):
          if i==0 or j==0 or  i==n-1 or j==n-1:
               print('*',end=' ')
          else:
              print(' ',end=' ')
      print()
      
#pattern of E    
n=int(input("Enter the size: "))
m=n//2
for i in range(n):
      for j in range(n):
          if i==0 or j==0 or  i==n-1 or i==m:
               print('*',end=' ')
          else:
              print(' ',end=' ')
      print()

#pattern of F
n=int(input("Enter the size: "))
m=n//2
for i in range(n):
      for j in range(n):
          if i==0 or j==0 or i==m:
               print('*',end=' ')
          else:
              print(' ',end=' ')
      print()
      

#pattern of G
n=int(input("Enter the size: "))
m=n//2
for i in range(n):
      for j in range(n):
          if i==0 or j==0 or (i==m and j>=m) or (j==n-1 and i>=m) or (i==n-1 and j<n-1) :
               print('*',end=' ')
          else:
              print(' ',end=' ')
      print()
      
#pattern of H
n=int(input("Enter the size: "))
m=n//2
for i in range(n):
      for j in range(n):
            if j==0 or j==n-1 or i==m:
                  print('*',end=' ')
            else:
                  print(' ',end=' ')
      print()

#pattern of I    
n=int(input("Enter the size: "))
m=n//2
for i in range(n):
      for j in range(n):
          if i==0 or j==m or i==n-1:
                print('*',end=' ')
          else:
                print(' ',end=' ')
      print()

#pattern of J       
n=int(input("Enter the size: "))
m=n//2
for i in range(n):
      for j in range(n):
            if i==0 or j==m or (i==n-1 and j<=m) or (j==0 and i>=m):
                  print('*',end=' ')
            else:
                  print(' ',end=' ')
      print()
      
      
#pattern of K
n=int(input("Enter the size: "))
m=n//2
for i in range(n):
      for j in range(n):
            if j==0 or i+j==m or i-j==m:
                  print('*',end=' ')
            else:
                  print(' ',end=' ')
      print()
      
#pattern of L
n=int(input("Enter the size: "))
for i in range(n):
      for j in range(n):
            if j==0 or i==n-1:
                  print('*',end=' ')
            else:
                  print(' ',end=' ')
      print()
      
#pattern of M
n=int(input("Enter the size: "))
m=n//2
for i in range(n):
      for j in range(n):
            if j==0 or j==n-1 or (i==j and i <=m) or (i+j==n-1 and i<=m):
                  print('*',end=' ')
            else:
                  print(' ',end=' ')
      print()
      
#pattern of N
n=int(input("Enter the size: "))
m=n//2
for i in range(n):
      for j in range(n):
            if j==0 or j==n-1 or i==j:
                  print('*',end=' ')
            else:
                  print(' ',end=' ')
      print()
      
#pattern of O
n=int(input("Enter the size: "))
m=n//2
for i in range(n):
      for j in range(n):
            if j==0 or j==n-1 or i==0 or i==n-1:
                  print('*',end=' ')
            else:
                  print(' ',end=' ')
      print()
      

#pattern of P
n=int(input("Enter the size: "))
m=n//2
for i in range(n):
      for j in range(n):
            if j==0 or i==m or i==0 or (j==n-1 and i<m):
                  print('*',end=' ')
            else:
                  print(' ',end=' ')
      print()
      
#pattern of Q
n=int(input("Enter the size: "))
m=n//2
for i in range(n):
      for j in range(n):
            if j==0 or i==0 or i==n-1 or j==n-1:
                  print('*',end=' ')

            elif i==0 and i>n//2:
                  print('*',end=' ')
            else:
                  print(' ',end=' ')
      print()
      
#pattern of S
n=int(input("Enter the size: "))
m=n//2
for i in range(n):
      for j in range(n):
            if i==0 or j==0 or i==m or (j==n-1 and i<m) or (i-j==m) :
                  print('*',end=' ')
            elif i==0 and i>n//2:
                  print('*',end=' ')
            else:
                  print(' ',end=' ')
      print()
      
#pattern of T
n=int(input("Enter the size: "))
m=n//2
for i in range(n):
      for j in range(n):
            if i==0 or j==m :
                  print('*',end=' ')
            else:
                  print(' ',end=' ')
      print()
      
#pattern of U
n=int(input("Enter the size: "))
m=n//2
for i in range(n):
      for j in range(n):
            if j==0 or j==n-1 or i==n-1:
                  print('*',end=' ')
            else:
                  print(' ',end=' ')
      print()
      '''
#pattern of V
n=int(input("Enter the size: "))
for i in range(n):
      for j in range(2*n-1):
            if j==i or j==(2*n-2-i):
                  print('*',end=' ')
            else:
                  print(' ',end=' ')
      print()
