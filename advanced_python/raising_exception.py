a =  int(input("enter the first number :"))
b =  int(input("enter the second number :"))

if(b==0):
    raise ZeroDivisionError("hey our program is not meant to divide numbers by 0")  #we can raise our own exceptions
else:
    print(f"the divison of the both the number is {a/b}")