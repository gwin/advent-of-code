f = open('./puzzle-002-input.txt')

def Points(a, b):
    # X-rock; Y-papper; Z-scisors
    t = {
        # Rock
        "A": { "X":3, "Y":6, "Z":0 },
        # Papper
        "B": { "X":0, "Y":3, "Z":6 },
        # Scissors
        "C": { "X":6, "Y":0, "Z":3 }
    }
    scores = {
        "X": 1,
        "Y": 2,
        "Z": 3
    }
    
    return scores[b] + t[a][b]

def Points2(a,b):
    # X-loose; Y-draw  ; Z-win
    # X-rock ; Y-papper; Z-scisors
    t = {
        # Rock
        "A": { "X":"Z", "Y":"X", "Z":"Y" },
        # Papper
        "B": { "X":"X", "Y":"Y", "Z":"Z" },
        # Scissors
        "C": { "X":"Y", "Y":"Z", "Z":"X" }
    }
    return Points(a, t[a][b])

score1 = 0
score2 = 0

for line in f:
    ab = line.strip().split(" ")
    score1 += Points(ab[0],ab[1])
    score2 += Points2(ab[0],ab[1])


print("Part #1 ", score1)
print("Part #2 ", score2)

