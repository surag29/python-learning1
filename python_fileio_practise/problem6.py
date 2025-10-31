word = ["donkey" , "bad",  "gande"]
with open("python_fileio_practise\\file2.txt","r") as f:
    content = f.read()
for words in word:
    content = content.replace(words,"####")

with open("python_fileio_practise\\file2.txt","w") as f:
    f.write(content)