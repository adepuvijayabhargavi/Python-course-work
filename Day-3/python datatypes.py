Python 3.13.5 (tags/v3.13.5:6cb20a2, Jun 11 2025, 16:15:46) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
a=10
type(a)
<class 'int'>
t=999.99
type(t)
<class 'float'>
c=12+8j
type(c)
<class 'complex'>
<class 'complex'>
SyntaxError: invalid syntax
SyntaxError: invalid syntax s='python'
SyntaxError: invalid syntax
s='dfghjk'
type(s)
<class 'str'>
s='''hgvjhh'''
type(s)
<class 'str'>
1=[]
SyntaxError: cannot assign to literal here. Maybe you meant '==' instead of '='?
>>> l=[]
>>> l=list()
>>> type(1)
<class 'int'>
>>> t=()
>>> t=(1,2,34,5,88)
>>> t
(1, 2, 34, 5, 88)
>>> type(t)
<class 'tuple'>
>>> s={1,2,3,4,6}
>>> tye(s)
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    tye(s)
NameError: name 'tye' is not defined. Did you mean: 'type'?
>>> type(s)
<class 'set'>
>>> s=set()
>>> s={45678, 546, 3456, 13423}
>>> a
10
>>> s
{3456, 546, 45678, 13423}
>>> {3456, 546, 45678, 13423}  d={'name':'avb','age':100,'course':'gbhj'}
SyntaxError: invalid syntax
>>> d = {'name':'abg','age':100,'course':'hjhj'}
>>> type(d)
<class 'dict'>
>>> status =True
>>> status =False
>>> type(status)
<class 'bool'>
>>> a= none
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    a= none
NameError: name 'none' is not defined. Did you mean: 'None'?
>>> a = none
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    a = none
NameError: name 'none' is not defined. Did you mean: 'None'?
>>> a = None
>>> type(a)
<class 'NoneType'>
