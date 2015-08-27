import sys
import json
import pickle

def prepareData(filename, prefix = "a"):
    num = 0
    f = open(filename, 'r')
    data = []
    counter = 0
    while True:
        lines = f.readlines(1000)
        if len(lines) == 0:
            if counter > 0:
                save(prefix + str(num), data)
            return
        for line in lines:
            if line.startswith('No'):
                if counter > 0:
                    save(prefix + str(num), data)
                    num += 1
                    data = []
                    counter = 0
                else:
                    continue
                    # meet first line here
            else:
                if line != '\n':
                    if counter % 4 == 3:
                        data.append(float(line))
                    counter += 1

def save(name, data):
    with open(name + '.data', 'wb') as output:
        pickle.dump(data, output)
        print(name + '.data' + " : saved")

    with open(name + '.json', 'wb') as output:
        json.dump(data, output)
        print(name + '.json' + " : saved")

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Program needs two arguments for datafile name and output filename")
        exit(1)
    else:
        prepareData(sys.argv[1], sys.argv[2])
        print("prepare completed!")
