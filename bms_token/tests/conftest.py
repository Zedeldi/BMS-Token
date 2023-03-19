"""Pytest fixtures."""

import random
import string

import pytest


@pytest.fixture
def secret() -> str:
    """Return random secret (length=40)."""
    return "".join([random.choice(string.hexdigits) for _ in range(40)])
