with open("python_fileio_practise\\file.txt","r") as f:
    content = f.read()
    print(content)
contentnew = content.replace("donkey","####")
with open("python_fileio_practise\\file.txt","w") as f:
    f.write(contentnew)