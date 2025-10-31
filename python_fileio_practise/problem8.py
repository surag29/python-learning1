with open("python_fileio_practise\\log.txt","r") as f :
    lines = f.readlines()
lineno = 1
for line in lines:
    if ("python" in line):
        print(f"python is present in the line number {lineno}")
        break
    lineno+=1
else:
    print("pyhton is not present in the file")
