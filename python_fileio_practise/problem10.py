with open("python_fileio_practise\\this.txt","r") as f:
    content1 = f.read()
with open("mythis.txt","r") as f:
    content2 = f.read()
if content1 == content2:
    print("both files are same")
else:
    print("files are different")

