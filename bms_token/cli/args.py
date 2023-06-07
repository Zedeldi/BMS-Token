"""Handle arguments for command-line interface.."""

from argparse import ArgumentParser


def get_parser() -> ArgumentParser:
    """Return argument parser instance."""
    parser = ArgumentParser(
        prog="bms_token",
        description="Python command-line interface for BMS Token",
        epilog="Copyright (C) 2023 Zack Didcott",
    )

    parser.add_argument("secret", help="secret key")
    parser.add_argument("-q", "--quiet", action="store_true", help="output less text")

    subparsers = parser.add_subparsers(dest="command", required=True)
    gen_parser = subparsers.add_parser(
        "generate", aliases=["gen", "g"], help="generate HOTP token at iteration"
    )
    gen_parser.add_argument(
        "iteration", type=int, help="iteration for generating HOTP token"
    )
    gen_parser.add_argument(
        "--digits", "-d", type=int, default=6, help="length of token"
    )
    gen_parser.add_argument(
        "--range",
        "-r",
        action="store_true",
        help="generate tokens in range of iteration",
    )
    gen_parser.set_defaults(command="generate")
    verify_parser = subparsers.add_parser(
        "verify", aliases=["v"], help="verify passcode for given secret"
    )
    verify_parser.add_argument("passcode", help="verification passcode")
    verify_parser.set_defaults(command="verify")

    return parser
