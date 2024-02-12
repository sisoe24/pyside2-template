"""Logging module."""
from __future__ import annotations

import sys
import logging
import pathlib

LOG_PATH = pathlib.Path(__file__).parent.parent / 'logs'
LOG_PATH.mkdir(exist_ok=True)

LOGGER = logging.getLogger('projectslug')
LOGGER.propagate = False
LOGGER.setLevel(logging.DEBUG)

BASE_FORMAT = logging.Formatter(
    '[%(asctime)s]  %(levelname)-10s %(filename)-25s %(funcName)-25s :: %(message)s',
    "%m-%d %I:%M%p")


def set_critical():
    critical = logging.FileHandler(LOG_PATH / 'errors.log', 'w')
    critical.setLevel(logging.ERROR)
    critical.setFormatter(BASE_FORMAT)
    critical.set_name('Critical')
    return critical


def set_debug():
    debug = logging.FileHandler(LOG_PATH / 'debug.log', 'w')
    debug.set_name('Debug')
    debug.setLevel(logging.DEBUG)
    debug.setFormatter(BASE_FORMAT)
    return debug


def set_console():
    console_format = logging.Formatter(
        '%(name)s %(levelname)-8s %(module)-10s%(funcName)-15sL:%(lineno)-5d :: %(message)s')
    console = logging.StreamHandler(stream=sys.stdout)
    console.set_name('Console')
    console.setLevel(logging.WARNING)
    console.setFormatter(console_format)
    return console


LOGGER.addHandler(set_console())
LOGGER.addHandler(set_critical())
LOGGER.addHandler(set_debug())
