from PyQt6.QtWidgets import QToolBar, QInputDialog
from PyQt6.QtGui import QAction
from services.query_service import *
from ui.custom_dialog import *

ACTIONS = ['Add Row', 'Update']

class ToolBar(QToolBar):
    def __init__(self):
        super(QToolBar, self).__init__()

        add_row_action = QAction('Add Row', self)
        add_row_action.setStatusTip('Add a row in database')
        add_row_action.triggered.connect(self.prompt_add_row)

        commit_change_action = QAction('Update', self)
        commit_change_action.setStatusTip('Update a row(s)')
        commit_change_action.triggered.connect(self.prompt_update_row)

        self.addAction(add_row_action)
        self.addAction(commit_change_action)
        
    def prompt_add_row(self):
        CustomDialog(self.currentTable, "Add Row")

    def prompt_update_row(self):
        CustomDialog(self.currentTable, "Update")

    def set_curr_table(self, curr_widget):
        self.currentTable = curr_widget