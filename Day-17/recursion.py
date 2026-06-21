'''
def func():
    if basecondi:
        return
    func()


def func(num):
    if num == 0:
        return
    print(num,end=' ')
    func(num-1)
    print(num,end=' ')

func(5)


#reverse recursion
def func(num):
    if num == 0:
        return
    print(num,end=' ')
    func(num-1)

func(5)
    

#recursion
def func(num):
    if num == 0:
        return
    #print(num,end=' ')
    func(num-1)
    print(num,end=' ')

func(5)


def sumofdigits(n):
    if n==0:
        return 0
    return n+sumofdigits(n-1)
print(sumofdigits(5))


def sumofdigits(n):
    if n==0:
        return 1
    return n*sumofdigits(n-1)
print(sumofdigits(5))




def power(base,pow):
    if pow == 0:
        return 1
    return base * power(base,pow-1)

print(pow(3,5))
print(pow(2,3))



def reverseofstr(s,ind):
    if ind == 0:
        return s[0]
    return s[ind]+reverseofstr(s,ind-1)

l="Python Programming"
print(reverseofstr(l,len(l)-1))
'''

