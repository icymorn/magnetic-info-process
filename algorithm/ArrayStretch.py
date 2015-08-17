def BoxStretch(arr, toLength):
    arrLen = len(arr)
    ratio = 1.0 * toLength / arrLen
    return [arr[int(i / ratio)] for i in range(toLength)]

if __name__ == '__main__':
    print BoxStretch([1,2,3,4,5,6], 20)
