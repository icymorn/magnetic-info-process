import pickle
import socket
import threading
import time
from config.Config import config

class DataLoader:
    def __init__(self):
        pass

    def read(self, filename):
        data = pickle.load(open(filename, 'rb'))
        return data

    def datasource(self):
        packer = DataPacker()
        packer.start()
        return packer

class DataPacker(threading.Thread):

    def __init__(self):
        super(DataPacker, self).__init__()
        self.running = True
        self.setDaemon(True)
        self.dataCache = []
        self.lastTime = 0
        self.lastProcessTime = 0

    def listen(self):
        while True:
            msg, client = self.socket.recvfrom(1024)
            left = msg.index('[')
            self.dataCache = [float(num) for num in msg[left:-1].split(',')]
            self.lastTime = time.time()


    def run(self):
        reciever = config.data['network']['server']
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        address = (reciever['ip'], reciever['port'])
        self.socket.bind(address)
        while True:
            msg, client = self.socket.recvfrom(1024)
            left = msg.index('[')
            self.dataCache = eval(msg[left:])
            self.lastTime = time.time()

    def hasUpdate(self):
        return self.lastTime > self.lastProcessTime

    def capture(self):
        tryTime = 0
        while tryTime < 100:
            if self.hasUpdate():
                self.lastProcessTime = time.time()
                return self.dataCache
            time.sleep(0.1)
            tryTime += 1

        print "Waiting too long for data. Exit now."
        exit(1)

def main():
    data = DataLoader()
    # print config.data
    print data.read("a1.data")

if __name__ == '__main__':
    main()
