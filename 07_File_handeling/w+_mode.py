f = open("sample.txt", "w+")
print(f.read())  # it will print nothing because the file is empty
f.write("Hello, World!")
f.close()