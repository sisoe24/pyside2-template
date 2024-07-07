# Nuke Pyside2 Template

A Python PySide2 plugin template for Nuke.

## Description

A basic template to create a basic plugin in Nuke with PySide2 with Python 3+.

## Features

- A ready-to-use QMainWindow with a QToolbar.
  - "About" widget with information about the application.
- A custom QMessageBox for errors and bug reports.
- A startup logging module.
- The ability to launch the plugin as a standalone application, (outside Nuke).

If using Visual Studio Code the following tasks will be available

- `Clean .pyc`: clean .pyc files.
- `Run Local`: Run application locally.

## Usage

You can use the template in two ways:

### Visual Studio Code

1. Install [NukeTools](https://marketplace.visualstudio.com/items?itemName=virgilsisoe.nuke-tools) for Visual Studio Code.
2. Launch the command `Nuke: Add Packages -> pysideTemplate`.

### Manual

1. Use as a template from this repository.
2. Run the script `scripts/substitute_placeholders.py` and supply the necessary information.

  ```bash
  python scripts/substitute_placeholders.py --init
  ```
3. Import the plugin into your menu.py file.

You can now run Nuke and find the plugin inside Window -> Custom. Alternately you can run the plugin in [local mode](#run-standalone).

## Run Standalone

To run the application outside Nuke, you must install the package dependencies. You can do so with the `pyproject.toml` by using `poetry` or the `requirements.txt` by using `pip`.

If you are using `poetry` you can run the following commands:

```bash
poetry install
poetry run local
```

## Notes

- From version `0.2.0` the template is not compatible with Python 2.7 anymore.
