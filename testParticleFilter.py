from censor.ParticleFilter import ParticleFilter
from config.Config import config
from data.DataLoader import DataLoader

loader = DataLoader()
data = loader.read(config.data['datafile']['test'][1])
pFilter = ParticleFilter()
pFilter.load([config.data['datafile']['test'][1]])
pFilter.capture(data[80:95])
print pFilter.filter(0.2)
print pFilter.filter(0.4)
print pFilter.filter(0.5)
print pFilter.filter(0.7)
print pFilter.filter(0.9)
