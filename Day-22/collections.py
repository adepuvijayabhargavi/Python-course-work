'''
import collections

s='python programming language'
print(collections.Counter(s))

d = {}
for i in s:
    if i in d:
        d[i]+=1
    else:
        d[i]=1

print(d)



import collections
s='python programming language'

d = collections.defaultdict(int)

for i in s:
    d[i]+=1

print(d)




import collections

l=collections.deque([])

l.appendleft(10)
l.appendleft(20)
l.appendleft(30)
l.appendleft(40)
l.pop()
l.pop()
l.pop()
l.appendleft(50)
l.appendleft(60)
l.pop()

print(l)



import collections

l=collections.deque([])

l.append(10)
l.append(20)
l.append(30)
l.append(40)
l.pop()
l.pop()
l.pop()
l.append(50)
l.append(60)
l.pop()

print(l)




import itertools

print(list(itertools.combinations('abcd',2)))
print(list(itertools.permutations('abcd',2)))
'''



from itertools import combinations,permutations

com = combinations('abcd', 2)
print([''.join(i) for i in com])

per = permutations('abcd', 2)
print([''.join(i) for i in per])






