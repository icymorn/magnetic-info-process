from algorithm.Dtw import dtwSubsequence, dtwExtend, dtwDistance
from algorithm.ArrayStretch import BoxStretch
from data.DataLoader import DataLoader
from config.Config import config
from graph.Basic import MagneticLine
if __name__ == '__main__':
    dl = DataLoader()
    data = config.data['datafile']['test']
    line1 = dl.read(data[3])
    offset = 50
    size = 50
    sub = line1[offset:offset + size]
    dist, cost, path = dtwSubsequence(sub, line1)
    print dist
    print path
    start = path[1][0]
    ml = MagneticLine()
    ml.addLine(line1, "origin data")

    ml.addLine([0 for i in range(start)] + sub, "predict data")
    ml.addLine([0 for i in range(offset)] + sub, "sub data")
    ml.show()
