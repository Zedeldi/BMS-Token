"""Open BMS Token GUI."""

import sys

from PyQt5.QtWidgets import QApplication

from bms_token.gui.core import BMSTokenGUI
from bms_token.token import BMSToken


def main() -> None:
    """Start GUI interface for BMS Token."""
    if "-h" in sys.argv or "--help" in sys.argv:
        print_usage()
        sys.exit(1)
    args = dict(zip(["path", "secret", "iteration", "digits"], sys.argv))
    secret = args.get("secret", None)
    iteration = int(args.get("iteration", 0))
    digits = int(args.get("digits", 6))
    app = QApplication(sys.argv)
    window = BMSTokenGUI(BMSToken(secret, iteration, digits) if secret else None)
    window.show()
    app.exec()


def print_usage() -> None:
    """Print usage message to stdout."""
    print("python -m bms_token.gui <secret> [iteration] [digits]")


if __name__ == "__main__":
    main()
