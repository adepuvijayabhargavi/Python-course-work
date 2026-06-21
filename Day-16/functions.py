'''
def function_name(arg):
    #stmts
    return
function_name(para)


def wish(name):
    print(f'welcome to the python course {name}!')

wish('bhargavi')
wish('komali')
wish('ashrutha')
wish('keerthana')


def iseven(num):
    if num%2==0:
        return f"{num} - Even Number"
    else:
        return f"{num} - Odd Number"

print(iseven(12))
print(iseven(13))


def factorial (num):
    fact=1
    for i in range(1,num+1):
        fact*=i
    return fact

num=int(input("Enter the number: "))
print("Factorial:",factorial(num))


def isprime(num):
    for i in range(2,num//2):
        if num%i==0:
            return f"{num} - Not Prime Number"
    return f"{num} - Prime Number"

num=int(input("Enter the number:"))
print(isprime(num))


def display(name,email,pwd):
    print("Name:",name)
    print("Email:",email)
    print("Password:",pwd)

display('bhargavi','bhargavi@gmail.com','bhargavi@123')
display('komalatha@gmail.com','komali','komali@54')
display('vaishnavi','vaishnu@gmail.com','vaishu@56')

def display(name,email,pwd):
    print("Name:",name)
    print("Email:",email)
    print("Password:",pwd)

display(name='bhargavi',email='bhargavi@gmail.com',pwd='bhargavi@123')
display(email='komalatha@gmail.com',name='komali',pwd='komali@54')
display(email='vaishnu@gmail.com',name='vaishnavi',pwd='vaishu@56')

def display(name,email,pwd=''):
    print("Name:",name)
    print("Email:",email)
    print("Password:",pwd)

display('bhargavi','bhargavi@gmail.com','bhargavi@123')
display('komalatha@gmail.com','komali',)

def display(*names):
    print("Names:",names)

display('bhargavi','komali','priyanka','sadhana','swetha')
display('keerthana','pravallika','ravali','pranathi')
display('bhargavi','komali','priyanka')
display('akhila')

def display(**names):
    print("Names:",names)
display(k1='bhargavi',k2='akhila',k3='pravallika')
display(k1='bhanu')
display(k1='keerthi',k2='rahul')
'''


