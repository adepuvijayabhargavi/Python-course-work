Python 3.13.5 (tags/v3.13.5:6cb20a2, Jun 11 2025, 16:15:46) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
t = (1,2,3,4,5)
t
(1, 2, 3, 4, 5)
t=()
t=(1,2,1,1,1,)
t
(1, 2, 1, 1, 1)
t=(1,1.14,'jshj',[])
t
(1, 1.14, 'jshj', [])
t=(10,20,30,40)
h=(100,200,300)
t+h
(10, 20, 30, 40, 100, 200, 300)
t*9
(10, 20, 30, 40, 10, 20, 30, 40, 10, 20, 30, 40, 10, 20, 30, 40, 10, 20, 30, 40, 10, 20, 30, 40, 10, 20, 30, 40, 10, 20, 30, 40, 10, 20, 30, 40)
h*2
(100, 200, 300, 100, 200, 300)
(t+h)*8
(10, 20, 30, 40, 100, 200, 300, 10, 20, 30, 40, 100, 200, 300, 10, 20, 30, 40, 100, 200, 300, 10, 20, 30, 40, 100, 200, 300, 10, 20, 30, 40, 100, 200, 300, 10, 20, 30, 40, 100, 200, 300, 10, 20, 30, 40, 100, 200, 300, 10, 20, 30, 40, 100, 200, 300)
t(0)
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    t(0)
TypeError: 'tuple' object is not callable
t[0]
10
t[4]
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    t[4]
IndexError: tuple index out of range
t[3]
40
h[1]
200
h[-1]
300
t[-2]
30
t[-3]
20
h[-1]
300
t9(:2)
SyntaxError: invalid syntax
t(:2)
SyntaxError: invalid syntax
t[:2]
(10, 20)
t[3:]
(40,)
t[-1:2]
()
t[1:1:1]
()
h[::-1]
(300, 200, 100)
h[1:2]
(200,)
t[:4:2]
(10, 30)
10 in t
True
30 not in h
True
30 in t
True
60 in t
False
30,50 not t,h
SyntaxError: invalid syntax
50 not in h
True
t[::-3]
(40, 10)
len(t)
4
sorted(t)
[10, 20, 30, 40]
min(t)
10
max(t)
40
sum(t)
100
t.count(20)
1
t.index(30)
2
t.index(10)
0
a = (1,2,4)
a
(1, 2, 4)
x,y,z=a
x
1
y
2
z
4
t = (1,2,3,[4,5,6],7,8)
t
(1, 2, 3, [4, 5, 6], 7, 8)
t[0]
1
t3]
SyntaxError: unmatched ']'
t[3]
[4, 5, 6]
t(3).append(60)
Traceback (most recent call last):
  File "<pyshell#58>", line 1, in <module>
    t(3).append(60)
TypeError: 'tuple' object is not callable
t
(1, 2, 3, [4, 5, 6], 7, 8)
t[4]
7
t[2]
3
t[3].append(10)
t
(1, 2, 3, [4, 5, 6, 10], 7, 8)
t[5].append(55)
Traceback (most recent call last):
  File "<pyshell#64>", line 1, in <module>
    t[5].append(55)
AttributeError: 'int' object has no attribute 'append'
t[5].extend(99)
Traceback (most recent call last):
  File "<pyshell#65>", line 1, in <module>
    t[5].extend(99)
AttributeError: 'int' object has no attribute 'extend'
s = {1,2,3,4]
SyntaxError: closing parenthesis ']' does not match opening parenthesis '{'
s =
SyntaxError: invalid syntax
s = {1,2,3,4}
s=set()
s=[1,1,1,1,}
SyntaxError: closing parenthesis '}' does not match opening parenthesis '['
s = {1,1,1,1,1}
s
{1}
s = {566,657,899,323,099,}
SyntaxError: leading zeros in decimal integer literals are not permitted; use an 0o prefix for octal integers
s = {656,89,2334,21,78,99}
s
{656, 99, 21, 89, 78, 2334}
s=set()
s
set()
s.add()
Traceback (most recent call last):
  File "<pyshell#78>", line 1, in <module>
    s.add()
TypeError: set.add() takes exactly one argument (0 given)
s.add(1)
s
{1}
s.add(467.576)
s
{1, 467.576}
s.add("gjhh")
s
{'gjhh', 1, 467.576}
s.add([1,2,3,4,5])
Traceback (most recent call last):
  File "<pyshell#85>", line 1, in <module>
    s.add([1,2,3,4,5])
TypeError: unhashable type: 'list'
s.add({1,2,3,4})
Traceback (most recent call last):
  File "<pyshell#86>", line 1, in <module>
    s.add({1,2,3,4})
TypeError: unhashable type: 'set'
s.add({1:1,2:2})
Traceback (most recent call last):
  File "<pyshell#87>", line 1, in <module>
    s.add({1:1,2:2})
TypeError: unhashable type: 'dict'
s
{'gjhh', 1, 467.576}
1 in s
True
2 in s
False
false not in s
Traceback (most recent call last):
  File "<pyshell#91>", line 1, in <module>
    false not in s
NameError: name 'false' is not defined. Did you mean: 'False'?
False not in s
True
True not in s
False
ghjss in s
Traceback (most recent call last):
  File "<pyshell#94>", line 1, in <module>
    ghjss in s
NameError: name 'ghjss' is not defined
'hj' in s
False
'tfhghjj' in s
False
'jhjgyggj' not in s
True
a = {1,2,3,4,5}
b = {6,7,8,9}
a
{1, 2, 3, 4, 5}
a|b
{1, 2, 3, 4, 5, 6, 7, 8, 9}
a.union(b)
{1, 2, 3, 4, 5, 6, 7, 8, 9}
a.intersection(b)
set()
a & b
set()
a-b
{1, 2, 3, 4, 5}
b-a
{8, 9, 6, 7}
a ^ b
{1, 2, 3, 4, 5, 6, 7, 8, 9}
a
{1, 2, 3, 4, 5}
a<={1}
False
a>={1}
True
a>={3}
True
a>={5}
True
a>={9}
False
b>={2}
False
b>={5}
False
a<={9}
False
a
{1, 2, 3, 4, 5}
b
{8, 9, 6, 7}
a.isdisjoint(b)
True
a.isdisjoint({90,80})
True
a
{1, 2, 3, 4, 5}
a.add(17)
a
{1, 2, 3, 4, 5, 17}
a.add(14)
a
{1, 2, 3, 4, 5, 17, 14}
a.update({11,12,13})
a
{1, 2, 3, 4, 5, 11, 12, 13, 14, 17}
a.discard(14)
a
{1, 2, 3, 4, 5, 11, 12, 13, 17}
a.pop()
1
a.pop(5)
Traceback (most recent call last):
  File "<pyshell#131>", line 1, in <module>
    a.pop(5)
TypeError: set.pop() takes no arguments (1 given)
a.pop()
2
a.remove(4)
a
{3, 5, 11, 12, 13, 17}
a.remove(13)

a.discard(51)
a
{3, 5, 11, 12, 17}
a.discard(23)
a
{3, 5, 11, 12, 17}
a.discard(11,12)
Traceback (most recent call last):
  File "<pyshell#141>", line 1, in <module>
    a.discard(11,12)
TypeError: set.discard() takes exactly one argument (2 given)
>>> a.discard(12)
>>> a
{3, 5, 11, 17}
>>> a.discard(3)
>>> a.clear()
>>> a
set()
>>> a
set()
>>> a.intersection_update(b)
>>> a
set()
>>> a={2,56,8,9}
>>> b={3,56,9,99}
>>> a.intersection_update(b)
>>> a
{56, 9}
>>> b
{56, 9, 3, 99}
>>> c=b

>>> c.add(12)
>>> c
{3, 99, 9, 12, 56}
>>> min(c)
3
>>> max(c)
99
>>> sorted(c)
[3, 9, 12, 56, 99]
>>> d = c.copy()
>>> d.add(10)
>>> d
{3, 99, 56, 9, 10, 12}
>>> c
{3, 99, 9, 12, 56}
>>> len(c)
5
>>> min(c)
3
>>> max(c)
99
>>> sorted(c)
[3, 9, 12, 56, 99]
>>> sum(c)
179
