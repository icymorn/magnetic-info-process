# ------------------------------------------------------------------------
# coding=utf-8
# ------------------------------------------------------------------------
#
#  Created by Jason Wu on 2015-08-29
#
# ------------------------------------------------------------------------

import math
import bisect
import random
from scipy.stats import norm
from particle.Particle import Particle
from motion.MotionModel import MotionModel
from sensor.SensorModel import SensorModel
from config.Config import config

# ------------------------------------------------------------------------
#some global parameters
LAMBDA = config.data['particle']['lambda']
SPPED = config.data['particle']['speed'];            # particle move speed (m)
RESAMPLE_UNIFORM_PERCENT = config.data['particle']['resample_uniform_percent']
RESAMPLE_AROUND_MAX_PERCENT = config.data['particle']['resample_around_max_percent']
RESAMPLE_AROUND_MAX_STANDARD_DEVIATION = config.data['particle']['resample_around_max_standard_deviation']

# ------------------------------------------------------------------------
class WeightedDistribution(object):
    def __init__(self, state):
        accum = 0.0
        self.state = [p for p in state if p.w > 0.0]
        self.distribution = []
        for x in self.state:
            accum += x.w
            self.distribution.append(accum)

    def pick(self):
        try:
            return self.state[bisect.bisect_left(self.distribution, random.uniform(0, 1))]
        except IndexError:
            # Happens when all particles are improbable w=0.0
            return None

# ------------------------------------------------------------------------
class ParticleFilter:

    def __init__(self, length, dataList = None):
        self.motionModel = MotionModel()
        self.sensorModel = SensorModel()
        self.sensorModel.loadData(dataList)
        self._path_data_count = self.sensorModel.sampleSize
        self._x_max = 0.0
        self._x_center = 0.0
        self._particles_count = 100
        self._path_length = length
        self.initSample(2, 10.8)

    @property
    def particles(self):
        return self._particles

    @property
    def x_max(self):
        return self._x_max

    @property
    def x_center(self):
        return self._x_center

    @property
    def path_length(self):
        return self._path_length

    def accept(self, data, direction = 1):
        isBelievable = self.sensorModel.accept(data, direction)
        return isBelievable

    def updateParticles(self, step, isBelievable):
        for p in self._particles:
            # update motion model
            p.pos = self.motionModel.update(p.pos, step, isBelievable)
            # update sensor model
            if isBelievable:
                diff, pos = self.sensorModel.evaluate(p.pos / self._path_length)
                fit = diff #+ 40*abs(pos-p.x/path_length)
                p.w *= math.exp(-LAMBDA*fit)

    # compute x_max, x_center
    def computePositions(self):
        #compute x where w max
        p_w_max = self._particles[0]
        for p in self._particles:
            if p.w >= p_w_max.w:
                p_w_max = p
        self._x_max = p_w_max.pos

        nu = sum(p.w for p in self._particles)
        if nu != 0.0 :
            self._x_center = sum(p.w / nu * p.pos for p in self._particles)
        else:
            self._x_center = 0.0

    # Normalize weights
    def normalizeWeights(self):
        nu = sum(p.w for p in self._particles)
        if nu:
            for p in self._particles:
                p.w = p.w / nu

    # Initialise particles. (mode=0:random, mode=1:uniform)
    def initSample(self, mode=1, nearPos = 0.0):
        uniform_weight = 1.0/self._particles_count
        self._particles = []
        self._iter = 0
        if mode == 0 : # random
            self._particles = Particle.create_random_particles(self._particles_count, uniform_weight)
        elif mode == 1: # uniform
            self._particles = Particle.create_uniform_particles(self._particles_count, uniform_weight)
        elif mode == 2: # near
            for _ in range(0, self._particles_count):
                pos = norm.rvs(nearPos, RESAMPLE_AROUND_MAX_STANDARD_DEVIATION*3)
                if pos < 0.0 or pos > self._path_length :
                     pos = nearPos
                new_particle = Particle(pos, uniform_weight)
                self._particles.append(new_particle)

    # Resample particles.
    def resampleParticles(self, uniform_percent=RESAMPLE_UNIFORM_PERCENT):
        # create a weighted distribution, for fast picking
        dist = WeightedDistribution(self._particles)
        uniform_weight = 1.0 / self._particles_count
        u_count = (int)(self._particles_count * uniform_percent * math.exp(-0.2*self._iter)) # uniform count
        self._iter += 1
        max_around_count = (int)(self._particles_count * RESAMPLE_AROUND_MAX_PERCENT) # max around count
        pick_count =self._particles_count - u_count - max_around_count # pick count from exist particles

        # uniform
        new_particles = self.create_uniform_particles(u_count, uniform_weight)

        # max around
        for i in xrange(0,max_around_count):
            new_particle = Particle(norm.rvs(self._x_max, RESAMPLE_AROUND_MAX_STANDARD_DEVIATION), uniform_weight)
            new_particles.append(new_particle)

        # pick from exist particles
        for i in xrange(0,pick_count):
            p = dist.pick()
            if p is None:  # No pick b/c all totally improbable
                new_particle = Particle(random.uniform(0,1) * self._path_length, uniform_weight)
            else:
                new_particle = Particle(p.pos, p.w)
            new_particles.append(new_particle)

        self._particles = new_particles

    # If isBelievable is Fasle, only move particles, not update weights or resample
    def getPredict(self, isBelievable):
        self.updateParticles(SPPED, isBelievable)
        self.computePositions()
        if isBelievable:
            self.normalizeWeights()
            self.resampleParticles()
        return self._x_max

    def create_random_particles(self, particles_num, w):
        return [Particle( random.uniform(0, 1) * self._path_length, w) for _ in xrange(0, particles_num)]

    def create_uniform_particles(self, particles_num, w):
        return [Particle( (i+random.uniform(0,1)) / particles_num * self._path_length, w) for i in xrange(0, particles_num)]
