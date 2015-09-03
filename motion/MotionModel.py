# ------------------------------------------------------------------------
# coding=utf-8
# ------------------------------------------------------------------------
#
#  Created by Jason Wu on 2015-08-20
#
# ------------------------------------------------------------------------

from scipy.stats import norm
from config.Config import config

class  MotionModel(object):
	def __init__(self,):
		self.step_standard_deviation = config.data['particle']['speed_standard_deviation']

	def update(self, pos, step, noise=False):
	    	if noise == True:
	    		return pos + norm.rvs(step, self.step_standard_deviation)
	    	else:
	    		return pos + step
