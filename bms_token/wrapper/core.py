"""Wrapper for OATHController C# class."""

import sys
from pathlib import Path
from typing import Optional

try:
    from pythonnet import load

    load("coreclr")
    import clr

    path = Path(__file__).absolute().parent / "bin" / "OATHController"
    clr.AddReference(str(path))
    from MobileSecureIT.Data import OATHController
except (ImportError, RuntimeError) as e:
    print(f"Error: {e}")
    sys.exit(1)


class OATHWrapper:
    """Wrapper for OATHController C# class."""

    @staticmethod
    def passcode(secret: str) -> str:
        """Return verification passcode from secret."""
        return OATHController.passcode(secret)

    @staticmethod
    def gen_hotp_token(secret: str, iteration: int, digits: int = 6) -> str:
        """Return HOTP token at iteration from secret."""
        return OATHController.GenerateHOTPPassword(secret, iteration, digits)


class BMSToken:
    """Class to handle BMS token methods."""

    def __init__(self, secret: str, iteration: int = 0, digits: int = 6) -> None:
        """Initialise BMSToken instance."""
        self.secret = secret.upper()
        self.iteration = iteration
        self.digits = digits

    def gen_hotp_token(self) -> str:
        """Return HOTP at current iteration and increment counter."""
        token = OATHWrapper.gen_hotp_token(self.secret, self.iteration, self.digits)
        self.iteration += 1
        return token

    def at(self, iteration: int, digits: Optional[int] = None) -> str:
        """Return HOTP token at specified iteration."""
        return OATHWrapper.gen_hotp_token(self.secret, iteration, digits or self.digits)

    @property
    def passcode(self) -> str:
        """Return verification passcode from secret."""
        return OATHWrapper.passcode(self.secret)

    def verify_passcode(self, passcode: str) -> bool:
        """Verify that specified passcode equals calculated passcode."""
        return self.passcode == passcode.upper()
