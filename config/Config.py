import yaml
import os

class Config:

    def __init__(self, filename):
        stream    = file(filename, 'r')
        self.data = yaml.load(stream)

def main():
    config = Config('config.yaml')
    print config.data

if __name__ == '__main__':
    main()
else:
    config = Config(os.path.dirname(__file__) + '/config.yaml')
