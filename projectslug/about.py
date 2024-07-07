"""Generate about information for the user or bug reports."""
from __future__ import annotations
import os

import re
import pathlib
import platform

from PySide2 import __version__ as PySide2_Version
from PySide2.QtCore import QSysInfo

ROOT = pathlib.Path(__file__).parent.parent
USER = os.getenv('USERNAME', os.getenv('USER', 'unknown'))

def _get_git_branch():
    """Get git branch name if any."""

    head_file = ROOT / '.git' / 'HEAD'
    if head_file.exists():
        with head_file.open() as file:
            return file.read().split('/')[-1].strip()

    return ""

def _parse_pyproject():
    """Get package name and version from pyproject.toml."""
    with (ROOT / 'pyproject.toml').open() as file:
        content = file.read()
        name = re.search(r'(?<=name = ")[^"]+', content).group()
        version = re.search(r'(?<=version = ")[^"]+', content).group()
        return {
            'name': name,
            'version': version,
        }

def about():
    """Generate about information with various app versions.

    Returns:
        (tuple): a tuple containing tuple(str, str) with about information
    """
    # FIXME: Replace with your github link
    web = f'https://github.com/{USER}/projectslug'
    name, version = _parse_pyproject().values()

    data = {
        'app': {
            'App': name,
            'Version': version, 
            'PySide2': PySide2_Version,
            'Python': platform.python_version(),
            'Platform': QSysInfo().prettyProductName(),
        },
        'links': {
            'Readme': f'{web}/blob/main/README.md',
            'Issues': f'{web}/issues',
            'Changelog': f'{web}/blob/main/CHANGELOG.md',
            'Logs': f'file:///{ROOT}/logs',
        }
    }

    branch = _get_git_branch()
    if branch:
        data['app']['Branch'] = branch

    return data