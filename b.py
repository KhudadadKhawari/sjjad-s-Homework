with open('file.txt') as file:
    data = file.read()
names = data.split('\n')
shortest = names[0]
for name in names:
    if len(name) < len(shortest):
        shortest = name
print(shortest)