from data.DataLoader import DataLoader
from algorithm.Dtw import dtwCalculate, dtwExtend, dtwDistance
from config.Config import config

class ParticleFilter:

    def __init__(self):
        self.lastSignal = []
        self.currSignal = None
        self.config = config.data['filter']
        self.lower = self.config['lower']
        self.upper = self.config['upper']
        self.locationPrefer = self.config['locationPrefer'] # best=0 or avg=1

    def load(self, fileList):
        loader = DataLoader()
        self.standard = loader.read(fileList[0])
        self.standardLength = len(self.standard)
        data = []
        # extend all data to same length
        for dataFile in fileList:
            line = loader.read(dataFile)
            dist, path = dtwDistance(self.standard, line)
            lineData = dtwExtend(line, path)
            data.append(lineData)

        self.data = data

    def capture(self, signalArr):
        self.currSignal = self.lastSignal + signalArr
        self.lastSignal = signalArr

    def filter(self, p):
        if self.currSignal is None:
            print "please capture some data firstly."
            exit(1)

        lower = 0 if p - self.lower < 0 else p - self.lower
        upper = 1 if p - self.upper > 1 else p + self.upper
        lowerIndex = int(self.standardLength * lower)
        upperIndex = int(self.standardLength * upper)
        if self.locationPrefer == 1:
            totalDist = 0
            totalPos  = 0
            dataCount = len(self.data)
            for line in self.data:
                dist, pos = dtwCalculate(self.currSignal, line[lowerIndex: upperIndex])
                totalDist += dist
                totalPos  += pos
            return totalDist / dataCount, totalPos / dataCount + lowerIndex
        else:
            bestDist = 999999999
            bestPos  = 0
            for line in self.data:
                dist, pos = dtwCalculate(self.currSignal, line[lowerIndex: upperIndex])
                if dist < bestDist:
                    bestPos = pos
                    bestDist = dist
            return bestDist, float(bestPos + lowerIndex) / self.standardLength
