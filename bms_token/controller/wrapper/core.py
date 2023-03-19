"""Wrapper for OATHController C# class."""

from pathlib import Path

try:
    from pythonnet import load

    load("coreclr")
    import clr

    path = Path(__file__).absolute().parent / "bin" / "OATHController"
    clr.AddReference(str(path))
    from MobileSecureIT.Data import OATHController
except (ImportError, RuntimeError) as e:
    raise e


from bms_token.controller.abc import BaseController


class OATHWrapper(BaseController):
    """Wrapper for OATHController C# class."""

    @staticmethod
    def passcode(secret: str) -> str:
        """Return verification passcode from secret."""
        return OATHController.passcode(secret)

    @staticmethod
    def gen_hotp_token(secret: str, iteration: int, digits: int = 6) -> str:
        """Return HOTP token at iteration from secret."""
        return OATHController.GenerateHOTPPassword(secret, iteration, digits)
