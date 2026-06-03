Python 3.13.5 (tags/v3.13.5:6cb20a2, Jun 11 2025, 16:15:46) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
s = 'python programming'
len(s)
18
sorted(s)
[' ', 'a', 'g', 'g', 'h', 'i', 'm', 'm', 'n', 'n', 'o', 'o', 'p', 'p', 'r', 'r', 't', 'y']
min(s)
' '
max(s)
'y'

ord('a')
97
ord('A')
65
ord('d')
100
ord('o')
111
char(12')
     
SyntaxError: unterminated string literal (detected at line 1)
char('5')
     
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    char('5')
NameError: name 'char' is not defined. Did you mean: 'chr'?
ord('m')
     
109
chr('43')
     
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    chr('43')
TypeError: 'str' object cannot be interpreted as an integer
chr(76)
     
'L'
chr(21)
     
'\x15'
chr(09)
     
SyntaxError: leading zeros in decimal integer literals are not permitted; use an 0o prefix for octal integers
chr(9)
     
'\t'
chr(1)
     
'\x01'
chr(37)
     
'%'
chr(8)
     
'\x08'
chr(55)
     
'7'
s = 'python Programming'
     
s.upper(s)
     
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    s.upper(s)
TypeError: str.upper() takes no arguments (1 given)
s.upper()
     
'PYTHON PROGRAMMING'
s.lower()
     
'python programming'
s.capitalize()
     
'Python programming'
s.title()
     
'Python Programming'
s.swapcase()
     
'PYTHON pROGRAMMING'
s
     
'python Programming'
>>> s.center(28,'-')
...      
'-----python Programming-----'
>>> s.center(26,,'*')
...      
SyntaxError: invalid syntax
>>> s.center(26,'*')
...      
'****python Programming****'
>>> s.ljust(28,'-')
...      
'python Programming----------'
>>> s.rjust(28,'-')
...      
'----------python Programming'
>>> '123'.zfill(5)
...      
'00123'
>>> '123'.zfill(20)
...      
'00000000000000000123'
>>> '123.zfill(2)
...      
SyntaxError: unterminated string literal (detected at line 1)
>>> '123':zfill(2)
...      
SyntaxError: illegal target for annotation
>>> '123'.zfill(3)
...      
'123'
>>> s.find('g')
...      
10
>>> s.rfind('o')
...      
9
>>> s.find('z')
...      
-1
>>> s.index('o')
...      
4
>>> s.rindex('o')
...      
9
>>> s.index('z')
     
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    s.index('z')
ValueError: substring not found
s.index('p')
     
0
s
     
'python Programming'
s.count('y')
     
1
s.count('m')
     
2
s.count('g')
     
2
s
     
'python Programming'
s.replace('python','java')
     
'java Programming'
s.maketrans('Python','123456')
     
{80: 49, 121: 50, 116: 51, 104: 52, 111: 53, 110: 54}

s.translate(s.maketrans('python','123456'))
     
'123456 Pr5grammi6g'
s = 'java,python,javascript,c,c++'
     
s.split()
     
['java,python,javascript,c,c++']
s.split(',',2)
     
['java', 'python', 'javascript,c,c++']
s.rscript(',',2)
     
Traceback (most recent call last):
  File "<pyshell#60>", line 1, in <module>
    s.rscript(',',2)
AttributeError: 'str' object has no attribute 'rscript'. Did you mean: 'rstrip'?
s.rsplit(',',2)
     
['java,python,javascript', 'c', 'c++']
g = 'sdfgh'
     
g = '''guhjkjh'''
     
g = '''ghygsghwdh
gfghjhj
hgjnk
hbj'''
     
g
     
'ghygsghwdh\ngfghjhj\nhgjnk\nhbj'
s.splitlines()
     
['java,python,javascript,c,c++']
g.splitlines()
     
['ghygsghwdh', 'gfghjhj', 'hgjnk', 'hbj']
l = ['java','python','javascript','c','c++']
     
''.join(1)
     
Traceback (most recent call last):
  File "<pyshell#72>", line 1, in <module>
    ''.join(1)
TypeError: can only join an iterable
''.join(l)
     
'javapythonjavascriptcc++'
'-'.join(1)
     
Traceback (most recent call last):
  File "<pyshell#74>", line 1, in <module>
    '-'.join(1)
TypeError: can only join an iterable
'-'.join(l)
     
'java-python-javascript-c-c++'
'@'.join(l)
     
'java@python@javascript@c@c++'
' '.join(l)
     
'java python javascript c c++'
','.join(l)
     
'java,python,javascript,c,c++'
s
     
'java,python,javascript,c,c++'
s.partition(',')
     
('java', ',', 'python,javascript,c,c++')
s.rpartition(',')
     
('java,python,javascript,c', ',', 'c++')
t = "Hello"
     
t.encode()
     
b'Hello'
b'Hello'.decode()
     
'Hello'
