"""GUI window to display BMS token and handle methods."""

from typing import Optional

from PyQt5.QtCore import QSettings, Qt
from PyQt5.QtGui import QCloseEvent
from PyQt5.QtWidgets import (
    QHBoxLayout,
    QLabel,
    QMessageBox,
    QPushButton,
    QVBoxLayout,
    QWidget,
)

from bms_token.gui.dialogs import SettingsDialog
from bms_token.token import BMSToken


class BMSTokenGUI(QWidget):
    """Class for GUI window."""

    def __init__(self, token: Optional[BMSToken] = None) -> None:
        """Initialise window with graphical elements."""
        super().__init__()
        self.settings = QSettings("bms-token", "gui")
        self.token = token
        while not self.token:
            self.token = self.loadToken()
        self.initUI()
        self.generateToken()

    def initUI(self) -> None:
        """Initialise GUI elements."""
        self.setWindowTitle("BMS Token")
        self.setMinimumSize(256, 128)

        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignCenter)

        self.titleLabel = QLabel()
        self.titleLabel.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.titleLabel)

        self.tokenLabel = QLabel()
        self.tokenLabel.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.tokenLabel)

        generateButton = QPushButton("Generate")
        generateButton.clicked.connect(self.generateToken)
        layout.addWidget(generateButton)

        controlLayout = QHBoxLayout()

        settingsButton = QPushButton("Settings")
        settingsButton.clicked.connect(
            lambda: self.openSettingsDialog() and self.generateToken()
        )
        controlLayout.addWidget(settingsButton)

        closeButton = QPushButton("Close")
        closeButton.clicked.connect(self.close)
        controlLayout.addWidget(closeButton)

        layout.addLayout(controlLayout)
        self.setLayout(layout)

    def closeEvent(self, event: QCloseEvent) -> None:
        self.saveToken()

    def generateToken(self) -> None:
        """Generate token and set label contents."""
        if not self.token:
            return None
        self.titleLabel.setText(f"Token #{self.token.iteration}:")
        self.tokenLabel.setText(self.token.gen_hotp_token())

    def saveToken(self) -> None:
        """Store current configuration in persistent QSettings."""
        if not self.token:
            return None
        self.settings.setValue("secret", self.token.secret)
        self.settings.setValue("iteration", self.token.iteration)
        self.settings.setValue("digits", self.token.digits)

    def loadToken(self) -> Optional[BMSToken]:
        """Get stored configuration from QSettings."""
        secret = self.settings.value("secret", type=str)
        iteration = self.settings.value("iteration", 0, type=int)
        digits = self.settings.value("digits", 6, type=int)
        if not secret:
            return self.openSettingsDialog()
        return BMSToken(secret, iteration, digits)

    def openSettingsDialog(self) -> Optional[BMSToken]:
        """Open SettingsDialog and parses returned dict."""
        prefs = SettingsDialog.getSettings()
        if not prefs or not prefs["secret"]:
            QMessageBox.critical(
                self, "Invalid Secret Key", "The provided secret key is not valid."
            )
            return None
        self.token = BMSToken(prefs["secret"], prefs["iteration"], prefs["digits"])
        if not self.token.verify_passcode(prefs["passcode"]):
            QMessageBox.critical(self, "Validation Failed", "Incorrect passcode.")
            return None
        self.saveToken()
        return self.token
