import wx
from window.CanvasPanel import CanvasPanel
from window.MainFrame import MainFrame

def main():
    app = wx.App(False)
    frame = MainFrame()
    frame.Show()
    app.MainLoop()
