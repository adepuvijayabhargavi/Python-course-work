'''
n=list(map(int,input().split()))
print("length:",len(n))
print("sorted:",sorted(n))
print("maximum:",max(n))
print("minimum:",min(n))

'''
tup=tuple(input("Tuple : ").split())
pro=input("Product: ")
pri=int(input("Price:"))
s = set (map(int,input("Set Values : ").split()))

print("Tuple:",tup)
d={}
d[pro]=pri
print("Dictionary:",d)
print("set:",s)

'''
salary=int(input())
bonus=0

if salary>=70000:
    bonus=salary *0.2
elif salary >= 50000:
    bonus=salary*0.5
elif salary>=30000:
    bonus=salary*0.1
else:
    bonus=salary*0.05

print("Bonus:",bonus)


'''
age=int(input())
if age>=18:
    print("Eligible for voting")
else:
    print("Not Eligible for voting")

'''
marks=int(input())
if marks>=35:
    print("Pass")
else:
    print("Fail")

