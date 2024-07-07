# coding: utf-8
from __future__ import print_function

import sys

from PySide2.QtWidgets import QApplication

from .main import MainWindow


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.setWindowTitle('projectslug Local')
    # window.setGeometry(10, 10, 500, 500)
    window.show()
    app.exec_()

if __name__ == '__main__':
    main()

