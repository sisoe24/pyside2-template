import os
import pytest

from src.main import MainWindow


def test_main(_main_ui):
    assert isinstance(_main_ui, MainWindow)


@pytest.mark.rapidtest
def test_simple(_package):
    assert os.path.exists(_package)
