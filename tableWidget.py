from PyQt6.QtWidgets import QTableWidget, QTableWidgetItem

class CustomTableWidget(QTableWidget):
    def __init__(self, data, headers):
        super(QTableWidget, self).__init__()
        self.setColumnCount(len(headers))
        self.setHorizontalHeaderLabels(headers)
        self.setRowCount(len(data))
        for i in range(len(data)):
            for j in range(len(headers)):
                self.setItem(i, j, QTableWidgetItem(str(data[i][j])))


