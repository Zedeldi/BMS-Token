"""Test OATHController methods."""

import pytest

from bms_token.controller import NativeController
from bms_token.controller.wrapper import OATHController, OATHWrapper


def test_native_passcode(secret: str) -> None:
    """Test native passcode generation method."""
    assert NativeController.passcode(secret) == OATHController.passcode(secret)


@pytest.mark.parametrize("iteration", [0, 1])
def test_native_hotp_token(secret: str, iteration: int) -> None:
    """Test native HOTP token generation method."""
    assert NativeController.gen_hotp_token(
        secret, iteration
    ) == OATHController.GenerateHOTPPassword(secret, iteration)


def test_wrapper_passcode(secret: str) -> None:
    """Test wrapper passcode generation method."""
    assert OATHWrapper.passcode(secret) == OATHController.passcode(secret)


@pytest.mark.parametrize("iteration", [0, 1])
def test_wrapper_hotp_token(secret: str, iteration: int) -> None:
    """Test wrapper HOTP token generation method."""
    assert OATHWrapper.gen_hotp_token(
        secret, iteration
    ) == OATHController.GenerateHOTPPassword(secret, iteration)
