from data.DataLoader import DataLoader

loader = DataLoader()
datapack = loader.datasource()

while True:
	print datapack.capture()