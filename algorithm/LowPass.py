alpha = 0.03

def lowPass(data):
    newData = [data[0]]
    for i in range(1, len(data)):
        newData.append(data[i] * alpha + newData[i - 1] *(1-alpha))
    return newData
