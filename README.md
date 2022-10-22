# Nuke Pyside2 Template

A Python PySide2 plugin template for Nuke.

## Description

This project is a template to create a basic plugin in Nuke with PySide2.

> To use this template, you need to use the Visual Studio Code extension [NukeTools](https://marketplace.visualstudio.com/items?itemName=virgilsisoe.nuke-tools).

## Features

- A ready-to-use QMainWindow with a QToolbar and a QStatusBar.
  - The toolbar offers an "About" widget with information about the application.
- A custom QMessageBox for errors and bug reports.
- A test environment with `pytest` and some sample tests to startup.
- A wrapper function to color a QWidget for layout testing.
- A startup logging module.
- The ability to launch the plugin as a standalone application, i.e., outside Nuke.

If using Visual Studio Code the following tasks will be available

- `Clean .pyc`: clean .pyc files (works only on Unix systems).
- `Toggle Widgets Color`: Toggle widget color state.
- `Run Local Application`: Run application locally.

## Usage

1. Install [NukeTools](https://marketplace.visualstudio.com/items?itemName=virgilsisoe.nuke-tools) for Visual Studio Code.
2. Launch the command `Nuke: Create PySide template`

You can now run Nuke and find the plugin inside Window -> Custom. Alternately you can run the plugin in [local mode](#run-standalone).

### Color Widgets

The module `color_widget.py` offers a utility function that can color the widget's layout to understand its proportions better.

```py
from .utility import color_widget

class Widget(QWidget):
    @color_widget()
    def __init__(self):
        super().__init__()
```

To toggle the widget color state, you can use the vscode command `Toggle Widgets Color`.

NOTE:

- It only works on an `__init__` method of a QWidget class instance.
- It can accept parameters value such as what color to use.

## Tests

Some sample tests are already included using `pytest`.

### Fixtures

- `_main_ui`: which initializes the main UI.
- `_package`: the package root directory.

## Run Standalone

To run the application outside Nuke, you must install the package dependencies. You can do so with the `pyproject.toml` by using `poetry` or the `requirements.txt` by using `pip`.

You can the run the application with the vscode `Run Local Application` task or
`poetry run python -m src.run_local`.
