from config.Config import config
from data.DataLoader import DataLoader
from graph.Basic import MagneticLine
from scipy import ndimage
from algorithm.Dtw import dtwDistance, dtwExtend
import numpy as np


def testGraphing():
    testdata = config.data['datafile']['test']
    dl = DataLoader()
    l = dl.read(testdata[0])
    l2 = dl.read(testdata[1])
    l3 = dl.read(testdata[2])
    ml = MagneticLine()
    dist, path = dtwDistance(l, l2)
    lineData = dtwExtend(l2, path)

    print path
   # l = np.array(l)
    # l1 = np.kron(l, [0.5, 0.5])
    # l2 = np.kron(l, [1, 1])
    # l3 = np.kron(l, [1.5, 1.5])

    # l2 = np.array(l2)
    # l2 = np.kron(l2, [1,2])
    ml.addLine(l, "a0")
    # ml.addLine(l1, "a1")
    ml.addLine(l2, "a1")
    ml.addLine(lineData, "b0")
    ml.show()

if __name__ == '__main__':
    # testResizing()
    testGraphing()
