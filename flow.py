from config.Config import config
from data.DataLoader import DataLoader
from algorithm.Dtw import dtwCalculate

testdatafilename = config.data['datafile']['test']
dl = DataLoader()
line1 = dl.read(testdatafilename[0])

sub = line1[100:105]

dist, position= dtwCalculate(sub, line1)
