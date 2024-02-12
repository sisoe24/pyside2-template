from __future__ import annotations

import traceback
from pprint import pformat

from PySide2.QtGui import QClipboard, QDesktopServices
from PySide2.QtWidgets import QMessageBox, QPushButton

from ..about import about


class ErrorDialog(QMessageBox):
    """Error dialog widget.

    Show a QMessageBox with a warning icon and a detailed text with the traceback
    of the error. It also has buttons to report the bug and open the logs.

    """

    def __init__(self, msg: str, parent=None):
        super().__init__(parent)

        self.setWindowTitle('projectslug')
        self.setIcon(QMessageBox.Warning)

        self.setText('projectslug error...')
        self.setInformativeText(msg)

        self.setStandardButtons(QMessageBox.Cancel | QMessageBox.Ok)
        self.addButton('Report bug', QMessageBox.ActionRole)
        self.addButton('Open logs', QMessageBox.ActionRole)

        self.buttonClicked.connect(self._on_click_button)

        self._traceback = traceback.format_exc()
        self.setDetailedText(
            'Traceback will be copied to clipboard when clicking Report Bug.'
            '\n---\n' + self._traceback
        )

    def _on_click_button(self, button: QPushButton):
        about_data = about()

        links = about_data['links']

        if button.text() == 'Report bug':
            QClipboard().setText(
                f'{pformat(about_data["app"])}\n\n{self._traceback}'
            )
            link = links['Issues']

        elif button.text() == 'Open logs':
            link = links['Logs']

        elif button.text() in ('OK', 'Cancel'):
            return

        else:
            link = ''

        QDesktopServices.openUrl(link)
