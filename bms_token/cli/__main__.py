"""Command-line interface for BMS token."""

from bms_token.cli.args import get_parser
from bms_token.token import BMSToken


def main() -> None:
    """Main entry-point for BMS token."""
    parser = get_parser()
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
