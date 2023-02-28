from PyQt6.QtWidgets import QDialog, QVBoxLayout, QLineEdit, QHBoxLayout, QLabel, QDialogButtonBox
from services.queryService import QueryService
from ui.tableWidget import CustomTableWidget

class CustomDialog(QDialog):
    def __init__(self, currentTable: CustomTableWidget, type, parent=None):
        super(QDialog, self).__init__(parent)
        self.currentTable = currentTable
        self.current_table_name = currentTable.table_name
        self.headers = self.currentTable.getHeaderNames()

        self.line_edits = []
        if type == "Add Row":
            self.setWindowTitle(type)

            # Create layout and add line edits to it
            v_layout = QVBoxLayout()
            h_layout = QHBoxLayout()

            # Take out the id section of the headers
            self.headers_no_id = self.headers[1:]

            for header in self.headers_no_id:
                label = QLabel(header)
                line_edit = QLineEdit()
                h_layout.addWidget(label)
                h_layout.addWidget(line_edit)
                self.line_edits.append(line_edit)

            # Buttons
            buttons = QDialogButtonBox(QDialogButtonBox.StandardButton.Ok | QDialogButtonBox.StandardButton.Cancel)
            buttons.button(QDialogButtonBox.StandardButton.Ok).clicked.connect(self.add_row_okay)
            buttons.button(QDialogButtonBox.StandardButton.Cancel).clicked.connect(self.close)

            v_layout.addLayout(h_layout)
            v_layout.addWidget(buttons)

            # Set layout for the dialog
            self.setLayout(v_layout)

            # Make the dialog visible
            self.exec()

    def add_row_okay(self): 
        values_to_be_added = self.get_dialog_values()
        # Insert to DB
        inserted_id = QueryService.insert(self.current_table_name, self.headers_no_id, values_to_be_added, self.headers[0])

        # Inserted data
        inserted_data = [inserted_id] + values_to_be_added
        # Add a row in table
        self.currentTable.add_row(inserted_data)


        self.close()

    def get_dialog_values(self):
        return [line_edit.text() for line_edit in self.line_edits]