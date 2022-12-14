def PuzzleFile():
    import sys

    dir = sys.argv[0].split("/")[1]
    if len(sys.argv) > 1 and sys.argv[1] == "--demo":
        data = "input-demo.txt"
    else:
        data = "input.txt"

    return "./"+dir+"/"+data

f = open(PuzzleFile())

def GetSignal(data:str="", signature:int=4) -> int:
    signal_length = len(data)
    signal_index = 0
    for i in range(0, signal_length):
        signal = data[i:i+signature]
        a = {}
        for s in signal:
            a[s] = 1
        
        if len(a) == signature:
            signal_index = i+signature
            break

    return signal_index

for line in f:
    data = line.strip()
    print("Signal #1", GetSignal(data, 4))
    print("Signal #2", GetSignal(data, 14))

        

 