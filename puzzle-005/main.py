import re
import copy

def PuzzleFile():
    import sys

    dir = sys.argv[0].split("/")[1]
    if len(sys.argv) > 1 and sys.argv[1] == "--demo":
        data = "input-demo.txt"
    else:
        data = "input.txt"

    return "./"+dir+"/"+data

f = open(PuzzleFile())
stacks_o = []
moves = []

s = int(len(f.readline())/4)
for i in range(s):
    stacks_o.append([])

f.seek(0)

for line in f:
    data = line
    llen = len(data)

    if data.count("[") > 0 and data.count("]") > 0:
        for i in range(0, llen, 4):
            t = data[i:i+4].strip().replace("[", "").replace("]", "")
            if len(t) > 0:
                stacks_o[int(i/4)].insert(0,t)
    elif data.count("move") > 0:
        move = re.findall("[0-9]+", data)
        for i in range(len(move)):
            move[i] = int(move[i])
        moves.append(move)
    # end if
# end for line in f

del move



def CrateMover9000(stacks:list, moves:list):
    for move in moves:
        move_from = move[1]-1
        move_to = move[2]-1
        for i in range(move[0]):
            cut = stacks[move_from].pop()
            stacks[move_to].append(cut)
            #print(stacks)
        #print("")

    buffer = ""

    for stack in stacks:

        length = len(stack)-1
        if length >= 0:
            buffer += stack[len(stack)-1]

    return buffer

def CrateMover9001(stacks:list, moves:list):
    for move in moves:
        move_from = move[1]-1
        move_to = move[2]-1
        crane_load = []

        for i in range(move[0]):
            crane_load.append(stacks[move_from].pop())

        crane_load.reverse()
    
        for i in crane_load:
            stacks[move_to].append(i)


    buffer = ""

    for stack in stacks:

        length = len(stack)-1
        if length >= 0:
            buffer += stack[len(stack)-1]

    return buffer

stacks9000 = copy.deepcopy(stacks_o)
stacks9001 = copy.deepcopy(stacks_o)

print("INIT:")
print(stacks9000)
print(moves)
print("---")
print("CreateMover9000: ", CrateMover9000(stacks9000, moves))

print("INIT:")
print(stacks9001)
print(moves)
print("---")
print("CreateMover9001: ", CrateMover9001(stacks9001, moves))