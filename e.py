with open('file.txt') as file:
    data = file.read()
names = data.split()
new = open('name_subj.txt','x')

for name in names:
    for a in range(len(names)):
        new.writelines(f"{name} Programming Fundamental lab,Programming Fundamental,English Composition,Calculus-1")
    new.write('\n')
    
