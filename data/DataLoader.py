import pickle
import json

dataset = {}

class DataLoader:
    def __init__(self):
        pass

    def read(self, filename):
        data = dataset.get(filename)
        if data is None:
            if filename.endswith('.json'):
                data = json.load(open(filename, 'rb'))
            else:
                data = pickle.load(open(filename, 'rb'))
            dataset[filename] = data
        return data


def main():
    data = DataLoader()
    # print config.data
    print data.read("a0.data")
    print data.read("a0.data")

if __name__ == '__main__':
    main()
