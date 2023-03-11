from PyQt6.QtWidgets import QTableWidget, QTableWidgetItem, QHeaderView, QAbstractItemView
from PyQt6.QtGui import QPalette, QColor
from PyQt6.QtCore import Qt, QItemSelection, QItemSelectionModel

class CustomTableWidget(QTableWidget):
    def __init__(self, data, headers, table_name):
        super(QTableWidget, self).__init__()
        # { key: row # value: original values stored in row }
        self.changed_rows_map = {}
        self.headers = headers
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
            # convert the first element to a string
            row = [int(list(row)[0])] + list(row)[1:]
            self.add_row(row)


        # Enable sorting and set the default sort column and order
        self.setSortingEnabled(True)
        self.sortItems(0, Qt.SortOrder.AscendingOrder)
        
        # Set selection color to light blue
        palette = self.palette()
        palette.setColor(QPalette.ColorRole.Highlight, QColor(220, 220, 255))
        palette.setColor(QPalette.ColorRole.HighlightedText, QColor(Qt.GlobalColor.black))

        self.setPalette(palette)

        # Only let single row selection
        self.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)

        # Select the whole row when a single cell is selected
        self.setSelectionBehavior(QTableWidget.SelectionBehavior.SelectRows)

        # Detect any changes made
        self.itemChanged.connect(self.stage_changes)

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
            item = QTableWidgetItem(row[i])
            item.setData(Qt.ItemDataRole.DisplayRole, row[i])
            self.setItem(row_count, i, item)

    def stage_changes(self):
        selected_items = self.selectedItems()

        if selected_items:
            row = selected_items[0].row()

            staged_item = {}
            for index, selected_item in enumerate(selected_items):
                header = self.headers[index]
                staged_item[header] = selected_item.text()
                selected_item.setBackground(QColor("#FFFFCC"))

            self.changed_rows_map[row] = staged_item

    def get_staged_changes(self):
        return self.changed_rows_map
    
    def clear_changed_rows_map(self):
        self.changed_rows_map.clear()
    
    def restore_table_color_to_white(self):
        self.clearSelection()
        # iterate over all the cells in the table
        for row in range(self.rowCount()):
            for col in range(self.columnCount()):
                # get the cell item and set its background color to white
                item = self.item(row, col)
                if item is not None and not item.isSelected():
                    item.setBackground(QColor('white'))