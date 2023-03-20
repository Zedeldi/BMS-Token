"""Pytest fixtures."""

import random
import string

import pytest


@pytest.fixture
def secret() -> str:
    """Return random secret 40 characters long."""
    return "".join([random.choice(string.hexdigits) for _ in range(40)])
