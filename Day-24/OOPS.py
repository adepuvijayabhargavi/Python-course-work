'''
class Flipkart:
    pass

bhargavi = Flipkart()
komali = Flipkart()
ashrutha = Flipkart()


class Flipkart:
    discount = 10
    products = ['laptop','phone','mouse','charger']

    @classmethod
    def showproducts(cls):
        print(cls.products)

    def login(self,username,password):
        self.username = username
        self.password = password
        print(f'Welcome to the flipkart {self.username}')

    @staticmethod
    def banner():
        print("10% discount is going on flipkart, show now!")

pranathi = Flipkart()
pranathi.login('pranathi','pranathi@123')
pranathi.banner()
pranathi.showproducts()

Flipkart.showproducts()
Flipkart.banner()



class instagram:
   def __init__(self,username,password):
        self.username = username
        self.password = password
        self.followers = []
        print(f'Welcome to the Instagram, {self.username}')

bhargavi = instagram('bhargavi','bhargavi@123')
               


class Instagram:
    def __init__(self,username,password):
        self.username = username
        self. __password = password
        self.followers = []

    def getpassword(self):
        return self.__password

    def setpassword(self,newpassword):
        self.__password = newpassword

bhargavi = Instagram('bhargavi','bhargavi@123')

print("Before username:",bhargavi.username)
bhargavi.username = 'akhila'
print("After username:",bhargavi.username)

print("Before password:",bhargavi.getpassword())
bhargavi.setpassword('akhila@123')
print("After password:",bhargavi.getpassword())


'''

class Instagram:
    def __init__(self):
        self._post = []

    @property
    def accesspost(self):
        return self._post

    @accesspost.setter
    def accesspost(self,newpost):
        self._post.append(newpost)

bhargavi = Instagram()

print(bhargavi.accesspost)
bhargavi.accesspost = 'class and object'
print(bhargavi.accesspost)

