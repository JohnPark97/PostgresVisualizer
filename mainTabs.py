from PyQt6.QtWidgets import QTabWidget, QWidget, QTableView
from table import *

class MainTabs(QTabWidget):
    def __init__(self, *args, **kwargs):
        super(QTabWidget, self).__init__(*args, **kwargs)

        list = [1, 2, 3]
        for x in list:
            self.addTab(Table("users"), str(x))