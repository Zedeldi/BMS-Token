"""Command-line interface for BMS token."""

from argparse import ArgumentParser

from bms_token.wrapper import BMSToken


def main() -> None:
    """Main entry-point for BMS token."""
    parser = ArgumentParser(
        prog="bms_token",
        description="Python command-line interface for BMS Token",
        epilog="Copyright (C) 2023 Zack Didcott",
    )

    parser.add_argument("secret", help="secret key")

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

    args = parser.parse_args()

    bms_token = BMSToken(args.secret)

    if args.command == "generate":
        if args.iteration < 0:
            raise ValueError("Iteration cannot be negative.")
        print(f"Secret: {bms_token.secret}")
        if args.range:
            for i in range(0, args.iteration + 1):
                print(f"#{i}: {bms_token.at(i, args.digits)}")
        else:
            token = bms_token.at(args.iteration, args.digits)
            print(f"#{args.iteration}: {token}")
    elif args.command == "verify":
        match = bms_token.verify_passcode(args.passcode)
        print(f"Secret: {bms_token.secret}")
        print(f"Passcode: {args.passcode.upper()} (Expected: {bms_token.passcode})")
        print(f"Match: {match}")


if __name__ == "__main__":
    main()
