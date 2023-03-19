"""Class to handle BMS token methods and attributes."""

from typing import Optional, Type

from bms_token.controller import BaseController, NativeController


class BMSToken:
    """Class to handle BMS token methods and attributes."""

    def __init__(
        self,
        secret: str,
        iteration: int = 0,
        digits: int = 6,
        controller: Type[BaseController] = NativeController,
    ) -> None:
        """Initialise BMSToken instance."""
        self.secret = secret.upper()
        self.iteration = iteration
        self.digits = digits
        self.controller = controller

    def gen_hotp_token(self) -> str:
        """Return HOTP at current iteration and increment counter."""
        token = self.controller.gen_hotp_token(self.secret, self.iteration, self.digits)
        self.iteration += 1
        return token

    def at(self, iteration: int, digits: Optional[int] = None) -> str:
        """Return HOTP token at specified iteration."""
        return self.controller.gen_hotp_token(
            self.secret, iteration, digits or self.digits
        )

    @property
    def passcode(self) -> str:
        """Return verification passcode from secret."""
        return self.controller.passcode(self.secret)

    def verify_passcode(self, passcode: str) -> bool:
        """Verify that specified passcode equals calculated passcode."""
        return self.passcode == passcode.upper()
