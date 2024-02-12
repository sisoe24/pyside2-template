"""Toolbar widget module."""
# coding: utf-8
from __future__ import annotations

from functools import partial

from PySide2.QtCore import Qt, Slot
from PySide2.QtGui import QDesktopServices
from PySide2.QtWidgets import (QAction, QFormLayout, QLabel, QPushButton,
                               QToolBar, QVBoxLayout, QWidget)

from ..about import about


def _show_window(widget: QWidget):
    """Show a widget window.

    If widget is already visible then regain focus.

    Args:
        widget (QWidget): a widget to insert inside the dialog widget.
    """
    widget.show()
    widget.activateWindow()
    widget.raise_()


class AboutWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        about_data = about()

        app_form_layout = QFormLayout()
        for key, value in about_data['app'].items():
            app_form_layout.addRow(key, QLabel(value))

        links_form_layout = QFormLayout()
        for key, value in about_data['links'].items():
            btn = QPushButton(key)
            btn.clicked.connect(partial(self._open_link, value))
            links_form_layout.addRow('', btn)

        layout = QVBoxLayout()
        layout.addLayout(app_form_layout)
        layout.addLayout(links_form_layout)
        self.setLayout(layout)
    
    @Slot(str)
    def _open_link(self, link: str):
        """Open a link in the default browser.

        Args:
            link (str): a link to open.
        """
        QDesktopServices.openUrl(link)


class ToolBar(QToolBar):
    """Custom QToolBar class."""

    def __init__(self, parent=None):
        """Init method for the ToolBar class."""
        super().__init__(parent)

        self.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.setMovable(False)
        self.setStyleSheet('color: white;')

        self.setup_action(title='About', widget=AboutWidget())

    def setup_action(self, title: str, widget: QWidget):
        """Set up action for toolbar.

        Connect a QAction trigger signal to spawn the floating window.

        Args:
            title (str): name of the action.
            widget (QWidget): QWidget to use as a floating window.

        Returns:
            QAction: The QAction created.

        """
        action = QAction(title, self)
        action.triggered.connect(lambda: _show_window(widget))
        self.addAction(action)
        return action
