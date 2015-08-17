from config.Config import config
from data.DataLoader import DataLoader
from graph.basic import MagneticLine

if __name__ == '__main__':
    import numpy as np
    # import scipy.misc.imresize
    testdata = config.data['datafile']['test']
    dl = DataLoader()
    l = dl.read(testdata[0])
    l2 = dl.read(testdata[1])
    l3 = dl.read(testdata[2])
    ml = MagneticLine()
    l = np.array(l)
    # l1 = np.kron(l, [0.5, 0.5])
    # l2 = np.kron(l, [1, 1])
    # l3 = np.kron(l, [1.5, 1.5])

    # l2 = np.array(l2)
    # l2 = np.kron(l2, [1,2])
    ml.addLine(l, "a0")
    # ml.addLine(l1, "a1")
    ml.addLine(l2, "a2")
    ml.addLine(l3, "b1")
    ml.show()
