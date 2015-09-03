import json
import pickle
import sys

def main():
    if len(sys.argv) != 2:
        print("need an input file")
        exit(1)
    with open(sys.argv[1], 'rb') as inputf:
        data = pickle.load(inputf)
        with open(sys.argv[1].split('.')[0] + '.json', 'wb') as output:
            json.dump(data, output)

    print "file saved."

if __name__ == '__main__':
    main()

