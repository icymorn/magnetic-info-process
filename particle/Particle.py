import math
from config.Config import config


class Particle:

    l = config.data['particle']['lambda']

    def __init__(self, pos):
        self.pos = pos
        self.weight = 1

    def updateWeight(self, fit):
        self.weight *= self.weight * math.exp(-Particle.l * fit)

    def getPos(self):
        return self.pos

    def setPos(self, pos):
        self.pos = pos

    def move(self, step):
        newPos = self.pos + step
        if newPos > 1 or newPos < 0:
            self.weight = 0
        self.pos = newPos

    def getWeight(self):
        return self.weight

    def setWeight(self, weight):
        self.weight = weight
