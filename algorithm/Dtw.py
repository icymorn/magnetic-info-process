from dtw import dtw
from graph.Basic import MagneticLine

def dtwDistance(x, y):
    dis, cost, path = dtw(x, y)
    return dis, path

def dtwExtend(x, path):
    arr1   = path[0]
    arr2   = path[1]
    last1  = -1
    last2  = -1
    result = []
    for i in xrange(len(arr1)):
        if arr1[i] > last1 and arr2[i] > last2:
            result.append(arr2[i])
        elif arr1[i] > last1:
            for j in xrange(arr1[i] - last1):
                result.append(arr2[i])
        elif arr2[i] > last2:
            pass
        last1 = arr1[i]
        last2 = arr2[i]
    return [x[i] for i in result]

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
