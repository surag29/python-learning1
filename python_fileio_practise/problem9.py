with open("python_fileio_practise\\this.txt","r") as f:
    content = f.read()
with open("mythis.txt","w") as f:
    f.write(content)