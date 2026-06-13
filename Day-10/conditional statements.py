s='python programming'

if 'python' in s:
    print('python found')
    
if s[0]=='p':
    print("string is starting with p")




data = ('abc','1234')

username,password = input("Enter the username and password:").split()

if data == (username,password):
    print("Login successfull")
else:
    print("Invalid login")




n = int(input("enter the num:  "))

if n>0:
    print('+ve')
elif n<0:
    print('-ve')
else:
    print("zero")




products ={
    'laptop':0,
    'mouse':10,
    'charger':5,
    'phone':30,
    'keyboard':0
}

product = input("enter the product: ")
if product in products:
    if products[product]!=0:
        print(f"you can buy {product}!!")
    else:
        print(f"{product} is out of stock")
else:
    print(f"{product} is not available")

