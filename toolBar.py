from PyQt6.QtWidgets import QToolBar, QInputDialog
from PyQt6.QtGui import QAction
from queryService import *
from customDialog import *

ACTIONS = ['Add Row', 'Commit Changes']

class ToolBar(QToolBar):
    def __init__(self, mainTab):
        super(QToolBar, self).__init__(mainTab)
        self.currentTable = mainTab.currentTable()

        add_row_action = QAction('Add Row', self)
        add_row_action.setStatusTip('Add a row in database')
        add_row_action.triggered.connect(self.addRow)

        self.addAction(add_row_action)
        
    def addRow(self):
        headers = self.currentTable.getHeaderNames()
        messageBox = CustomDialog(headers, "Add Row")

        # QueryService.insert('accounts', [asdf])