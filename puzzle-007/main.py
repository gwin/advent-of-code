def PuzzleFile():
    import sys

    dir = sys.argv[0].split("/")[1]
    if len(sys.argv) > 1 and sys.argv[1] == "--demo":
        data = "input-demo.txt"
    else:
        data = "input.txt"

    return "./"+dir+"/"+data

f = open(PuzzleFile())
root = {}

class FolderBrowser:

    comm = []

    root = {
        "/root": []
    }

    cursor = ""

    position = 0

    def set_input(self, commands):
        self.comm = commands

    def run_line(self, line:str):
        #print("[",line,"]")
        parts = line.split(" ")
        if parts[0] == "$":
            self.run_command(line)
        elif parts[0] == "dir":
            path = self.cursor + "/" + parts[1]
            self.root[path] = []
        else:
            file = {
                "name": parts[1],
                "size": parts[0] 
            }
            self.root[self.cursor].append(file)

    def run_command(self, line:str):
        data = line.split(" ")
        
        if data[1] == "cd":
            self.run_cd(data[2])
        elif data[1] == "ls":
            self.run_ls()

    def run_cd(self, path:str):
        if path == "/":
            self.cursor = "/root"
        elif path == "..":
            c = self.cursor.split("/")
            c.pop()
            s = "/"
            self.cursor = s.join(c)
        else:
            self.cursor = self.cursor + "/" + path

        #print(self.cursor)

    def run_ls(self):
        return


    def run(self):
        
        for line in self.comm:
            self.position += 1
            data = line.strip()
            self.run_line(data)

        self.root = dict(sorted(self.root.items())) 

    def get_cursor(self) -> list:
        return self.cursor

    def get_root(self) -> dict:
        return self.root

    def get_root_pretty(self, path:dict=None):
        if path == None:
            path = self.root

        for folder in path:
            parts = folder.replace("/root", "").split("/")
            tab = len(parts)

            if len(parts) > 0:
                directory = parts.pop()
            else:
                directory = ""

            for i in range(tab):
                print(" ", end="")

            print("-", directory)
            
            for file in path[folder]:
                for i in range(tab):
                    print(" ", end="")

                print("-", file["name"], "   ", file["size"],"b")

class FolderSize:
    folder = {}

    struct = {}

    def set_structure(self, struct:dict):
        self.struct = struct

    def compute_all(self):
        for folder in self.struct:
            self.folder[folder] = self.compute(folder)

    def compute(self, path:str) -> int:
        #print(path)
        sum = 0
        for line in self.struct:
            line = str(line)
            if line.startswith(path):
                sum += self.sum_folder(self.struct[line])
            # endif
        # endfor
        return sum

    def sum_folder(self, files:dict) -> int:
        sum = 0
        for file in files:
            sum += int(file["size"])
        return sum

    def print_folders(self):
        for folder in self.folder:
            print(folder, "size: ", self.folder[folder])

    def get_folders(self) -> dict:
        return self.folder 


fb = FolderBrowser()
fb.set_input(f)
fb.run()

fs = FolderSize()
fs.set_structure(fb.get_root())
fs.compute_all()
fs.print_folders()

# Part 1
total_size = 0
folders = fs.get_folders()
for f in folders:
    if folders[f] <= 100000:
        total_size += folders[f]

print("Total size: ", total_size)

# Part 2
disk_size = 70000000
disk_used = folders["/root"]
disk_reqd = 30000000

disk_need = disk_reqd + disk_used - disk_size
can_delete = []

print("Need", disk_need)

for f in folders:
    if folders[f] >= disk_need:
        can_delete.append(folders[f])

can_delete.sort()

print(can_delete[0])