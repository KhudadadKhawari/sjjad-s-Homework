with open('file.txt') as file:
    data = file.read()
names = data.split('\n')
for a in range(4):
    print(names[a][:4])

