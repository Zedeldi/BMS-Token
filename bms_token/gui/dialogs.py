"""Dialog windows for BMS token GUI client."""

from typing import Any, Type

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QDialog,
    QGroupBox,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QSpinBox,
    QVBoxLayout,
)


class SettingsDialog(QDialog):
    """BMS token GUI client settings dialog."""

    def __init__(self) -> None:
        """Initialise dialog and create graphical elements."""
        super().__init__()
        self.initUI()

    def initUI(self) -> None:
        """Create graphical elements for window."""
        self.setWindowTitle("BMS Token - Settings")
        self.setWindowFlag(Qt.WindowContextHelpButtonHint, False)
        self.resize(600, 300)

        self.secretInputLabel = QLabel("Secret key:")
        self.secretInput = QLineEdit()
        self.secretInput.setPlaceholderText("Ssshhh! It's a secret!")
        self.secretInput.setToolTip("Secret key for token generation.")

        self.passcodeInputLabel = QLabel("Validation passcode:")
        self.passcodeInput = QLineEdit()
        self.passcodeInput.setPlaceholderText("Passcode")
        self.passcodeInput.setToolTip("Passcode for secret key validation.")

        self.iterationInputLabel = QLabel("Iteration:")
        self.iterationInput = QSpinBox()
        self.iterationInput.setValue(0)
        self.iterationInput.setRange(0, 2147483647)
        self.iterationInput.setToolTip("Current iteration for token generation.")

        self.digitsInputLabel = QLabel("Digits:")
        self.digitsInput = QSpinBox()
        self.digitsInput.setValue(6)
        self.digitsInput.setRange(1, 10)
        self.digitsInput.setToolTip("Length of token to generate.")

        self.submitButton = QPushButton("Submit")
        self.submitButton.clicked.connect(self.returnSettings)

        self.secretLayout = QVBoxLayout()
        self.secretLayout.addWidget(self.secretInputLabel)
        self.secretLayout.addWidget(self.secretInput)
        self.secretLayout.addWidget(self.passcodeInputLabel)
        self.secretLayout.addWidget(self.passcodeInput)

        self.secretGroup = QGroupBox("Secret")
        self.secretGroup.setLayout(self.secretLayout)

        self.configLayout = QHBoxLayout()
        self.configLayout.addWidget(self.iterationInputLabel)
        self.configLayout.addWidget(self.iterationInput)
        self.configLayout.addWidget(self.digitsInputLabel)
        self.configLayout.addWidget(self.digitsInput)

        self.configGroup = QGroupBox("Configuration")
        self.configGroup.setLayout(self.configLayout)

        self.parentLayout = QVBoxLayout()
        self.parentLayout.addWidget(self.secretGroup)
        self.parentLayout.addWidget(self.configGroup)
        self.parentLayout.addWidget(self.submitButton)
        self.setLayout(self.parentLayout)

    def returnSettings(self) -> dict[str, Any]:
        """Close dialog and return dictionary with settings."""
        self.accept()
        settings = {
            "secret": self.secretInput.text() or "",
            "passcode": self.passcodeInput.text() or "",
            "iteration": int(self.iterationInput.text() or 0),
            "digits": int(self.digitsInput.text() or 6),
        }
        return settings

    @classmethod
    def getSettings(cls: Type["SettingsDialog"]) -> dict[str, Any]:
        """Create a dialog instance and return user settings."""
        dialog = cls()
        if dialog.exec_():
            return dialog.returnSettings()
        return {}
