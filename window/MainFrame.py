import wx
from window.TreeCtrl import TreeCtrl
from window.CanvasPanel import CanvasPanel
class MainFrame(wx.Frame):

    def __init__(self):
        wx.Frame.__init__(self, None, title='wx.TreeCtrl')

        previewPanel = wx.Panel(self)

        treeCtrl = TreeCtrl(self)
        canvasPanel = CanvasPanel(previewPanel)

        controlPanel = wx.Panel(previewPanel, size = (-1, 50))
        controlBox = wx.BoxSizer(wx.HORIZONTAL)
        startButton = wx.Button(controlPanel, 1, "start")
        stopButton = wx.Button(controlPanel, 1, "stop")
        secondsLabel = wx.StaticText(controlPanel, label="seconds:")
        intervalSpin = wx.SpinButton(controlPanel, 1)
        startsAtLabel = wx.StaticText(controlPanel, label="starts at(%):")
        startSpin = wx.SpinButton(controlPanel, 1)
        dataLenLabel = wx.StaticText(controlPanel, label="data length:")
        dataLenSpin = wx.SpinButton(controlPanel, 1)

        intervalSpin.SetValue(2)
        startSpin.SetValue(0)
        dataLenSpin.SetValue(5)

        intervalSpin.SetRange(1, 5)
        startSpin.SetRange(0, 100)
        dataLenSpin.SetRange(1, 20)

        controlBox.Add(startButton, 1, wx.LEFT | wx.ALIGN_CENTER_VERTICAL)
        controlBox.Add(stopButton, 1, wx.RIGHT | wx.ALIGN_CENTER_VERTICAL)
        controlBox.Add(secondsLabel, 1, wx.ALIGN_CENTER_VERTICAL)
        controlBox.Add(intervalSpin, 1, wx.ALIGN_CENTER_VERTICAL)
        controlBox.Add(startsAtLabel, 1, wx.ALIGN_CENTER_VERTICAL)
        controlBox.Add(startSpin, 1, wx.ALIGN_CENTER_VERTICAL)
        controlBox.Add(dataLenLabel, 1, wx.ALIGN_CENTER_VERTICAL)
        controlBox.Add(dataLenSpin, 1, wx.ALIGN_CENTER_VERTICAL)
        controlPanel.SetSizer(controlBox)

        treeCtrl.setOnloadFunc(canvasPanel.loadFileGraph)

        vbox = wx.BoxSizer(wx.VERTICAL)
        vbox.Add(canvasPanel, 2, wx.EXPAND | wx.LEFT | wx.RIGHT | wx.TOP| wx.BOTTOM , 5)
        vbox.Add(controlPanel, 0, wx.LEFT)

        previewPanel.SetSizer(vbox)

        hbox = wx.BoxSizer(wx.HORIZONTAL)
        hbox.Add(treeCtrl, 0, wx.EXPAND | wx.TOP | wx.BOTTOM, 5)
        hbox.Add(previewPanel, 2, wx.EXPAND | wx.TOP | wx.LEFT | wx.RIGHT | wx.BOTTOM, 5)

        self.SetSizer(hbox)
        self.SetSize((700, 800))
        self.Centre()

        self.previewPanel = previewPanel
        self.canvasPanel  = canvasPanel
        self.controlPanel = controlPanel
        self.treeCtrl     = treeCtrl
        self.startButton  = startButton
        self.stopButton   = stopButton
        self.interval     = intervalSpin

        self.setCallback()

    def setCallback(self):
        pass
        # self.startButton.Bind(wx.EVT_BUTTON, lambda e: self.canvasPanel.draw())
