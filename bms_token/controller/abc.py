"""Abstract base classes for OATH controller."""

from abc import ABC, abstractmethod


class BaseController(ABC):
    """Abstract base class for OATHController."""

    @staticmethod
    @abstractmethod
    def passcode(secret: str) -> str:
        """Return verification passcode from secret."""
        ...

    @staticmethod
    @abstractmethod
    def gen_hotp_token(secret: str, iteration: int, digits: int = 6) -> str:
        """Return HOTP token at iteration from secret."""
        ...
