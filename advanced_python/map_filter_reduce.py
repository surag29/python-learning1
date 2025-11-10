from functools import reduce

#map example

l = [1,2,33,4,5,6,7]

square = lambda x: x*x
sqlist = map(square,l)
print(list(sqlist))

#filter example 
def even(n):
    if(n%2==0):
        return True
    return False

slist = filter(even,l)
print(list(slist))
  
#reduce example
def sum(a,b):
    return a+b
print(reduce(sum,l))