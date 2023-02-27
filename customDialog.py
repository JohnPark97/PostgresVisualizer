from PyQt6.QtWidgets import QDialog, QVBoxLayout, QLineEdit, QHBoxLayout, QLabel, QDialogButtonBox
from queryService import QueryService

class CustomDialog(QDialog):
    def __init__(self, headers, type, parent=None):
        super(QDialog, self).__init__(parent)

        self.line_edits = []
        if type == "Add Row":
            self.setWindowTitle(type)

            # Create layout and add line edits to it
            v_layout = QVBoxLayout()
            h_layout = QHBoxLayout()

            # Take out the id section of the headers
            self.headers = headers[1:]

            for header in self.headers:
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
        QueryService.insert('accounts', self.headers, values_to_be_added)
        self.close()

    def get_dialog_values(self):
        return [line_edit.text() for line_edit in self.line_edits]