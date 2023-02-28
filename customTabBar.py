from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPainter, QColor
from PyQt6.QtWidgets import QTabBar

# NOT IN USE
class MyTabBar(QTabBar):
    def __init__(self, parent=None):
        super().__init__(parent)
        
    def paintEvent(self, event):
        painter = QPainter(self)
        option = self.tabRect(0)

        # Draw a line for each tab except the last one
        for i in range(self.count() - 1):
            tab_rect = self.tabRect(i)
            x = tab_rect.x() + tab_rect.width()
            y1 = tab_rect.y() + tab_rect.height() + 1
            y2 = option.y() + option.height() - 1
            painter.setPen(QColor(200, 200, 200))
            painter.drawLine(x, y1, x, y2)

        # Draw the last tab without a line
        tab_rect = self.tabRect(self.count() - 1)
        painter.setPen(QColor(200, 200, 200))
        painter.drawRoundedRect(tab_rect, 5, 5)
        painter.drawText(tab_rect, Qt.AlignmentFlag.AlignCenter, self.tabText(self.count() - 1))