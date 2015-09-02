import zmq, json
from data.DataLoader import DataLoader
from config.Config import config
def main():
    loader = DataLoader()
    data = loader.read(config.data['datafile']['test'][0])
    context = zmq.Context()
    publisher = context.socket(zmq.REQ)
    publisher.connect('tcp://127.0.0.1:9988')

    publisher.send(json.dumps({'data': data[10:15], 'id': 1}))
    recv = publisher.recv()

    print json.loads(recv)
if __name__ == '__main__':
    main()
