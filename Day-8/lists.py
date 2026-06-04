Python 3.13.5 (tags/v3.13.5:6cb20a2, Jun 11 2025, 16:15:46) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
s = '         hello         worls      '
s
'         hello         worls      '
s.strip()
'hello         worls'
s.lstrip()
'hello         worls      '
s.rstrip()
'         hello         worls'
s = 'string.py'
s
'string.py'
s.startswith('str')
True
s.startswith('hgh')
False
s.endswith('py')
True
s.endswith('js')
False
'gfhgghj'.isalpha()
True
gHGJHJH.isalpha()
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    gHGJHJH.isalpha()
NameError: name 'gHGJHJH' is not defined
GHJHJ.isalpha()
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    GHJHJ.isalpha()
NameError: name 'GHJHJ' is not defined
ghjh.isalnum()
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    ghjh.isalnum()
NameError: name 'ghjh' is not defined
1324.isalnum()
SyntaxError: invalid syntax
566. isalnum()
SyntaxError: invalid syntax
'37283'.isalnum()
True
hdjdjs767.isalnum()
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    hdjdjs767.isalnum()
NameError: name 'hdjdjs767' is not defined
'shwj782js'.isalnum
<built-in method isalnum of str object at 0x000001C68372F070>
'56676'.isalnum
<built-in method isalnum of str object at 0x000001C6819F1C50>
'hbs'.isaplnum
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    'hbs'.isaplnum
AttributeError: 'str' object has no attribute 'isaplnum'. Did you mean: 'isalnum'?
'shxbjsxn'.isalnum
<built-in method isalnum of str object at 0x000001C68372FAB0>
'hjhjw'.islower()
True
'HGHJJ'isupper()
SyntaxError: invalid syntax
'HGHJB'.isupper()
True
'gfh'.isupper()
False
' '.isspace()
True
'dog               '.isspace()
False
'ghjj'istitle()
SyntaxError: invalid syntax
'Tiger'.istitle()
True
'fhghj'.istitle()
False
'shxhjxjx'isidentifier()
SyntaxError: invalid syntax
'jdgwjdhjhj'.isidentifier()
True
'jhjdhj^57**((*9)09qjk23o9200000000009'isidentifier()
SyntaxError: invalid syntax
'xhejewufhewwwifu849rij&II*UI@WJH'.isidentifier()
False
l = []
l=list()
l
[]
type(l)
<class 'list'>
l=[7,9,6,]
m=[3,7,9]
l+m
[7, 9, 6, 3, 7, 9]
l*8
[7, 9, 6, 7, 9, 6, 7, 9, 6, 7, 9, 6, 7, 9, 6, 7, 9, 6, 7, 9, 6, 7, 9, 6]
(l+m)*1000

(l+m)*98
[7, 9, 6, 3, 7, 9, 7, 9, 6, 3, 7, 9, 7, 9, 6, 3, 7, 9, 7, 9, 6, 3, 7, 9, 7, 9, 6, 3, 7, 9, 7, 9, 6, 3, 7, 9, 7, 9, 6, 3, 7, 9, 7, 9, 6, 3, 7, 9, 7, 9, 6, 3, 7, 9, 7, 9, 6, 3, 7, 9, 7, 9, 6, 3, 7, 9, 7, 9, 6, 3, 7, 9, 7, 9, 6, 3, 7, 9, 7, 9, 6, 3, 7, 9, 7, 9, 6, 3, 7, 9, 7, 9, 6, 3, 7, 9, 7, 9, 6, 3, 7, 9, 7, 9, 6, 3, 7, 9, 7, 9, 6, 3, 7, 9, 7, 9, 6, 3, 7, 9, 7, 9, 6, 3, 7, 9, 7, 9, 6, 3, 7, 9, 7, 9, 6, 3, 7, 9, 7, 9, 6, 3, 7, 9, 7, 9, 6, 3, 7, 9, 7, 9, 6, 3, 7, 9, 7, 9, 6, 3, 7, 9, 7, 9, 6, 3, 7, 9, 7, 9, 6, 3, 7, 9, 7, 9, 6, 3, 7, 9, 7, 9, 6, 3, 7, 9, 7, 9, 6, 3, 7, 9, 7, 9, 6, 3, 7, 9, 7, 9, 6, 3, 7, 9, 7, 9, 6, 3, 7, 9, 7, 9, 6, 3, 7, 9, 7, 9, 6, 3, 7, 9, 7, 9, 6, 3, 7, 9, 7, 9, 6, 3, 7, 9, 7, 9, 6, 3, 7, 9, 7, 9, 6, 3, 7, 9, 7, 9, 6, 3, 7, 9, 7, 9, 6, 3, 7, 9, 7, 9, 6, 3, 7, 9, 7, 9, 6, 3, 7, 9, 7, 9, 6, 3, 7, 9, 7, 9, 6, 3, 7, 9, 7, 9, 6, 3, 7, 9, 7, 9, 6, 3, 7, 9, 7, 9, 6, 3, 7, 9, 7, 9, 6, 3, 7, 9, 7, 9, 6, 3, 7, 9, 7, 9, 6, 3, 7, 9, 7, 9, 6, 3, 7, 9, 7, 9, 6, 3, 7, 9, 7, 9, 6, 3, 7, 9, 7, 9, 6, 3, 7, 9, 7, 9, 6, 3, 7, 9, 7, 9, 6, 3, 7, 9, 7, 9, 6, 3, 7, 9, 7, 9, 6, 3, 7, 9, 7, 9, 6, 3, 7, 9, 7, 9, 6, 3, 7, 9, 7, 9, 6, 3, 7, 9, 7, 9, 6, 3, 7, 9, 7, 9, 6, 3, 7, 9, 7, 9, 6, 3, 7, 9, 7, 9, 6, 3, 7, 9, 7, 9, 6, 3, 7, 9, 7, 9, 6, 3, 7, 9, 7, 9, 6, 3, 7, 9, 7, 9, 6, 3, 7, 9, 7, 9, 6, 3, 7, 9, 7, 9, 6, 3, 7, 9, 7, 9, 6, 3, 7, 9, 7, 9, 6, 3, 7, 9, 7, 9, 6, 3, 7, 9, 7, 9, 6, 3, 7, 9, 7, 9, 6, 3, 7, 9, 7, 9, 6, 3, 7, 9, 7, 9, 6, 3, 7, 9, 7, 9, 6, 3, 7, 9, 7, 9, 6, 3, 7, 9, 7, 9, 6, 3, 7, 9, 7, 9, 6, 3, 7, 9, 7, 9, 6, 3, 7, 9, 7, 9, 6, 3, 7, 9, 7, 9, 6, 3, 7, 9, 7, 9, 6, 3, 7, 9, 7, 9, 6, 3, 7, 9, 7, 9, 6, 3, 7, 9, 7, 9, 6, 3, 7, 9, 7, 9, 6, 3, 7, 9, 7, 9, 6, 3, 7, 9, 7, 9, 6, 3, 7, 9, 7, 9, 6, 3, 7, 9, 7, 9, 6, 3, 7, 9, 7, 9, 6, 3, 7, 9]
l[0]
7
l[6]
Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    l[6]
IndexError: list index out of range
m[1]
7
l[0:1:1]
[7]
m[7:2:1]
[]
m[0:2::]
SyntaxError: invalid syntax
l[::-1]
[6, 9, 7]
m[1::]
[7, 9]
l[:1:2:3]
SyntaxError: invalid syntax
m[4:2]
[]
l[::9]
[7]
4 not in l
True
10 not in m
True
10 in l
False
40 in l
False
40 in m
False
9 in m
True
7 in l,m
(True, [3, 7, 9])
7 in (1,m)
False
655 not in m
True
100000 in l
False
13 in m
False
l = [10,20,30,40,50]
l
[10, 20, 30, 40, 50]
id[1]
Traceback (most recent call last):
  File "<pyshell#70>", line 1, in <module>
    id[1]
TypeError: 'builtin_function_or_method' object is not subscriptable
id(1)
140725234779048
1[4]
Traceback (most recent call last):
  File "<pyshell#72>", line 1, in <module>
    1[4]
TypeError: 'int' object is not subscriptable
l[4]
50
l[4]=100
l
[10, 20, 30, 40, 100]
l.append(120)
l
[10, 20, 30, 40, 100, 120]
l.append(400)

l
[10, 20, 30, 40, 100, 120, 400]
l.extend([2,90])
l.extend([6,99])
l
[10, 20, 30, 40, 100, 120, 400, 2, 90, 6, 99]
l.insert(4,70)
l
[10, 20, 30, 40, 70, 100, 120, 400, 2, 90, 6, 99]
l.insert(0,909)
l
[909, 10, 20, 30, 40, 70, 100, 120, 400, 2, 90, 6, 99]
l.insert(4,80,800)
Traceback (most recent call last):
  File "<pyshell#88>", line 1, in <module>
    l.insert(4,80,800)
TypeError: insert expected 2 arguments, got 3
l
[909, 10, 20, 30, 40, 70, 100, 120, 400, 2, 90, 6, 99]
l.pop()
99
l.pop(0)
909
l.pop(1)
20
l.remove(400)
l
[10, 30, 40, 70, 100, 120, 2, 90, 6]
l.remove(100)
l
[10, 30, 40, 70, 120, 2, 90, 6]
l.del(3)
SyntaxError: invalid syntax
l.del(0)
SyntaxError: invalid syntax
l.del(6)
SyntaxError: invalid syntax
l.del[6]
SyntaxError: invalid syntax
del l[4]
l
[10, 30, 40, 70, 2, 90, 6]
del l[0]
l
[30, 40, 70, 2, 90, 6]
l.clear()
l
[]
[10, 30, 40, 70, 100, 120, 2, 90, 6]
[10, 30, 40, 70, 100, 120, 2, 90, 6]
l
[]
l = [200,30,44,88,66,80,19,77]
l
[200, 30, 44, 88, 66, 80, 19, 77]
sorted(l)
[19, 30, 44, 66, 77, 80, 88, 200]
>>> l.sort()
>>> min(l)
19
>>> max(l)
200
>>> l.reverse()
>>> l
[200, 88, 80, 77, 66, 44, 30, 19]
>>> sorted(l,reverse=true)
Traceback (most recent call last):
  File "<pyshell#118>", line 1, in <module>
    sorted(l,reverse=true)
NameError: name 'true' is not defined. Did you mean: 'True'?
>>> l.sorted(reverse=True)
Traceback (most recent call last):
  File "<pyshell#119>", line 1, in <module>
    l.sorted(reverse=True)
AttributeError: 'list' object has no attribute 'sorted'. Did you mean: 'sort'?
>>> sorted(l,reverse=True)
[200, 88, 80, 77, 66, 44, 30, 19]
>>> l.index(6)
Traceback (most recent call last):
  File "<pyshell#122>", line 1, in <module>
    l.index(6)
ValueError: 6 is not in list
>>> l.index(30)
6
>>> l.index(200)
0
>>> l.count(30)
1
>>> l.count(200)
1
>>> l.count(77)
1
>>> l
[200, 88, 80, 77, 66, 44, 30, 19]
>>> len(l)
8
>>> sum(l)
604
>>> # 0 0.0 '' [] () set() False
>>> any([1,2,4,5,5,0,0,0,0,0])
True
>>> all([1,2,4,5,5,0,0,0,0,0])
False
