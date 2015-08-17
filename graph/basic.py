from matplotlib import pyplot as plt
from matplotlib import style

style.use('ggplot')

class BasicGraph(object):
    def __init__(self, name = "chart", xlabel = "X axis", ylabel = "Y axis"):
        self.title = name
        self.xlabel = xlabel
        self.ylabel = ylabel
        plt.figure()

    def show(self):
        plt.title(self.title)
        plt.xlabel(self.xlabel)
        plt.ylabel(self.ylabel)
        plt.legend()
        plt.show()

class MagneticLine(BasicGraph):
    def __init__(self):
        super(MagneticLine, self).__init__("Magnetic Chart", "Sampling point", "10e-3 T")
        self.lineNo = 1

    def addLine(self, data, label = None):
        if label:
            plt.plot(data, label = label)
        else:
            plt.plot(data, label = "line " + str(self.lineNo))
        self.lineNo += 1

    # def show(self):
    #     super(BasicGraph, self).show()

def main():
    ml = MagneticLine()
    ml.addLine([5,6,7,8])
    ml.show()

if __name__ == '__main__':
    main()
