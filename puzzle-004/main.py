def PuzzleFile():
    import sys

    dir = sys.argv[0].split("/")[1]
    if len(sys.argv) > 1 and sys.argv[1] == "--demo":
        data = "input-demo.txt"
    else:
        data = "input.txt"

    return "./"+dir+"/"+data

f = open(PuzzleFile())

def SectionContains(s1:str,s2:str):
    s1a = s1.split("-")
    s2a = s2.split("-")

    aMin = int(s1a[0])
    aMax = int(s1a[1])

    bMin = int(s2a[0])
    bMax = int(s2a[1])

    #print(aMin,aMax,bMin,bMax)

    # a contains b?
    if aMin <= bMin and aMax >= bMax:
        return True
    elif bMin <= aMin and bMax >= aMax:
        return True
    else:
        return False

def SectionOverlaps(s1:str,s2:str):
    s1a = s1.split("-")
    s2a = s2.split("-")

    aMin = int(s1a[0])
    aMax = int(s1a[1])

    bMin = int(s2a[0])
    bMax = int(s2a[1])

    aList = []
    bList = []

    for i in range(aMin, aMax+1):
        aList.append(i)

    for i in range(bMin, bMax+1):
        bList.append(i)


    intersec = list(set(aList).intersection(bList))

    if len(intersec) > 0:
        return True
    else: 
        return False
    


contains = 0
overlaps = 0

for line in f:
    data = line.strip().split(",")
    if SectionContains(data[0],data[1]) == True:
        contains = contains + 1
    if SectionOverlaps(data[0],data[1]) == True:
        overlaps = overlaps + 1


print(contains)
print(overlaps)
