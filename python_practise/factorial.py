n =  int(input("enter the number to find its factorial:"))
fact = 1
for i in range(1,n+1):
    if n==0 or n==1:
        print(f"factorial of {n} is 1")
        break
    else:
        fact = fact*i
print(f"factorial of {n} is {fact}")

def factorial_recursive(n):
    if n==0 or n==1:
        return 1
    else:
        return n * factorial_recursive(n-1)
print(factorial_recursive(n))