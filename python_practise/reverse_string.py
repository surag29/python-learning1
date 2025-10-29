a = "madam"
b = ""
# print(a[::-1])
for i in range(len(a)-1,-1,-1):
 b = b+a[i]
print(b)

if b==a:
    print("palindrome")
else:
    print("not palindrome")