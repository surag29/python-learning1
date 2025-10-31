with open("python_fileio_practise\\log.txt","r") as f:
    content = f.read()
if "python" in content:
    print("yes python is present")
else:
    print("np python is not present")



