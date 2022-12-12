f = open('./puzzle-001-input.txt')
elfs = []
tmp = 0

for line in f:
    if line == "\n":
        elfs.append(tmp)
        tmp = 0
    else:
        tmp = tmp + int(line)
    
elfs.sort(reverse=True)

print("Top #1", elfs[0])
print("Top #3", (elfs[0]+elfs[1]+elfs[2]))

del f, elfs, tmp