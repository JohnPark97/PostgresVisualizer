from PyQt6.QtWidgets import QTableView
from customTableModel import *
from services.query_service import QueryService

# NOT IN USE
class CustomTable(QTableView):
    def __init__(self, table, *args, **kwargs):
        super(QTableView, self).__init__(*args, **kwargs)

        self.populateData()
        self.table = table

    def populateData(self):
        rows = QueryService.get(table="users")
        headers = QueryService.getHeaders(table="users")


        self.model = CustomTableModel(rows, headers)
        self.setModel(self.model)
