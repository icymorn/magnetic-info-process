import mlpy

def dtwDistance(x, y):
    dis, cost, path = mlpy.dtw_std(x, y, dist_only = False)
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
            result.append(arr2[i])
        elif arr2[i] > last2:
            pass
        last1 = arr1[i]
        last2 = arr2[i]
    return [x[i] for i in result]

def dtwCalculate(x, y):
    dist, cost, path = mlpy.dtw_subsequence(x, y)
    path = path[1]
    return dist, path[len(path) - 1]

def dtwSubsequence(x, y):
    return mlpy.dtw_subsequence(x, y)

