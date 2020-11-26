with open('file.txt') as file:
    data = file.read()
names = data.split('\n')
total_length = 0
for name in names:
    total_length += int(len(name))

print(total_length / int(len(names)))
