from PyQt6.QtWidgets import QToolBar, QInputDialog
from PyQt6.QtGui import QAction
from services.queryService import *
from ui.customDialog import *

ACTIONS = ['Add Row', 'Commit Changes']

class ToolBar(QToolBar):
    def __init__(self):
        super(QToolBar, self).__init__()

        add_row_action = QAction('Add Row', self)
        add_row_action.setStatusTip('Add a row in database')
        add_row_action.triggered.connect(self.prompt_add_row)

        self.addAction(add_row_action)
        
    def prompt_add_row(self):
        CustomDialog(self.currentTable, "Add Row")

    def set_curr_table(self, curr_widget):
        self.currentTable = curr_widget