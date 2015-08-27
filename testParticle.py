from particle.ParticleFactory import ParticleFactory
from config.Config import config
from data.DataLoader import DataLoader
import time
import bisect


# get sample data
loader = DataLoader()
data   = loader.read(config.data['datafile']['test'][1])

# init particle factory
pFactory = ParticleFactory(100, [config.data['datafile']['test'][1]])

realPos  = 0
size     = 5
dataSize = len(data)

while True:
    # get a slice of data
    recieve = data[realPos:realPos + size]
    pFactory.accept(recieve)
    step = len(recieve)
    pFactory.move(step)
    p2 = pFactory.getPredict()

    # robot real position change
    print "real:", float(realPos) / dataSize, "\tpre2:", p2, "\terr2:", abs(float(realPos) / dataSize - p2)
    pFactory.resample()
    time.sleep(1)

    realPos += size
    if realPos >= dataSize:
        break
