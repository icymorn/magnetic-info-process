from algorithm.Dtw import dtwDistance, dtwExtend, dtwSubsequence
from algorithm.ArrayStretch import BoxStretch
from data.DataLoader import DataLoader
from config.Config import config
from graph.Basic import MagneticLine
import random
if __name__ == '__main__':
    dl = DataLoader()
    data = config.data['datafile']['test']
    line1 = dl.read(data[3])
    line2 = dl.read(data[5])
    # line1 = [0,0,0,0,0,1,0,0,0]
    # line2 = [0,0,3,3,3,0,0]
    offset  = 150
    size    = 10
    sub     = line2[offset:offset + size]
    sub_bak = sub[:]
    noise   = []

    for i in range(size):
        n = random.randint(-1, 1) * 0
        sub[i] += n
        noise.append(n)
    dist, cost, path = dtwSubsequence(sub, line1)

    start = path[1][0]
    print "dist", dist
    print "path", path[1]
    print "noise", noise
    # cost, path = dtwDistance(line1, line2)
    # line3 = dtwExtend(sub, path)
    # line1 is longer than line2
    ml = MagneticLine()
    ml.addLine(line1, "origin data")

    ml.addLine([0 for i in range(start)] + sub, "predict data")
    ml.addLine([0 for i in range(offset)] + sub_bak, "sub data")
    # ml.addLine(line2)
    # ml.addLine(line3, "extended line")
    ml.show()

    # line1, line2 = line2, line1
    # # line2 is longer than line1
    # cost, path = dtwDistance(line1, line2)
    # line3 = dtwExtend(line2, path)
    # ml2 = MagneticLine()
    # ml2.addLine(line1)
    # ml2.addLine(line2)
    # ml2.addLine(line3)
    # ml2.show()
