names = {}
for line in open("population.csv", "r"):
    split = line.split(",")
    for items in range(len(split)):
        if items == 0:
            names[split[0]] = []
        else:
            names[split[0]].append(split[items])
print(names)
# works
'''
for i in range(0, len(lines)):

    if (i == 0):
        names[lines[0]] = []
    else:
        names[lines[0]].append(lines[i])
print(names)
'''

    
