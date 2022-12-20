def SolvePuzzle(input_file:str):
    cb1 = RopeBridge(9)
    cb1.cross(input_file)

    #cb2 = RopeBridge(9)
    #cb2.cross(input_file)

class RopeBridge:
    f = None
    hpos = {}
    tmoves = {}
    knots = []

    hx = 0
    hy = 0

    tx = 0
    ty = 0

    maxx = 0
    maxy = 0

    minx = 0
    miny = 0

    def __init__(self, knots_number:int):
        for i in range(knots_number):
            self.knots.append({
                "x": 0,
                "y": 0,
                "positions": []
            })
        pass

    def walk(self, direction:str, steps:int):
        for i in range(steps):
            callback = getattr(self, "step_" + direction)
            callback()
            #self.step(direction)

    def step_r(self):
        self.hx += 1
        print( "-> hr (", self.hx, ",", self.hy, ")")
        if(self.hx > self.maxx):
            self.maxx = self.hx
        self.tail_follow()

    def step_l(self):
        self.hx -= 1
        print( "-> hl (", self.hx, ",", self.hy, ")")
        if self.hx < self.minx:
            self.minx = self.hx
        self.tail_follow()

    def step_u(self):
        self.hy += 1
        print( "-> hu (", self.hx, ",", self.hy, ")")
        if(self.hy > self.maxy):
            self.maxy = self.hy
        self.tail_follow()

    def step_d(self):
        self.hy -= 1
        print( "-> hd (", self.hx, ",", self.hy, ")")
        if self.hy < self.miny:
            self.miny = self.hy
        self.tail_follow()

    def tail_follow(self):
        x1 = self.hx
        y1 = self.hy
        for i in range(0,len(self.knots)):
            k = self.tail_needs_to_move(x1, y1, i)
            x1 = int(k["x"])
            y1 = int(k["y"])
            
        

    def tail_needs_to_move(self, x:int, y:int, i:int):
        # head (x,y): (4,1) (4,1) (4,2)
        # tail (x,y): (3,0) (3,0) (4,1)

        hx = x
        hy = y
        
        tx = int(self.knots[i]["x"])
        ty = int(self.knots[i]["y"])

        #print( "--> (", i, ") ", x, y, tx, ty)

        if hx - tx == 1 and hy - ty == 2 or hx - tx == 2 and hy - ty == 1 or hx - tx == 2 and hy - ty == 2:
            '''
            4.....
            3.....
            2..hH.
            1.T...
            0.t...
             01234
            '''
            self.knots[i]["x"] += 1
            self.knots[i]["y"] += 1
            print("=> tru k=",i+1," (", self.knots[i]["x"], ",", self.knots[i]["y"], ")")
        elif hx - tx == -1 and hy - ty == 2 or hx - tx == -2 and hy - ty == 1 or hx - tx == -2 and hy - ty == 2:
            '''
            4.....
            3.....
            2.Hh..
            1...T.
            0...t.
             01234
            '''
            self.knots[i]["x"] -= 1
            self.knots[i]["y"] += 1
            print("=> tlu k=",i+1," (", self.knots[i]["x"], ",", self.knots[i]["y"], ")")
        elif hx - tx == 1 and hy - ty == -2 or hx - tx == 2 and hy - ty == -1 or hx - tx == 2 and hy - ty == -2:
            '''
            4.t...
            3.T...
            2..hH.
            1.....
            0.....
             01234
            '''
            self.knots[i]["x"] += 1
            self.knots[i]["y"] -= 1
            print("=> trd k=",i+1," (", self.knots[i]["x"], ",", self.knots[i]["y"], ")")
        elif hx - tx == -1 and hy - ty == -2 or hx - tx == -2 and hy - ty == -1 or hx - tx == -2 and hy - ty == -2:
            '''
            4...t.
            3.....
            2..h..
            1.....
            0.....
             01234
            '''
            self.knots[i]["x"] -= 1
            self.knots[i]["y"] -= 1
            print("=> tld k=",i+1," (", self.knots[i]["x"], ",", self.knots[i]["y"], ")")
        elif hx - tx == 2 and hy - ty == 0:
            self.knots[i]["x"] += 1
            print("=> tr k=",i+1," (", self.knots[i]["x"], ",", self.knots[i]["y"], ")")
        elif hx - tx == -2 and hy - ty == 0:
            self.knots[i]["x"] -= 1
            print("=> tl k=",i+1," (", self.knots[i]["x"], ",", self.knots[i]["y"], ")")
        elif hx - tx == 0 and hy - ty == 2:
            self.knots[i]["y"] += 1
            print("=> tu k=",i+1," (", self.knots[i]["x"], ",", self.knots[i]["y"], ")")
        elif hx - tx == 0 and hy - ty == -2:
            self.knots[i]["y"] -= 1
            print("=> td k=",i+1," (", self.knots[i]["x"], ",", self.knots[i]["y"], ")")
        else:
            print("=> idle k=",i+1," (", self.knots[i]["x"], ",", self.knots[i]["y"], ")")

        
        tpos = str(self.knots[i]["x"]) + "/" + str(self.knots[i]["y"])
        #self.tmoves.append(tpos)
        self.knots[i]["positions"].append(tpos)

        return self.knots[i]


    def cross(self, input_file:str):
        f = open(input_file)
        for line in f:
            data = line.strip().split(" ")
            self.walk(data[0].lower(), int(data[1]))

        l = len(self.knots)
        #print(self.knots[l-1]["positions"])

        uq = self.unique(self.knots[l-1]["positions"])
        print(len(uq))

    def unique(self, list1:list) -> list:
    
        # initialize a null list
        unique_list = []
    
        # traverse for all elements
        for x in list1:
            # check if exists in unique_list or not
            if x not in unique_list:
                unique_list.append(x)
        # print list
        return unique_list

    def print_pos(self):
        for y in range(self.maxy, self.miny, -1):
            for x in range(self.maxx, self.minx, -1):
                pos = str(y) + "/" + str(x)
                if pos in self.tmoves:
                    print("x", end="")
                else:
                    print(".", end="")
            print("")