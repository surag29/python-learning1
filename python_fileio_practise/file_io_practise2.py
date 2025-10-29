# f =  open("myfile.txt","r")
# content1 = f.readline()
# print(content1)
# content2 = f.readline()
# print(content2)
# content3 = f.readline()
# print(content3)
# f.close()


# f = open("myfile.txt","w")
# f.write("adding a new line to the file\n")
# f.close()
# f = open("myfile.txt","r")
# content4 = f.read()
# print(content4)
# f.close()


f = open("python_fileio_practise\\poem.text")
content = f.read()
n =  input("enter the word to be searched:")

if(n in content):
    print(f"yes, {n} is present in the file")
else:
    print(f"no, {n} is not present in the file")
f.close
# help(dict)