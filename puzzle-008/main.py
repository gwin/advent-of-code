def PuzzleFile():
    import sys

    dir = sys.argv[0].split("/")[1]
    if len(sys.argv) > 1 and sys.argv[1] == "--demo":
        data = "input-demo.txt"
    else:
        data = "input.txt"

    return "./"+dir+"/"+data

class Forest:
    scenic_rank = []
    forest = []

    max_x = 0
    max_y = 0

    visible = 0

    def PlantTrees(self) -> list:
        f = open(PuzzleFile())
        for line in f:
            data = line.strip()
            forest_row = []
            for tree in data:
                forest_row.append(int(tree))
            self.forest.append(forest_row)

        self.max_x = len(self.forest)
        self.max_y = len(self.forest[0])

        return forest

    def _IsEdgeTree(self, i:int, j:int) -> bool:
        if i == 0 or j == 0 or i == self.max_x-1 or j == self.max_y-1:
            return True
        else:
            return False

    def _IsTreeVisible(self, i:int, j:int) -> bool:
        if(self._IsEdgeTree(i,j)):
            return True
        #return False
        tree = self.forest[i][j]
        print("[",i,"][",j,"] ->", tree)

        # check x-left
        IsVisible = True
        for x in range(0, j):
            print("x-l ", tree, "<=", self.forest[i][x])
            if tree <= self.forest[i][x]:
                IsVisible = False
                break
        if IsVisible:
            print("[visible]")
            return True

        # check x-right
        IsVisible = True
        for x in range(j+1, self.max_x):
            print("x-r ", tree, "<=", self.forest[i][x])
            if tree <= self.forest[i][x]:
                IsVisible = False
        if IsVisible:
            print("[visible]")
            return True

        # check y-top
        IsVisible = True
        for y in range(0, i):
            print("y-t ", tree, "<=", self.forest[y][j])
            if tree <= self.forest[y][j]:
                IsVisible = False
        if IsVisible:
            print("[visible]")
            return True

        # check y-bottom
        IsVisible = True
        for y in range(i+1, self.max_y):
            print("y-b ", tree, "<=", self.forest[y][j])
            if tree <= self.forest[y][j]:
                IsVisible = False
        if IsVisible:
            print("[visible]")
            return True

        return False

    def CheckTreeVisibility(self, i:int, j:int):
        self._IsTreeVisible(i,j)

    def GetVisibleTrees(self) -> int:
        visible = 0
        for i in range(self.max_x):
            for j in range(self.max_y):
                if self._IsEdgeTree(i,j):
                    visible += 1
                elif self._IsTreeVisible(i,j):
                    visible += 1
                # endif
            # endfor
        # endfor
        return visible

    def GetScenicRanks(self) -> list:
        return self.scenic_rank

    def GetTreeScenicRank(self, i:int, j:int) -> list:
        r = [0, 0, 0, 0, 1]
        tree = self.forest[i][j]

        #print("-> ", j-1, self.max_y)

        for x in range(j-1, -1, -1):
            #print("->",self.forest[i][x])
            r[0] += 1
            if tree <= self.forest[i][x]:
                break


        for x in range(j+1, self.max_y):
            #print("->",self.forest[i][x])
            r[1] +=1
            if tree <= self.forest[i][x]:
                break

        for x in range(i-1, -1, -1):
            #print("->",self.forest[i][x])
            r[2] += 1
            if tree <= self.forest[x][j]:
                break

        for x in range(i+1, self.max_x):
            #print("->",self.forest[i][x])
            r[3] +=1
            if tree <= self.forest[x][j]:
                break

        r[4] = r[0] * r[1] * r[2] * r[3]

        return r


    def RankByScenicView(self):
        self.scenic_rank = []
        for i in range(self.max_x):
            self.scenic_rank.append([])
            for j in range(self.max_y):
                self.scenic_rank[i].append(self.GetTreeScenicRank(i,j))
            # endfor
        # endfor

    def GetHighestScenicRank(self):
        if not self.scenic_rank:
            self.RankByScenicView()

        highest_rank = 0
        for rank_row in self.scenic_rank:
            for rank in rank_row:
                if rank[4] > highest_rank:
                    highest_rank = rank[4]
                # endif
            # endfor
        # endfor

        return highest_rank


forest = Forest()
forest.PlantTrees()

#forest.CheckTreeVisibility(2,3)
#print(forest.GetTreeScenicRank(1,2))
#print(forest.GetTreeScenicRank(3,2))

forest.RankByScenicView()
#print(forest.scenic_rank)

print(forest.GetHighestScenicRank())