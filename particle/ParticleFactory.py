from particle.Particle import Particle
from sensor.ParticleFilter import ParticleFilter
from config.Config import config
import bisect
import random


class ParticleFactory:

    def __init__(self, length = 10, fileList = None):
        particle = []
        for i in xrange(length):
            particle.append(Particle(float(i) / length))
        self.particle = particle
        self.length = length
        self.pFilter = ParticleFilter()
        if fileList is None:
            self.pFilter.load(config.data['datafile']['test'])
        else:
            self.pFilter.load(fileList)
        self.setFitCalculator(fitCalculus)

    def accept(self, data, direction = 1):
        self.pFilter.accept(data, direction)

    def move(self, step):
        ratio = float(step) / self.pFilter.standardLength
        totallWeight = 0.0
        for p in self.particle:
            p.move(ratio)
            self._fitCalculus(p, self.pFilter.eval(p.getPos()))
            weight = p.getWeight()
            totallWeight += weight

        # normalize
        if totallWeight > 0.0:
            for p in self.particle:
                p.setWeight(p.getWeight() / totallWeight)

    def setFitCalculator(self, func):
        self._fitCalculus = func

    def getActiveParticle(self):
        return [p for p in self.particle if p.getWeight() > 0.0]

    def getBest(self):
        bestP = self.particle[0]
        best = bestP.getWeight()
        for p in self.particle:
            if p.getWeight() > best:
                best = p.getWeight()
                bestP = p
        return bestP

    def getPredict(self):
        total = 0.0
        for p in self.particle:
            total += p.getWeight() * p.getPos()
        return total

    def resample(self):
        accum = 0.0
        state = self.getActiveParticle()
        distribution = []

        for x in state:
            accum += x.getWeight()
            distribution.append(accum)

        newParticle = []

        for _ in self.particle:
            newParticle.append(Particle(state[bisect.bisect_left(distribution, random.uniform(0, 1))].getPos()))

        self.particle = newParticle

def fitCalculus(particle, filterData):
    diff, pos = filterData
    particle.updateWeight(diff + abs(pos - particle.getPos()))
