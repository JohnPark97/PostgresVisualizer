from PyQt6.QtWidgets import QDialog, QVBoxLayout, QLineEdit, QHBoxLayout, QLabel, QDialogButtonBox

class CustomDialog(QDialog):
    def __init__(self, headers, type, parent=None):
        super(QDialog, self).__init__(parent)

        if type == "Add Row":
            self.setWindowTitle(type)

            # Create layout and add line edits to it
            v_layout = QVBoxLayout()
            h_layout = QHBoxLayout()
            for header in headers:
                label = QLabel(header)
                line_edit = QLineEdit()
                h_layout.addWidget(label)
                h_layout.addWidget(line_edit)

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
        # TODO: implementation
        self.close()
