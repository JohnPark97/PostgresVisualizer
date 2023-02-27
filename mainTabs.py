from PyQt6.QtWidgets import QTabWidget
from queryService import *
from common import *
from tableWidget import CustomTableWidget


class MainTabs(QTabWidget):
    def __init__(self, *args, **kwargs):
        super(QTabWidget, self).__init__(*args, **kwargs)

        tables = [removeSpecialCharacters(str(i)) for i in QueryService.getTables()]

        for table in tables:
            data = QueryService.get(table)
            headers = QueryService.getHeaders(table)
            self.addTab(CustomTableWidget(data, headers), table)

    def currentTable(self):
        # TODO: make this changeable when the tab changes
        return self.currentWidget()