import zmq, json
def main():
    context = zmq.Context()
    publisher = context.socket(zmq.REQ)
    publisher.connect('ipc://filter')
    publisher.send(json.dumps({'data': [1,2,3,4], 'id': 1}))
    recv = publisher.recv()
    print json.loads(recv)
if __name__ == '__main__':
    main()
