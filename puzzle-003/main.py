def SolvePuzzle(input_file:str):
    f = open(input_file) 
    total = 0
    total2 = 0

    j = 0
    buffer = []

    for line in f:
        data = line.strip()
        c = FindItemPriority(data)
        pos = CharToInt(c)
        total += pos
        #print(c, "/", pos)

        buffer.append(data)
        j = j+1

        if j % 3 == 0:
            total2 = total2 + FindBadge(buffer)
            buffer = []
            j = 0
        else:
            pass


    print(total)
    print(total2)


def FindItemPriority(data: str): 
    length = int(len(data)/2)

    p1 = data[0:length]
    p2 = data[length:]

    for i in range(length):
        c = p1[i:(i+1)]
        if p2.count(c) > 0:
            return c

def CharToInt(char: str):
    import string
    all = string.ascii_lowercase + string.ascii_uppercase
    length = len(all)

    for i in range(length):
        if char == all[i:(i+1)]:
            return i+1

def CompartmentHasBoth(f:str, b:str, c:str):
    if b.count(f) and c.count(f):
        return True
    else:
        return False



def FindBadge(ruck: list):
    a = str(ruck[0])
    b = str(ruck[1])
    c = str(ruck[2])
    
    alen = len(a)
    #print(ruck)
    #print(alen)
    for ch in range(alen):
        chx = a[ch:ch+1]
        if CompartmentHasBoth(chx, b, c):
            return CharToInt(chx)



