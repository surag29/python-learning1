def decorator(func):  # this captures your funtion that is add
    def wrapper(a,b):  # this captures your arguments or paramteres
        print("this will be printed before the method ")
        func(a,b)
        print("this will be printed after ")
    return wrapper

  




@decorator
def add(a,b):
    print(f"the addition of the two numbers is {a+b}")

add(5,10)


