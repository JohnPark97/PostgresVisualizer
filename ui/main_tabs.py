from PyQt6.QtWidgets import QTabWidget
from services.query_service import *
from common import *
from ui.table_widget import CustomTableWidget
from ui.tool_bar import ToolBar


class MainTabs(QTabWidget):
    def __init__(self, toolbar: ToolBar):
        super(QTabWidget, self).__init__()
        self.toolbar = toolbar

        # Connect the currentChanged signal to the on_tab_changed function
        self.currentChanged.connect(self.on_tab_changed)

        tables = [removeSpecialCharacters(str(i)) for i in QueryService.getTables()]

        for table_name in tables:
            data = QueryService.get(table_name)
            headers = QueryService.getHeaders(table_name)
            self.addTab(CustomTableWidget(data, headers, table_name), table_name)

        # Initialize the toolbar's current tab
        self.toolbar.set_curr_table(self.currentWidget())

    def on_tab_changed(self):
        self.toolbar.set_curr_table(self.currentWidget())
