#question 1
a=int(input("enter your number"))
b=bin(a)
print(b)
#ques 2
a=int(input("enter first number"))
b=int(input("enter second number"))
op=input("enter your operator")
if op=="*":
    print(a*b)
elif op=="+":
    print(a+b)
elif op=="-":
    print(a-b)
elif op == "/":
    print(a/b)
elif op=="%":
    print(a%b)
elif op=="//":
    print(a//b)
else:
    print("enter a valid operator")
#ques 3
print((3+4)*(5))
print("\n")

n=int(input("enter your number"))
ans=(n)*(n-1)/2
print(ans)
print("\n")

import math
r=int(input("enter the radius"))
a=4*(math.pi)
ans=a*(r*r)
print(ans)
print("\n")

import math
a=90
b=45
r=int(input("enter value of r"))
c=float(r*(math.cos(a))*2)
d=float(r*(math.sin(a))*2)
ans=math.sqrt(c+d)
print(ans)
print("\n")

x1=int(input("enter value of x1"))
x2=int(input("enter value of x2"))
a=(x2-x1)
y1=int(input("enter value of y1"))
y2=int(input("enter value of y2"))
b=(y2-y1)
ans=(b/a)
print(ans)
print("\n")

#ques 4
for i in range(5):
    print(i,end=" ")
print()
for i in range(3,10):
    print(i,end=" ")
print()
for i in range(4,13,3):
    print(i,end=" ")
print()
for i in range(15,5,-2):
    print(i,end=" ")
print()
for i in range(5,3):
    print(i,end=" ")
#ques 5
a=int(input("enter number of hydrogen atoms"))
b=int(input("enter number of carbon atoms"))
c=int(input("enter number of oxygen atoms"))
print("molecular weight of moleculeis",a*1.00794+b*12.0107+c*15.9994)
