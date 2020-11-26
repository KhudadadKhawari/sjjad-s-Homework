with open('file.txt') as file:
    data = file.read()
names = data.split()

def specific_names(length):
    for name in names:
        if len(name) == length:
            print(name)

specific_names(5)