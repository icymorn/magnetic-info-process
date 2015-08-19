from censor.ParticleFilter import ParticleFilter
from config.Config import config
from data.DataLoader import DataLoader

loader = DataLoader()
data = loader.read(config.data['datafile']['test'][1])
pFilter = ParticleFilter()
pFilter.load([config.data['datafile']['test'][1]]) # accept a "list" of magnetic data file.
pFilter.capture(data[80:95]) # a new slice of data captured
print pFilter.filter(0.2) # output the (dist, pos) of particle in position of 0.2
print pFilter.filter(0.4)
print pFilter.filter(0.5)
print pFilter.filter(0.7)
print pFilter.filter(0.9)
