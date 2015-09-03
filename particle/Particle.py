# ------------------------------------------------------------------------
# coding=utf-8
# ------------------------------------------------------------------------
#
#  Created by Jason Wu on 2015-08-29
#
# ------------------------------------------------------------------------

import random

class Particle(object):
    def __init__(self, pos, w=1):
        self._pos = pos
        self._w = w

    def __repr__(self):
        return "(x=%f, w=%f)" % (self._pos, self._w)

    @property
    def pos(self):
        return self._pos

    @pos.setter
    def pos(self, value):
        if not isinstance(value, float):
            raise ValueError('pos must be an float!')
        if value < 0.0:
            self._w = 0.0
            #raise ValueError('pos must between 0.0 ~ 1.0 !')
        self._pos = value

    @property
    def w(self):
        return self._w

    @w.setter
    def w(self, value):
        if not isinstance(value, float):
            raise ValueError('weight must be an float!')
        if value < 0.0 or value > 1.0:
            raise ValueError('weight must between 0.0 ~ 1.0 !')
        self._w = value