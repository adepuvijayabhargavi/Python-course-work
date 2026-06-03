name = input()
rollno = int(input())
s1 = int(input())
s2 = int(input())
s3 = int(input())

total = s1+s2+s3
avg = total/3

print(f'student name : {name}')
print(f'Roll number : {rollno}')
print(f'Total marks : {total}')
print(f'Average marks : {avg}')


s = input()

print('Total characters :',len(s))
print('First character :',s[0])
print('Last character :'s[-1])
print('Uppercase :'s.upper())
print('Reversed string :'s[::-1])



a,b,c = list(map(int,input().split()))

print('sum :',a+b+c)
print('Average:',(a+b+c)/3)
print('Product:'a*b*c)



