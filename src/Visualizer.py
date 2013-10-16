# -*- coding: utf-8 -*-

from PySide import QtCore, QtGui
from Ui_MainWindow import *
import sys

import numpy as np

import matplotlib
import matplotlib.animation as animation

import sys
# specify the use of PySide
matplotlib.rcParams['backend.qt4'] = "PySide"

# import the figure canvas for interfacing with the backend
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas

# import 3D plotting
from mpl_toolkits.mplot3d import Axes3D    # @UnusedImport
from matplotlib.figure import Figure

from ClosedSystem import ClosedSystem


class MainWindow(QtGui.QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.ui =  Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.plotWidget = AnimationWidget(parent = self.ui.animationTab )

class AnimationWidget(FigureCanvas):
    def __init__(self, parent=None):
        self.figure = Figure(facecolor=(0, 0, 0))
        super(AnimationWidget, self).__init__(self.figure)
        self.setParent(parent)

        self.system = ClosedSystem()
        self.system.create_particles()
        self.system.calculate_state()
        self.axes = self.figure.add_subplot(111, projection = '3d')

        for particle in self.system.particles:
            self.axes.scatter(particle.r[0], particle.r[1], particle.r[2])

	

    def update(self):
        self.system.evolve()
        for particle in self.system.particles:
            self.axes.scatter(particle.r[0], particle.r[1], particle.r[2])

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    mySW = MainWindow()
    mySW.show()
    sys.exit(app.exec_())