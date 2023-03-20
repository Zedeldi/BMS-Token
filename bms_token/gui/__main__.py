"""Open BMS Token GUI."""

import sys

from PyQt5.QtWidgets import QApplication

from bms_token.gui.core import BMSTokenGUI
from bms_token.token import BMSToken


def print_usage() -> None:
    """Print usage message to stdout."""
    print("python -m bms_token.gui <secret> [iteration]")


if __name__ == "__main__":
    try:
        secret = sys.argv[1]
    except IndexError:
        print_usage()
        sys.exit(1)
    try:
        iteration = int(sys.argv[2])
    except IndexError:
        iteration = 0
    app = QApplication(sys.argv)
    token = BMSToken(secret, iteration)
    window = BMSTokenGUI(token)
    app.exec()
