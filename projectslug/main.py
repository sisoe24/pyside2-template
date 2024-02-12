from __future__ import annotations

import logging
from random import randint
from typing import Optional

from PySide2.QtCore import Qt, Slot
from PySide2.QtGui import QColor, QPalette
from PySide2.QtWidgets import (QHeaderView, QLabel, QMainWindow, QPushButton,
                               QTableWidget, QTableWidgetItem, QVBoxLayout,
                               QWidget)

from . import nuke
from .widgets import ErrorDialog, ToolBar

LOGGER = logging.getLogger('projectslug')


class NodesTable(QTableWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.setColumnCount(2)
        self.setHorizontalHeaderLabels(['Name', 'Type'])
        self.setSelectionBehavior(QTableWidget.SelectRows)
        self.setSelectionMode(QTableWidget.SingleSelection)
        self.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        self.itemClicked.connect(self.zoom_node)
    
    def _item_builder(self, text: str):
        item = QTableWidgetItem(text)
        item.setFlags(item.flags() & ~Qt.ItemIsEditable)
        return item

    @Slot()
    def zoom_node(self):
        item = self.item(self.currentRow(), 0)

        node = nuke.toNode(item.text())
        if not node:
            return

        node.selectOnly()
        nuke.zoomToFitSelected()

    def refresh(self):
        # clear previous rows
        self.clearContents()

        nodes = nuke.allNodes()
        self.setRowCount(len(nodes))

        for index, node in enumerate(nodes):
            self.setItem(index, 0, self._item_builder(node.name()))
            self.setItem(index, 1, self._item_builder(node.Class()))


class ExampleWidgets(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        table = NodesTable()

        refresh_btn = QPushButton("Refresh")
        refresh_btn.clicked.connect(table.refresh)

        layout = QVBoxLayout()
        layout.addWidget(QLabel('<h2>Nodes</h2>'))
        layout.addWidget(table)
        layout.addWidget(refresh_btn)

        self.setLayout(layout)


class MainWindow(QMainWindow):

    def __init__(self, parent=None):
        super().__init__(parent)

        LOGGER.info('Main window created.')

        self.setWindowTitle("myproject")
        self.addToolBar(ToolBar())

        try:
            main_widgets = ExampleWidgets()
        except Exception as err:
            ErrorDialog(str(err), self).show()
            LOGGER.critical(err, exc_info=True)
        else:
            self.setCentralWidget(main_widgets)

    def _debug_colors(self, widget: Optional[QWidget] = None):
        """Set random colors to all widgets for debugging purposes."""
        widget = widget or self
        for child in widget.children():

            if not isinstance(child, QWidget):
                continue

            child.setAutoFillBackground(True)
            palette = QPalette()
            palette.setColor(
                QPalette.Window,
                QColor(randint(0, 255), randint(0, 255), randint(0, 255)),
            )
            child.setPalette(palette)
            self._debug_colors(child)


try:
    import nukescripts
except ImportError as error:
    pass
else:
    nukescripts.panels.registerWidgetAsPanel(
        'projectslug.projectslug.main.MainWindow', 'projectslug',
        'projectslug.MainWindow')
