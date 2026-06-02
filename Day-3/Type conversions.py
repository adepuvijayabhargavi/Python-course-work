Python 3.13.5 (tags/v3.13.5:6cb20a2, Jun 11 2025, 16:15:46) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> a=10
>>> a
10
>>> float(a)
10.0
>>> complex(a)
(10+0j)
>>> str(a)
'10'
>>> list(a)
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    list(a)
TypeError: 'int' object is not iterable
>>> tuple(a)
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    tuple(a)
TypeError: 'int' object is not iterable
>>> set(a)
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    set(a)
TypeError: 'int' object is not iterable
>>> dict(a)
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    dict(a)
TypeError: 'int' object is not iterable
>>> bool(a)
True
>>> b=10.5
>>> int(b)
10
>>> complex(b)
(10.5+0j)
>>> str(b)
'10.5'
>>> list(b)
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    list(b)
TypeError: 'float' object is not iterable
>>> tuple(b)
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    tuple(b)
TypeError: 'float' object is not iterable
set(a)
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    set(a)
TypeError: 'int' object is not iterable
dict(a)
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    dict(a)
TypeError: 'int' object is not iterable
bool(a)
True
c=2+3j
int(c)
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    int(c)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'complex'
c
(2+3j)
float(c)
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    float(c)
TypeError: float() argument must be a string or a real number, not 'complex'
str(c)
'(2+3j)'
list(a)
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    list(a)
TypeError: 'int' object is not iterable
tuple(c)
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    tuple(c)
TypeError: 'complex' object is not iterable
set(c)
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    set(c)
TypeError: 'complex' object is not iterable
dict(c)
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    dict(c)
TypeError: 'complex' object is not iterable
bool(c)
True
s='python'
a='465767'
b='65767.878'
int(s)
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    int(s)
ValueError: invalid literal for int() with base 10: 'python'
int(a)
465767
int(b)
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    int(b)
ValueError: invalid literal for int() with base 10: '65767.878'
float(s)
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    float(s)
ValueError: could not convert string to float: 'python'
float(a)
465767.0
float(b)
65767.878
complex(s)
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    complex(s)
ValueError: complex() arg is a malformed string
complex(a)
(465767+0j)
complex(b)
(65767.878+0j)
list(s)
['p', 'y', 't', 'h', 'o', 'n']
list(a)
['4', '6', '5', '7', '6', '7']
list(b)
['6', '5', '7', '6', '7', '.', '8', '7', '8']
tuple(s)
('p', 'y', 't', 'h', 'o', 'n')
tuple(a)
('4', '6', '5', '7', '6', '7')
tuple(b)
('6', '5', '7', '6', '7', '.', '8', '7', '8')
set(s)
{'y', 't', 'n', 'o', 'p', 'h'}
set(a)
{'5', '4', '7', '6'}
set(b)
{'7', '6', '.', '8', '5'}
dict(s)
Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    dict(s)
ValueError: dictionary update sequence element #0 has length 1; 2 is required
dict(a)
Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    dict(a)
ValueError: dictionary update sequence element #0 has length 1; 2 is required
dict(b)
Traceback (most recent call last):
  File "<pyshell#54>", line 1, in <module>
    dict(b)
ValueError: dictionary update sequence element #0 has length 1; 2 is required
bool(s)
True
bool(a)
True
bool(b)
True
l=[67,7,98,04,32]
SyntaxError: leading zeros in decimal integer literals are not permitted; use an 0o prefix for octal integers
l=[89,77,44,21,6]
l
[89, 77, 44, 21, 6]
int(l)
Traceback (most recent call last):
  File "<pyshell#61>", line 1, in <module>
    int(l)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'list'
float(l)
Traceback (most recent call last):
  File "<pyshell#62>", line 1, in <module>
    float(l)
TypeError: float() argument must be a string or a real number, not 'list'
complex(l)
Traceback (most recent call last):
  File "<pyshell#63>", line 1, in <module>
    complex(l)
TypeError: complex() first argument must be a string or a number, not 'list'
str(l)
'[89, 77, 44, 21, 6]'
tuple(l)
(89, 77, 44, 21, 6)
set(l)
{6, 44, 77, 21, 89}
bool(l)
True
t=(4,rea,8.8,33,99)
Traceback (most recent call last):
  File "<pyshell#68>", line 1, in <module>
    t=(4,rea,8.8,33,99)
NameError: name 'rea' is not defined
