class Live:
    liveItems = []
    size = 0

    def __init__(self, fileName):
        file = open(fileName, 'r')

        line = file.readline().split()
        while line:
            tempArray = []
            for l in line:
                tempArray.append(int(l))
            self.liveItems.append(tempArray)
            line = file.readline().split()

        file.close()

        self.size = len(self.liveItems)

    def nextStat(self):
        newState = [[0 for x in range(self.size)] for y in range(self.size)]

        for i in range(0, self.size - 1):
            for j in range(0, self.size - 1):
                howMany = 0
                ##print(state[i][j],end=' ')

                for si in range(-1, 2):
                    for ri in range(-1, 2):
                        if i + si >= 0 and j + ri >= 0 and i + si < self.size and j + ri < self.size:
                            if self.liveItems[i + si][j + ri] == 1:
                                howMany += 1

                howMany -= self.liveItems[i][j]
                if howMany > 3 or howMany < 2:
                    newState[i][j] = 0
                elif howMany == 3:
                    newState[i][j] = 1
                else:
                    newState[i][j] = self.liveItems[i][j]

        self.liveItems = newState