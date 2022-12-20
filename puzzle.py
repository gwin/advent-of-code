import sys
import importlib

def PuzzleFile():
    import sys

    dir = sys.argv[2]
    if len(sys.argv) > 3 and sys.argv[3] == "demo":
        data = "input-demo.txt"
    else:
        data = "input.txt"

    return "./puzzle-"+dir+"/"+data

def PuzzleCreate():
    import os
    pwd = os.path.dirname(os.path.realpath(__file__))
    dir = str(sys.argv[2])

    if not dir.isdigit():
        print("The directory name can contain digits only!")
        return
    elif len(dir) != 3:
        print("The directory name needs to be exactly 3 digit long!")
        return

    mkd = pwd + "/puzzle-" + dir
    

    if not os.path.isdir(mkd):
        os.mkdir(mkd)
        print("Created Puzzle: ")
        print(mkd)

        open(mkd+"/input-demo.txt", "w").close()
        print(" - input-demo.txt")
        open(mkd+"/input.txt", "w").close()
        print(" - input.txt")

        f = open(mkd+"/main.py", "w")
        f.write("def SolvePuzzle(input_file:str):\n")
        f.write("    pass\n")
        f.close()

        print(" - main.py")
    else:
        print("Directory [", mkd, "] already exists.")



'''
python puzzle.py run 009 demo
python puzzle.py run 009
python puzzle.py create 009
'''

print_instructions = False


if len(sys.argv) < 2:
    print("You need to pass at least two arguments!")
    print_instructions = True
elif sys.argv[1] not in ("create", "run", "help"):
    print("First argument should be one of 'create', 'run' or 'help'!", end=" ")
    print("[", sys.argv[1], "] given")
    print_instructions = True
elif sys.argv[1] == "help":
    print_instructions = True
elif sys.argv[1] == "run":
    Puzzle = importlib.import_module("puzzle-" + sys.argv[2] + ".main")
    if not callable(getattr(Puzzle, "SolvePuzzle")):
        print("This puzzle needs to be run directly.")
    else:
        Puzzle.SolvePuzzle(PuzzleFile())
elif sys.argv[1] == "create":
    PuzzleCreate()

if print_instructions:
    print("Usage Examples:")
    print("puzzle.py run XXX demo - run puzzle XXX with demo data")
    print("puzzle.py run XXX - run puzzle XXX with production data")
    print("puzzle.py create XXX - create folder and files for XXX puzzle") 



