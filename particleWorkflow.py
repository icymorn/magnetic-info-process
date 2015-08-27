from particle.ParticleFactory import ParticleFactory
from config.Config import config
import zmq, json

generators = {}

def particleFilter():
    pFactory = ParticleFactory(400, [config.data['datafile']['test'][1]])

    while True:
        # get a slice of data
        recieve = yield
        pFactory.accept(recieve)
        step = len(recieve)
        pFactory.move(step)
        yield pFactory.getPredict()

        pFactory.resample()

def main():
    context = zmq.Context()
    subscriber = context.socket(zmq.REP)
    subscriber.bind('tcp://127.0.0.1:9988')
    while True:
        rec = subscriber.recv()
        data = json.loads(rec)
        robotId = data['id']
        gen = generators.get(robotId)
        if gen is None:
            gen = particleFilter()
            generators[robotId] = gen

        gen.next()
        ret = gen.send(data['data'])
        subscriber.send(json.dumps({'pos':ret}))

if __name__ == "__main__":
    main()

