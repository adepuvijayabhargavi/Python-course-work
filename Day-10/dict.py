Python 3.13.5 (tags/v3.13.5:6cb20a2, Jun 11 2025, 16:15:46) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
d={}
d
{}
d=dict()
d
{}
type(d)
<class 'dict'>
d={'k1':'v1','k2':'v2','k3':'v2'}
d
{'k1': 'v1', 'k2': 'v2', 'k3': 'v2'}
d={}
d[1]
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    d[1]
KeyError: 1
d[l]='int'
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    d[l]='int'
NameError: name 'l' is not defined
d[1]='int'
d
{1: 'int'}
d[12.3]='float'
d
{1: 'int', 12.3: 'float'}
d[2+87j]
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    d[2+87j]
KeyError: (2+87j)
d[6+88j]='complex'
d
{1: 'int', 12.3: 'float', (6+88j): 'complex'}
d[[1,2,3,4]]='list'
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    d[[1,2,3,4]]='list'
TypeError: unhashable type: 'list'
d[[2,3,4,5]]
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    d[[2,3,4,5]]
TypeError: unhashable type: 'list'
d[(2,3,4,5)]='tuple'
d
{1: 'int', 12.3: 'float', (6+88j): 'complex', (2, 3, 4, 5): 'tuple'}
d[false]='bool'
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    d[false]='bool'
NameError: name 'false' is not defined. Did you mean: 'False'?
d[False]='bool'
d
{1: 'int', 12.3: 'float', (6+88j): 'complex', (2, 3, 4, 5): 'tuple', False: 'bool'}
d={}
d[1]=1
d
{1: 1}
d[23]
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    d[23]
KeyError: 23
d[3]
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    d[3]
KeyError: 3
d
{1: 1}
d[3]
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    d[3]
KeyError: 3
d={}
d
{}
d[23]=23.4
d[3]='gfhj'
d[4]=4+6j
d[5]=[3,2,1]
d[6]=(1,2,3)
d[7]={1,3}
d[8]={1:1,2:2}
d[9]=False
d
{23: 23.4, 3: 'gfhj', 4: (4+6j), 5: [3, 2, 1], 6: (1, 2, 3), 7: {1, 3}, 8: {1: 1, 2: 2}, 9: False}
d={}
d
{}
d[1]=2
d[2]=2
d[3]=2
d[4]=2
d
{1: 2, 2: 2, 3: 2, 4: 2}
d
{1: 2, 2: 2, 3: 2, 4: 2}
d[3]
2
d={1:2,2:4,3:6,4:8,5:10,6:12]
SyntaxError: closing parenthesis ']' does not match opening parenthesis '{'
d={1:2,2:4,3:6,4:8,5:10,6:12}
d[4]
8
d[6]
12
d[2]
4
d={'komalatha':89,'bhargavi':76,'subbu':90,'nagendra':76}
d['bhargavi']
76
d['subbu']
90
d['kayva']
Traceback (most recent call last):
  File "<pyshell#59>", line 1, in <module>
    d['kayva']
KeyError: 'kayva'
d['nagendra']
76
d['sahith']
Traceback (most recent call last):
  File "<pyshell#61>", line 1, in <module>
    d['sahith']
KeyError: 'sahith'
d.get('sahith')
d.get('dinesh')
d.get('bhargavi')
76
d.get('akhil','user not found')
'user not found'
d.get('subbu','user not found')
90
d
{'komalatha': 89, 'bhargavi': 76, 'subbu': 90, 'nagendra': 76}
'akhil' in d
False
'bhargavi' in d
True
'komalatha' not in d
False
'sunny' not in d
True
'subbu' not in d
False
d.keys()
dict_keys(['komalatha', 'bhargavi', 'subbu', 'nagendra'])
d.values()
dict_values([89, 76, 90, 76])
d.items()
dict_items([('komalatha', 89), ('bhargavi', 76), ('subbu', 90), ('nagendra', 76)])
sorted(d)
['bhargavi', 'komalatha', 'nagendra', 'subbu']
max(d)
'subbu'
min(d)
'bhargavi'
len(b)
Traceback (most recent call last):
  File "<pyshell#79>", line 1, in <module>
    len(b)
NameError: name 'b' is not defined
len(d)
4
max(len)
Traceback (most recent call last):
  File "<pyshell#81>", line 1, in <module>
    max(len)
TypeError: 'builtin_function_or_method' object is not iterable
d['komalatha']
89
d['komalatha']=200
d
{'komalatha': 200, 'bhargavi': 76, 'subbu': 90, 'nagendra': 76}
d['bhargavi']=60
d
{'komalatha': 200, 'bhargavi': 60, 'subbu': 90, 'nagendra': 76}
d['rishi']
Traceback (most recent call last):
  File "<pyshell#87>", line 1, in <module>
    d['rishi']
KeyError: 'rishi'
d['rishi']=67
d
{'komalatha': 200, 'bhargavi': 60, 'subbu': 90, 'nagendra': 76, 'rishi': 67}
d.update({'praneeth':90,'manideep':99})

d
{'komalatha': 200, 'bhargavi': 60, 'subbu': 90, 'nagendra': 76, 'rishi': 67, 'praneeth': 90, 'manideep': 99}
d.popitem()
('manideep', 99)
d
{'komalatha': 200, 'bhargavi': 60, 'subbu': 90, 'nagendra': 76, 'rishi': 67, 'praneeth': 90}
d.remove('komalatha')
Traceback (most recent call last):
  File "<pyshell#94>", line 1, in <module>
    d.remove('komalatha')
AttributeError: 'dict' object has no attribute 'remove'
>>> remove('komalatha')
Traceback (most recent call last):
  File "<pyshell#95>", line 1, in <module>
    remove('komalatha')
NameError: name 'remove' is not defined
>>> del d['komalatha']
>>> d
{'bhargavi': 60, 'subbu': 90, 'nagendra': 76, 'rishi': 67, 'praneeth': 90}
>>> d.pop(subbu)
Traceback (most recent call last):
  File "<pyshell#98>", line 1, in <module>
    d.pop(subbu)
NameError: name 'subbu' is not defined
>>> d.pop('subbu)
...       
SyntaxError: unterminated string literal (detected at line 1)
>>> d.pop('subbu')
...       
90
>>> d.clear()
...       
>>> d
...       
{}
>>> d={'komalatha': 200, 'bhargavi': 60, 'subbu': 90, 'nagendra': 76, 'rishi': 67, 'praneeth': 90, 'manideep': 99}
...       
>>> d
...       
{'komalatha': 200, 'bhargavi': 60, 'subbu': 90, 'nagendra': 76, 'rishi': 67, 'praneeth': 90, 'manideep': 99}
>>> d.setdefault('rishi',0)
...       
67
>>> d.setdefault('sathish',0)
...       
0
>>> d
...       
{'komalatha': 200, 'bhargavi': 60, 'subbu': 90, 'nagendra': 76, 'rishi': 67, 'praneeth': 90, 'manideep': 99, 'sathish': 0}
>>> d.get('pranathi',0)
...       
0
>>> d
...       
{'komalatha': 200, 'bhargavi': 60, 'subbu': 90, 'nagendra': 76, 'rishi': 67, 'praneeth': 90, 'manideep': 99, 'sathish': 0}
