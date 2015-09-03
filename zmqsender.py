import zmq, json
from data.DataLoader import DataLoader
from config.Config import config
import time
def main():
    loader = DataLoader()
    data = loader.read(config.data['datafile']['test'][0])
    context = zmq.Context()
    publisher = context.socket(zmq.REQ)
    publisher.connect('tcp://127.0.0.1:9988')

    index = 20
    path_particles_count = len(data)

    while True:
        currPos = float(index) / path_particles_count * 18.18
        publisher.send(json.dumps({'data': data[index-5:index], 'id': 1, 'currPos': currPos}))
        recv = publisher.recv()
        print json.loads(recv)
        time.sleep(0.5)
        index += 5
    
if __name__ == '__main__':
    main()
