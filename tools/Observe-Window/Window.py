# ------------------------------------------------------------------------
# coding=utf-8
# ------------------------------------------------------------------------
#
#  Created by Jason Wu on 2015-08-29
#
# ------------------------------------------------------------------------

from __future__ import absolute_import

import sys
import zmq
import threading

from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.Qwt5 import *
from Ui_Window import Ui_MainWindow

class Window(QMainWindow,Ui_MainWindow):
    def __init__(self,  parent=None):
        super(Window, self).__init__(parent)
        self.setupUi(self)
        self.initMyUI()
        self.init()
        self.show()

    def initMyUI(self):
        self.qwtPlot.setTitle("Particle Filter")
        self.qwtPlot.setAxisTitle(self.qwtPlot.xBottom, "p.x (m)")
        self.qwtPlot.setAxisTitle(self.qwtPlot.yLeft, "p.w")
        self.qwtPlot.setAxisScale(self.qwtPlot.yLeft,0,0.2,0.1)
        self.qwtPlot.setAxisScale(self.qwtPlot.xBottom,0,20,1.2)

        self.curve = QwtPlotCurve()
        self.curve.attach(self.qwtPlot)
        self.layout().addWidget(self.qwtPlot)
        self.curve.setStyle(QwtPlotCurve.Sticks)
        self.symbol = QwtSymbol()
        self.symbol.setStyle(QwtSymbol.Ellipse)
        self.symbol.setSize(5)
        self.symbol.setBrush(QColor(255,0,0))
        self.curve.setSymbol(self.symbol)

        self.curveCenter = QwtPlotCurve()
        self.curveCenter.attach(self.qwtPlot)
        self.curveCenter.setStyle(QwtPlotCurve.Sticks)
        self.curveCenter.setPen(QColor(0,255,0))

        self.curveMax = QwtPlotCurve()
        self.curveMax.attach(self.qwtPlot)
        self.curveMax.setStyle(QwtPlotCurve.Sticks)
        self.curveMax.setPen(QColor(255,0,0))

        self.curveSimulate = QwtPlotCurve()
        self.curveSimulate.attach(self.qwtPlot)
        self.curveSimulate.setStyle(QwtPlotCurve.Sticks)
        self.curveSimulate.setPen(QColor(0,0,255))
        
        self.connect(self, SIGNAL("replot"), self.replot_particles)

    def init(self):
        self.recvthread = threading.Thread(target=self.recvThread)
        self.recvthread.setDaemon(True)
        self.recvthread.start()

        self.x_predict = 0.0
        self.x_simulate = 0.0
        self.poss = []
        self.weights = []

    def setupReplot(self):
        #particles
        x = self.poss
        y = self.weights
        self.curve.setData(x,y)
        #max
        xM = [self.x_predict]
        yM = [1]
        self.curveMax.setData(xM,yM)
        #simulate
        xS = [self.x_simulate]
        yS = [1]
        self.curveSimulate.setData(xS,yS)

    def replot_particles(self):
        self.qwtPlot.replot()

    def recvThread(self):
        try:
            # Socket to talk to server
            context = zmq.Context()
            socket = context.socket(zmq.SUB)
            socket.connect ("tcp://127.0.0.1:9955")
            socket.setsockopt(zmq.SUBSCRIBE, '')
            while True:
                data = socket.recv_pyobj()
                self.x_predict = data.get('x_predict')
                self.x_simulate = data.get('x_simulate')
                self.poss = data.get('poss')
                self.weights = data.get('weights')
                self.setupReplot()
                self.emit(SIGNAL("replot"))
        except Exception,ex:
            print "recvThread ",Exception," : ",ex
   
if __name__ == "__main__":
    app = QApplication(sys.argv)
    myapp = Window()
    myapp.show()

sys.exit(app.exec_())
