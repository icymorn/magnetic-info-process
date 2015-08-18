from algorithm.Dtw import dtwDistance, dtwExtend, dtwShrink
from data.DataLoader import DataLoader
from config.Config import config
from graph.Basic import MagneticLine

if __name__ == '__main__':
    dl = DataLoader()
    data = config.data['datafile']['test']
    line1 = dl.read(data[0])
    line2 = dl.read(data[1])

    cost, path = dtwDistance(line1, line2)
    line3 = dtwExtend(line2, path)

    # line1 is longer than line2
    ml = MagneticLine()
    ml.addLine(line1)
    ml.addLine(line2)
    ml.addLine(line3)
    ml.show()

    line1, line2 = line2, line1
    # line2 is longer than line1
    cost, path = dtwDistance(line1, line2)
    line3 = dtwShrink(line2, path)
    ml2 = MagneticLine()
    ml2.addLine(line1)
    ml2.addLine(line2)
    ml2.addLine(line3)
    print len(line1), len(line3)
    ml2.show()
