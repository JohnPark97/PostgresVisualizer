from PyQt6.QtWidgets import QTableWidget, QTableWidgetItem, QHeaderView

class CustomTableWidget(QTableWidget):
    def __init__(self, data, headers):
        super(QTableWidget, self).__init__()
        self.setColumnCount(len(headers))
        self.setHorizontalHeaderLabels(headers)
        self.setRowCount(len(data))
        for i in range(len(data)):
            for j in range(len(headers)):
                self.setItem(i, j, QTableWidgetItem(str(data[i][j])))

        # resize cell by the header length
        header = self.horizontalHeader()
        for i in range(len(header)):
            header.setSectionResizeMode(i, QHeaderView.ResizeMode.ResizeToContents)
        header.setSectionResizeMode(0, QHeaderView.ResizeMode.Fixed)

    def getHeaderNames(self):
        num_cols = self.columnCount()
        header_names = []
        for col in range(num_cols):
            header_item = self.horizontalHeaderItem(col)
            header_name = header_item.text()
            header_names.append(header_name)

        return header_names

