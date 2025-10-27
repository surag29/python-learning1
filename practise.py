n =  int(input("Enter a number: "))
evensum = 0
oddsum = 0
for i in range(1,n):
    if i%2==0:
        evensum += i
    else:
        oddsum += i
print("Sum of even numbers:", evensum)
print("Sum of odd numbers:", oddsum)

