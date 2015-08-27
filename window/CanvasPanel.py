import wx

import matplotlib
matplotlib.use('WXAgg')

from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigureCanvas
from matplotlib.figure import Figure
from data.DataLoader import DataLoader
import os

class CanvasPanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        self.figure = Figure()
        self.axes = self.figure.add_subplot(111)
        self.canvas = FigureCanvas(self, -1, self.figure)
        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.sizer.Add(self.canvas, 1, wx.LEFT | wx.TOP | wx.GROW)
        self.SetSizer(self.sizer)
        self.Fit()
        self.data = None

    def setLine(self, line):
        self.data = line

    def draw(self):
        self.axes.clear()
        if self.data is not None:
            self.axes.plot(self.data)
        self.canvas.draw()

    def loadFileGraph(self, filename):
        filepath = './data/' + filename
        if os.path.isfile(filepath):
            loader = DataLoader()
            self.setLine(loader.read(filepath))
            self.draw()
