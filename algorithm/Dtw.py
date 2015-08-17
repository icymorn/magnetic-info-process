from dtw import dtw
from graph.Basic import MagneticLine

def dtwDistance(x, y):
    dis, cost, path = dtw(x, y)
    return dtw, path

def dtwExtend(x, path):
    return [x[i] for i in path[1]]

def test():
    # y = [i * 2 for i in x]
    x = [0, 0, 1, 1, 2, 4, 2, 1, 2, 0]
    y = [1, 1, 1, 2, 2, 2, 2, 3]
    # print x, y
    # dis, cost, path = dtw(x, y)
    # print dis, cost, path

    # x = [1,2,4,6,8,10,2]
    # y = [1,1,1,6,1,1,1]
    print x, y
    dis, cost, path = dtw(x, y)
    print cost, path
    y2 = [y[i] for i in path[1]]
    ml = MagneticLine()
    ml.addLine(x, 'x')
    ml.addLine(y, 'y1')
    ml.addLine(y2, 'y2')
    ml.show()