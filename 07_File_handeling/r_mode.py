with open("practice.txt", "r") as file:
    data = file.read()

new_data = data.replace("java", "python")
print(new_data)

with open("practice.txt", "w") as file:
    file.write(new_data)