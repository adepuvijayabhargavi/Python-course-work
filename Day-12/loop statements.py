#str list tuple set dict range()
'''
for var in seq:
    print(var)
    
s='python programming'
for ch in s:
     print(ch)
     
l=['sugar','salt','jam','eggs']
for item in l:
    print(item)
    
s={'laptop','charger','remote','phone'}
for i in s:
    print(i)
    
t=('1.intro','2.Tokens','3.Data types')
for i in t:
    print(i)
    
d={'name':'bhargavi','batch':55,'course':'PFS','skills':['python','mysql','java']}
for i in d:
    print(i,d[i])


#range(start,stop+1,step) => (0,n,1)

for i in range (1,11):
    print(i)
    
for i in range(2,51,2):
    print(i)
   
for i in range (5,101,5):
    print(i)

for i in range (20,0,-1):
    print(i)
    
for i in range(6):
    print(i)
    
for i in range(30,101,30):
    print(i)
    
for i in range(1,50,2):
    print(i)


s='looping statements'

for i in range(len(s)):
    print(i,s[i])
   
l=[7,2,3,4,5,6,9]
for i in range (len(l)):
    print(i,l[i])
     
l=(5,6,9,2,8)
for i in range(len(l)):
    print(i,l[i])
    


s='looping'

for i in enumerate(s):
    print(i[0],i[l])

l=[3,35,6,8,9,1,]
for i in enumerate(1):
    print(i[0],i[1])
    
t=(2,3,4,6,8,9)
for i in enumerate(t):
    print(i[0],i[1])
    
t=(2,3,4,5,6,7)
for i in enumerate(t):
    print(i[0],i[1])
    

for i in range(10):
    pass
    
for i in range(10):
    if i==5:
        break
    print(i)
    
s='looping statements'
for i in s:
    if i in 'aeiouAEIOU':
        print(i)
        
l=[56,76,32,3,34,67,78,4,9,85,32,11]
for i in l:
    if i%2==0:
        print(i)
        
l=[12,34,56,78,98,11,22]
for i in l:
    if i%6==0:
        print(i)
       
d={'laptop':0,'chargers':2,'keyboard':10,'phone':15,'tab':0,'mouse':5}
for i in d:
    if d[i]:
        print(i)
        
t=(9,2,13,45,66,7)
for i in range(len(t)):
    print(i*t[i])
     '''
names={'soumika','rimsha','bhargavi','komali','ashrutha','pranathi'}
for i in names:
    print(i.upper())

    
