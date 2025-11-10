from functools import reduce
a = [22,3,4,5,6,79,80]
def gt(a,b):
    if(a>b):
      return a
    return b

gtt = reduce(gt,a)
print(gtt)