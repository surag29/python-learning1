def sum(a,b):
    return a+b
print(sum(33,35))


def pract(name,age=22):
    print(f"your  age is {age} and name is {name}")
pract(name = "surag",age = 21)


def palindrome_check(st):
    rev = ""
    for i in range(len(st)-1,-1,-1):
        rev = rev+st[i]
    if rev ==st:
            print(f"it is palindrome {st}")
    else:
            print(f"not a palindrome {st}")
palindrome_check("surag")



def greatest(a,b,c):
    if a>=b and a>=c:
        print(f"{a} is greatest")
    elif b>=a and b>=c:
        print(f"{b} is greatest")
    else:
        print(f"{c} is greatest")

greatest(4,8,5)


for i in range(1,6):
    print("hello world",end = " ")

n =  int(input("enter the number "))
for i in range(n,0,-1):
    print("*"*i)



def sum_of_natural_numbers(n):
    if n==1:
        return 1
    else:
        return n + sum_of_natural_numbers(n-1)
print(sum_of_natural_numbers(5))

def star(n):
    if n==0:
        return
    else:
        print("*"*n)
        star(n-1)
star(5)

def inch_to_cm(inch):
    cm = inch*2.54
    return cm
n = int(input("enter the inch value "))
print(inch_to_cm(n))

def multiplication_table(n):
    for i in range(1,11):
        print(f"{n} x {i} = {n*i}")
multiplication_table(7)
    

