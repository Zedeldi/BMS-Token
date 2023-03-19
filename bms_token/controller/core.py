"""Class to handle OATHController methods."""

import hashlib
import hmac
import sys

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
        i_bytes = bytearray(iteration.to_bytes(8, sys.byteorder))
        if sys.byteorder == "little":
            i_bytes.reverse()
        hmac_obj = hmac.new(
            bytearray.fromhex(secret),
            i_bytes,
            hashlib.sha1,
        )
        digest = hmac_obj.digest()
        idx = digest[19] & 15
        n1 = (digest[idx] & 127) << 24
        n2 = (digest[idx + 1] & 255) << 16
        n3 = (digest[idx + 2] & 255) << 8
        n4 = digest[idx + 3] & 255
        d = int("1" + "0" * digits)
        token = (n1 | n2 | n3 | n4) % d
        return f"{token:0{digits}}"
