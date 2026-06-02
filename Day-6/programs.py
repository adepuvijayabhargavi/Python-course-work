Python 3.13.5 (tags/v3.13.5:6cb20a2, Jun 11 2025, 16:15:46) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
name=input()
bhargavi
name
'bhargavi'
name = input("Enter your name: ")
Enter your name: bhargavi
age = input("Enter your age: ")
Enter your age: 21
type(age)
<class 'str'>
gpa = float(input("Enter the cpa:"))
Enter the cpa:7.8
gpa
7.8
type(gpa)
<class 'float'>
'bhargavi komali vaishanvi ashrutha'
'bhargavi komali vaishanvi ashrutha'
'bhargavi komali vaishanvi ashrutha'.split('')
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    'bhargavi komali vaishanvi ashrutha'.split('')
ValueError: empty separator
products = input("enter the product").split()
enter the productlaptop mouse keyboard charger cable
products
['laptop', 'mouse', 'keyboard', 'charger', 'cable']
topics = tuple(input("enter the topics: ").split())
enter the topics: token tuple statement comments
topics
('token', 'tuple', 'statement', 'comments')
op = set(input("enter the oper: ").split())
enter the oper: in not in is is not and or not
op
{'not', 'is', 'and', 'or', 'in'}
list(map(int,input("Enter the marks: ").split()))
Enter the marks: 23 46 78 90
[23, 46, 78, 90]
prices = tuples(map(int,input("Enter the prices: ").split()))
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    prices = tuples(map(int,input("Enter the prices: ").split()))
NameError: name 'tuples' is not defined. Did you mean: 'tuple'?
prices = tuple(map(int,input("Enter the prices: ").split()))
Enter the prices: 4 3 2 3 2 4 
prices
(4, 3, 2, 3, 2, 4)
rating = set(map(int,input("Enter the prices: ").split()))
Enter the prices: 6 7 8 
prices
(4, 3, 2, 3, 2, 4)
rating = set(map(int,input("Enter the rating: ").split()))
Enter the rating: 2 4 6 7 4 3
rating
{2, 3, 4, 6, 7}
a=10
a
10
b=20
b
20
a, b = 10, 20
a
10
b
20
a, b =(10, 20)
a
10
b
20
a, b = [10, 20]
a
10
b
20
username , password =input("Enter the username & password: ").split()
Enter the username & password: codegnan c@sfghb
password
'c@sfghb'
username
'codegnan'
a, b, c, d= list(map(int,input("enter the 4 sides: ").split()))
enter the 4 sides: 3 5 8 9 
a
3
b
5
c
8
d
9
>>> price, discount = list(map(float,input().split()))
212 60.9
>>> price
212.0
>>> discount
60.9
>>> a = eval(input())
878
>>> a
878
>>> a = eval(input())
7878.8787
>>> a
7878.8787
>>> a = eval(input())
(3,7,9,7,1)
>>> a
(3, 7, 9, 7, 1)
>>> a = eval(input())
[1,5,7,9,0]
>>> a
[1, 5, 7, 9, 0]
>>> a = eval(input())
{2:4,3:6,4:8}
>>> a
{2: 4, 3: 6, 4: 8}
>>> a = eval(input())
True
>>> a
True
>>> type(a)
<class 'bool'>
>>> s='python programming language'
>>> s
'python programming language'
>>> type(s)
<class 'str'>
>>> a = 'codegnan'
>>> b = 'pfs'
>>> a+b
'codegnanpfs'
>>> (a+b)*10
'codegnanpfscodegnanpfscodegnanpfscodegnanpfscodegnanpfscodegnanpfscodegnanpfscodegnanpfscodegnanpfscodegnanpfs'
>>> 'python'*20
'pythonpythonpythonpythonpythonpythonpythonpythonpythonpythonpythonpythonpythonpythonpythonpythonpythonpythonpythonpython'
