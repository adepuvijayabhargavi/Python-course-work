#list comprehension 
'''
l = [val for var in seq]
l = [val for var in seq if condition]
l = [val if condition else val for var in seq]

res1 = []
for i in range(1,11):
    res1.append(i)

res2 = [i for i in range(1,11)]

print(res1)
print(res2)

res3 = []
for i in range(3,31,3):
    res3.append(i)

res4 = [i for i in range (3,31,3)]

print(res3)
print(res4)

res5 = []
for i in range(2,52,2):
    res5.append(i)

res6 = [ i for i in range (2,52,2)]

print(res5)
print(res6)

a = 'python programming'
l=[]
for i in a:
    if i in 'aeiouAEIOU':
        l.append(i)
print(l)

l1 = [i for i in a if i in 'aeiouAEIOU']
print(l1)

a = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
l = []
for i in a:
    if i%2==0:
        l.append(i)
    else:
        l.append(0)
print(l)

l1 = [ i if i%2==0 else 0 for i in a]
print(l1)


l = [int(input(f"Enter the number - {i+1}: ")) for i in range(10)]
print(l)

l = []
for i in range(3):
    for j in range (1,4):
        l.append(j)
print(l)

l1 = [j for i in range(3) for j in range(1,4)]
print(l1)


l = [[j for j in range(1,4)] for i in range(3)]
print(l)


s = set()
for i in range(1,11):
    s.add(i)

s1 = {i for i in range(1,11)}

print(s,s1)

d = {}
for i in range(1,11):
    d[i]=i*i

print(d)

res = {i:i*i for i in range (1,11)}
print(res)

res = {input("Enter the name: "):int(input("enter the marks: "))for i in range(5)}
print(res)
'''
s
    
