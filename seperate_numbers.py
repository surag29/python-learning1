n =  int(input("enter the number: "))
copy =  n
rev = 0
while n>0:
     rev = rev*10+n%10
     n = n//10
if copy == rev:
    print("the number is palindrome", rev)
else:
    print("the number is not palindrome", rev)