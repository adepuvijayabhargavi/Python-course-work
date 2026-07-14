'''
import sys

print(sys.argv)
print(sys.path)
print(sys.version)

print("Before exit")
sys.exit()
print("After exit")



import platform

print(platform.system(), platform.release(),platform.processor())




import math

print(math.pi)
print(math.e)

print(math.sqrt(25))
print(math.pow(2,5))

print(math.ceil(12.9))
print(math.ceil(12.0333))
print(math.ceil(12.3))
print(math.ceil(12.11))

print(math.floor(12.3))
print(math.floor(12.000001))
print(math.floor(12.9999999))




import math

print(math.fabs(-12))
print(math.factorial(5))
print(math.gcd(8,28))

print(math.log(10,10))
print(math.sin(10))
print(math.cos(10))
print(math.tan(10))
print(math.tan(45))

print(math.degrees(20))
print(math.radians(20))





import random

l=['python','c','c++','java','html']
print(random.choice(l))
print(random.choices(l,k=3))

s='rps'
print(random.choice(s))
print(l)
random.shuffle(l)
print(l)




import random

random.seed(4)
print(random.random())
print(random.randint(1,6))
print(random.uniform(1,6))

l=['python','c','c++','java','html']
print(random.choice(l))
print(random.choices(l,k=3))

s='rps'
print(random.choice(s))
print(l)
random.shuffle(l)
print(l)
'''



