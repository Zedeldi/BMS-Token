"""Collection of generic helper functions."""


def hex_encode(n: int) -> str:
    """Return hex-encoding of int n."""
    return hex(n)[2:].upper()
