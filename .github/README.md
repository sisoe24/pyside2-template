# Nuke Pyside2 Template

A Python PySide2 plugin template for Nuke.

## Description

This project is a template to create a basic plugin in Nuke with PySide2.

> To use this template, you need to use the Visual Studio Code extension [NukeTools](https://marketplace.visualstudio.com/items?itemName=virgilsisoe.nuke-tools).

## Features

- A ready-to-use QMainWindow with a QToolbar.
  - The toolbar offers an "About" widget with information about the application.
- A custom QMessageBox for errors and bug reports.
- A startup logging module.
- The ability to launch the plugin as a standalone application, (outside Nuke).

If using Visual Studio Code the following tasks will be available

- `Clean .pyc`: clean .pyc files.
- `Run Local Application`: Run application locally.

## Usage

You can use the template in two ways:

### Visual Studio Code

1. Install [NukeTools](https://marketplace.visualstudio.com/items?itemName=virgilsisoe.nuke-tools) for Visual Studio Code.
2. Launch the command `Nuke: Create PySide template`

### Manual

1. Clone the repository.
2. Run the script `template.py` and supply the necessary information.

  ```bash
  python template.py -h
  python template.py "MyPlugin" "/path/to/nuke/plugin"
  ```

You can now run Nuke and find the plugin inside Window -> Custom. Alternately you can run the plugin in [local mode](#run-standalone).

## Run Standalone

To run the application outside Nuke, you must install the package dependencies. You can do so with the `pyproject.toml` by using `poetry` or the `requirements.txt` by using `pip`.

You can run the application in one of the following ways:

* `poetry run app`
* `poetry run python -m run_app.main` 
