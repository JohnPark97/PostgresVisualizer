from PyQt6.QtWidgets import QTableWidget, QTableWidgetItem, QHeaderView

class CustomTableWidget(QTableWidget):
    def __init__(self, data, headers):
        super(QTableWidget, self).__init__()
        self.setColumnCount(len(headers))
        self.setHorizontalHeaderLabels(headers)

        # resize cell by the header length
        header = self.horizontalHeader()
        for i in range(len(header)):
            header.setSectionResizeMode(i, QHeaderView.ResizeMode.ResizeToContents)
        header.setSectionResizeMode(0, QHeaderView.ResizeMode.Fixed)

        # set initial rows
        for row in data:
            self.add_row(row)

    def getHeaderNames(self):
        num_cols = self.columnCount()
        header_names = []
        for col in range(num_cols):
            header_item = self.horizontalHeaderItem(col)
            header_name = header_item.text()
            header_names.append(header_name)

        return header_names

    def add_row(self, row):
        row_count = self.rowCount()
        col_count = self.columnCount()
        self.insertRow(row_count)

        for i in range(col_count):
            item = QTableWidgetItem(str(row[i]))
            self.setItem(row_count, i, item)