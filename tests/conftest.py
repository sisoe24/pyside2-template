"""Pytest configuration file."""
import os

import pytest

from src.main import MainWindow


def pytest_addoption(parser):
    """Add pytest new options."""
    parser.addoption(
        '--checklinks', action='store_true', default=False, help='Validate web link'
    )


def pytest_collection_modifyitems(config, items):
    """Change pytest behavior for certain marks."""
    if config.getoption('--checklinks'):
        return

    skip_check = pytest.mark.skip(reason='need --checklinks option to run')

    for item in items:
        if "web" in item.keywords:
            item.add_marker(skip_check)


def pytest_configure(config):
    """Add pytest new configurations."""
    config.addinivalue_line('markers', 'web: validate web link')
    config.addinivalue_line('markers', 'rapidtest: rapid test')


@pytest.fixture(scope='session')
def _package():
    """Package directory path.

    Yields:
        str: path of the package root.
    """
    current_dir = os.path.dirname(__file__)
    package_dir = os.path.abspath(os.path.dirname(current_dir))

    yield package_dir


@pytest.fixture()
def _main_ui(qtbot):
    """Initialize Main UI Widget."""
    widget = MainWindow()
    qtbot.addWidget(widget)
    yield widget
