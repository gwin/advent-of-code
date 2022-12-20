def SolvePuzzle(input_file:str):
    sr = SignalReader()
    sr.run(input_file)

class SignalReader:

    cycles = []
    buffer = {}

    x = 1
    signal_total = 0

    def run(self, input_file:str):
        f = open(input_file)
        i = 0

        for line in f:

            data = line.strip()

            #print(i, ": ", data)

            if data != "noop":
                i+=2
                split = data.split(" ")
                self.buffer[str(i)] = int(split[1])
            else:
                i+=1


        self.x = 1
        self.signal_total = 0

        for j in range(0,i+2):
            if str(j) in self.buffer:
                self.x += self.buffer[str(j)]
                print(j+1, ": ", self.x, " -> ", self.buffer[str(j)])
            else:
                print(j+1, ": ", self.x)

            if self.is_signal(j+1):
                print("")
                print(j+1, "*", self.x, "=", (j+1)*self.x)
                self.signal_total += (j+1)*self.x

        print(self.signal_total)
            

    def is_signal(self, j:int) -> bool:
        x = 0
        while x < j:
            if x*40 + 20 == j:
                return True
            else:
                x += 1

        return False
            
            

        # endfor

        print("")
        print(self.buffer)
        print(self.cycles)


