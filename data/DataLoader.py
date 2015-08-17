import pickle

class DataLoader:
    def __init__(self):
        pass

    def read(self, filename):
        data = pickle.load(open(filename, 'rb'))
        return data


def main():
    data = DataLoader()
    # print config.data
    print data.read("a1.data")

if __name__ == '__main__':
    main()
