f = open("file3.txt", "r")
f.seek(3)
print(f.tell())  #tell the current position
text = f.read(4)
print(text)
f.close()