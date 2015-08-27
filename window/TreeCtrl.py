import wx
import os

class TreeCtrl(wx.TreeCtrl):

    def __init__(self, parent):
        wx.TreeCtrl.__init__(self, parent, 0, size = (150, -1))
        self.loadTreeData()
        self.ExpandAll()

        self.setOnloadFunc(printData)

    def loadFileList(self):
        contents = os.listdir('./data')
        files = []
        for item in contents:
            if os.path.isfile('./data/' + item) and item.endswith('.data'):
                files.append(item)
        return files

    def loadTreeData(self):
        filelist = self.loadFileList()
        self.root = self.AddRoot('File list')
        for filename in filelist:
            self.AppendItem(self.root, filename )

    def setOnloadFunc(self, func):
        self.Bind(wx.EVT_TREE_SEL_CHANGED, lambda evt: func(self.GetItemText(evt.GetItem())))



def printData(data):
    print data
