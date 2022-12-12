def PuzzleFile():
    import sys

    dir = sys.argv[0].split("/")[1]
    if len(sys.argv) > 1 and sys.argv[1] == "--demo":
        data = "input-demo.txt"
    else:
        data = "input.txt"

    return "./"+dir+"/"+data

f = open(PuzzleFile())
stacks = [[], [], [], [], []]

for line in f:
    data = line
    llen = len(data)

    if data.count("[") > 0 and data.count("]") > 0:
        for i in range(0, llen, 4):
            t = data[i:i+4].strip()
            #print("["+t+"]")
            if len(t) > 0:
                stacks[int(i/4)].append(t)
    elif data.count("move") > 0:
        print("move")


print(stacks)