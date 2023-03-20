"""GUI window to display BMS token and handle methods."""

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QLabel, QPushButton, QVBoxLayout, QWidget

from bms_token.token import BMSToken


class BMSTokenGUI(QWidget):
    """Class for GUI window."""

    def __init__(self, token: BMSToken) -> None:
        """Initialise window with graphical elements."""
        super().__init__()
        self.token = token
        self.initUI()
        self.generateToken()
        self.show()

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

        closeButton = QPushButton("Close")
        closeButton.clicked.connect(self.close)
        layout.addWidget(closeButton)

        self.setLayout(layout)

    def generateToken(self) -> None:
        """Generate token and set label contents."""
        self.titleLabel.setText(f"Token #{self.token.iteration}:")
        self.tokenLabel.setText(self.token.gen_hotp_token())
