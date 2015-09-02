from config.Config import config
from data.DataLoader import DataLoader
from graph.Basic import MagneticLine
from scipy import ndimage
from algorithm.ArrayStretch import BoxStretch
import numpy as np

def testGraphing():
    # import scipy.misc.imresize
    testdata = config.data['datafile']['test']
    dl = DataLoader()
    l = dl.read(testdata[0])
    l2 = dl.read(testdata[1])
    l3 = dl.read(testdata[2])
    ml = MagneticLine()
    dist, path = dtwDistance(l, l2)
    lineData = dtwExtend(l2, path)

   # l = np.array(l)
    # l1 = np.kron(l, [0.5, 0.5])
    # l2 = np.kron(l, [1, 1])
    # l3 = np.kron(l, [1.5, 1.5])

    # l2 = np.array(l2)
    # l2 = np.kron(l2, [1,2])
    ml.addLine(l, "a0")
    # ml.addLine(l1, "a1")
    ml.addLine(l2, "a1")
    ml.addLine(lineData, "a1'")
    ml.show()

def testResizing():
    testdata = config.data['datafile']['test']
    dl = DataLoader()
    data = dl.read(testdata[0])
    print len(data)
    newdata = BoxStretch(data, 600)
    ml = MagneticLine()
    ml.addLine(data, "origin")
    ml.addLine(newdata, "newline")
    ml.show()

if __name__ == '__main__':
    # testResizing()
    testGraphing()
