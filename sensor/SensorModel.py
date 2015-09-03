from data.DataLoader import DataLoader
from algorithm.Dtw import dtwCalculate, dtwExtend, dtwDistance
from config.Config import config
from algorithm.PassFilter import low_filter
class SensorModel:

    def __init__(self):
        self.lastSignal     = []
        self.currSignal     = None
        self.config         = config.data['sensor']
        self.lower          = self.config['lower']
        self.upper          = self.config['upper']
        self.locationPrefer = self.config['locationPrefer'] # best = 0 or avg = 1
        self.direction      = 1
        self.signalLength   = config.data['sensor']['bufferSize']
        self.lastDirection  = 1
        self.r              = 0.03

    def load(self, fileList):
        loader          = DataLoader()
        self.standard   = loader.read(fileList[0])
        self.sampleSize = len(self.standard)
        data            = []
        # extend all data to same length
        for dataFile in fileList:
            line       = loader.read(dataFile)
            dist, path = dtwDistance(self.standard, line)
            lineData   = dtwExtend(line, path)
            data.append(lineData)

        self.data = data

    def loadData(self, magneticData, direction = 1):
        self.standard   = magneticData[0]
        self.sampleSize = len(self.standard)
        data            = []
        for line in magneticData:
            diff, path = dtwDistance(self.standard, line)
            lineData   = dtwExtend(line, path)
            data.append(lineData)
        self.data = data

    def accept(self, signalArr, direction = 1):
    #print "get signal", signalArr
        if self.lastDirection == direction:
            if self.currSignal is None:
                self.currSignal = self.filter(signalArr)
            else:
                for i in signalArr:
                    self.currSignal.append(self.currSignal[-1] * (1-self.r) + self.r * i)
                self.currSignal = self.currSignal[-self.signalLength:]
        else:
            self.lastDirection = direction
            self.currSignal = self.filter(signalArr)
        if len(self.currSignal)  < self.signalLength:
            return False
        else:
            return True

    def filter(self, data):
        # return data
        newData = [data[0]]
        for i in range(1, len(data)):
            newData.append(data[i] * self.r + newData[i - 1] *(1-self.r))
        return newData

    def evaluate(self, p):
        if self.currSignal is None:
            print "please capture some data firstly."
            exit(1)
        currSignal1 = self.filter(self.currSignal)
        upperIndex = int(p * self.sampleSize)
        lowerIndex = upperIndex - len(self.currSignal)
        lowerIndex = 0 if lowerIndex < 0 else lowerIndex

        if self.locationPrefer == 1:
            totalDist = 0
            totalPos  = 0
            dataCount = len(self.data)
            for line in self.data:
                dist, pos = dtwCalculate(currSignal1, line[lowerIndex: upperIndex])
                totalDist += dist
                totalPos  += pos
            return totalDist / dataCount, totalPos / dataCount + lowerIndex
        else:
            bestDist = 999999999
            bestPos  = 0
            for line in self.data:
                dist, pos = dtwCalculate(currSignal1, line[lowerIndex: upperIndex])
                if dist < bestDist:
                    bestPos = pos
                    bestDist = dist
            return bestDist, 0
