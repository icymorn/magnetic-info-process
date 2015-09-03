from particle.ParticleFilter import ParticleFilter
from config.Config import config
import zmq
from data.MapLoader import loadRouteFromMap
generators = {}

mapDirectory = '/home/moe/PycharmProjects/dingge/app/map/'
context = zmq.Context()
socket = context.socket(zmq.PUB)
socket.bind("tcp://*:9955")

def particleFilterCo(pathLength, magneticData):
     particleFilter = ParticleFilter(pathLength, magneticData)

     while True:
        # get a slice of data
        sensorData, x_simulate = yield
        isBelievable           = particleFilter.accept(sensorData)
        x_predict              = particleFilter.getPredict(isBelievable)
        if x_simulate is not None:
            print 'error: %f' %(x_predict - x_simulate)
            socket.send_pyobj({'x_predict': x_predict, 'x_simulate': x_simulate, 'poss': [p.pos for p in particleFilter.particles],
                'weights': [p.w for p in particleFilter.particles]})
        else:
            socket.send_pyobj({'x_predict': x_predict, 'x_simulate': 0.0, 'poss': [p.pos for p in particleFilter.particles],
                'weights': [p.w for p in particleFilter.particles]})
        yield x_predict

def main():
    context = zmq.Context()
    subscriber = context.socket(zmq.REP)
    subscriber.bind('tcp://127.0.0.1:9988')
    while True:
        data       = subscriber.recv_pyobj()
        robotId    = data['id']
        x_simulate = data.get('currPos')
        gen        = generators.get(robotId)
        if gen is None or data.get('route') != '':
            route               = data.get('route')
            mapData             = loadRouteFromMap(mapDirectory +  data.get('map') + '.json', route, data['direction'])
            gen                 = particleFilterCo(mapData['distance'], mapData['fingerdata'])
            generators[robotId] = gen

        gen.next()
        ret = gen.send((data['data'], x_simulate))
        subscriber.send_pyobj({'pos':ret})

if __name__ == "__main__":
    main()

