from PyQt6.QtWidgets import QTableView
from customTableModel import *
from queryService import QueryService

class Table(QTableView):
    def __init__(self, table, *args, **kwargs):
        super(QTableView, self).__init__(*args, **kwargs)

        self.populateData()
        self.table = table

    def populateData(self):
        rows = QueryService.get(table="users")
        headers = QueryService.getHeaders(table="users")


        self.model = CustomTableModel(rows, headers)
        # self.model.setHorizontalHeaderLabels(headers)
        # self.model.setHeaderData(1, Qt.Horizontal, 'Date')
        self.setModel(self.model)
