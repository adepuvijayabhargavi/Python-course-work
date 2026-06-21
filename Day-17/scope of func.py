'''
#local scope
--------------------------
def display():
    n=10
    print("Inside:",n)

display()
print("Outside:",n)

#global access
--------------------------
n=10
def display():
    print("Inside:",n)

display()
print("Outside:",n)
n=10
def display():
    print("Inside:",n)
display()
print("Outside:",n)

#global access
-------------------------
def display():
    global n
    n=10
    print("Inside:",n)

display()
print("Outside:",n)

#global key word
------------------------
def display():
   global n
   n+=10
   print("Inside:",n)

n=10
display()
print("Outside:",n)

#nonlocal function
-------------------------
def outer():
    n=10
    def inner():
        nonlocal n
        n+=10
        print("Inner function:",n)
    inner()

    print("Outer function:",n)

outer()

#no execution for variable declaration
s='python'
print(len(s))

len=5
print(len(s))

#pass by values-passing immutable items

def update(n):
    n+=10
    print("Inside:",n)

n=19
update(n)
print("Outside:",n)


def update(n):
    n+=10.1
    print("Inside:",n)

n=19.2
update(n)
print("Outside:",n)

def update(n):
    n+=10
    print("Inside:",n)

n=12+3j
update(n)
print("Outside:",n)

def update(n):
    n+=(1,11,2,22)
    print("Inside:",n)

n=(6,9,88)
update(n)
print("Outside:",n)


def update(n):
    n+=[1,11,2,22]
    print("Inside:",n)

n=[6,9,88]
update(n)
print("Outside:",n)

'''
def update(n):
    n.append (8)
    print("Inside:",n)

n={6,9,88}
update(n)
print("Outside:",n)

