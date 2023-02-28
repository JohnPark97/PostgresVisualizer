from PyQt6.QtWidgets import QTableWidget, QTableWidgetItem, QHeaderView
from PyQt6.QtGui import QPalette, QColor
from PyQt6.QtCore import Qt

class CustomTableWidget(QTableWidget):
    def __init__(self, data, headers, table_name):
        super(QTableWidget, self).__init__()
        self.table_name = table_name
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
        
        # Set selection color to light blue
        palette = self.palette()
        palette.setColor(QPalette.ColorRole.Highlight, QColor(220, 220, 255))
        palette.setColor(QPalette.ColorRole.HighlightedText, QColor(Qt.GlobalColor.black))

        self.setPalette(palette)

        # Select the whole row when a single cell is selected
        self.setSelectionBehavior(QTableWidget.SelectionBehavior.SelectRows)

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