import pickle
import json

class DataLoader:
    def __init__(self):
        pass

    def read(self, filename):
        if filename.endswith('.json'):
            data = json.load(open(filename, 'rb'))
        else:
            data = pickle.load(open(filename, 'rb'))
        return data


def main():
    data = DataLoader()
    # print config.data
    print data.read("out0.json")

if __name__ == '__main__':
    main()
