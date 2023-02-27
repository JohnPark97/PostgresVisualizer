
from PyQt6.QtWidgets import QMainWindow
from mainTabs import *
from toolBar import ToolBar

class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.setWindowTitle("Postgresql Visualizer")
        width = 800
        height = 500
        self.setMinimumSize(width, height)
        self._tabWidget = MainTabs(self)
        self.setCentralWidget(self._tabWidget)

        self.toolbar = ToolBar(self._tabWidget)
        self.addToolBar(self.toolbar)
