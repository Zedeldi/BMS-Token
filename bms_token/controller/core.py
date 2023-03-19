"""Class to handle OATHController methods."""

from bms_token.controller.abc import BaseController


class NativeController(BaseController):
    """Native Python class for OATHController."""

    @staticmethod
    def passcode(secret: str) -> str:
        """Return verification passcode from secret."""
        return secret[5:31:5].upper()

    @staticmethod
    def gen_hotp_token(secret: str, iteration: int, digits: int = 6) -> str:
        """Return HOTP token at iteration from secret."""
        raise NotImplementedError
