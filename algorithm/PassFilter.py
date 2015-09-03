r = 0.03
a = 0.999

def low_filter(x):
    y = [x[0]]
    for i in range(1, len(x)):
        y.append(x[i] * r + y[i - 1] * (1-r))
    return y

def low_filter_part(x,start,end):
    y = [x[0]]
    for i in range(1, len(x)):
        if i > start and i < end :
            y.append(x[i] * r + y[i - 1] * (1-r))
        else:
            if i == start:
                y.append(x[i])
            else:
                y.append(0.0)
    return y

def high_filter(x):
    y = [0.0]
    for i in range(1, len(x)):
        y.append(a*(y[i-1]  + x[i] - x[i-1]))
    return y

def high_filter_short(x, sample, pos):
    length = len(x)
    if pos - length > 0:
        y = [sample[pos - length]]
    else:
        y = [sample[0]]
    for i in range(1, length):
        y.append(a * (y[i - 1]  + x[i] - x[i - 1]))
    return y

def main():
    print high_filter_short([1,2,3,4], [2,3,4,5,6,4,3,3,54,6,7,3], 7)

if __name__ == '__main__':
    main()
