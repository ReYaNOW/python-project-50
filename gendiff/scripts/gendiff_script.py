import argparse
import sys
from gendiff import generate_diff


def make_parser():
    description = "Compares two configuration files and shows a difference."
    parser = argparse.ArgumentParser(prog="gendiff", description=description)
    parser.add_argument(
        "first_file",
        type=str,
    )

    parser.add_argument(
        "second_file",
        type=str,
    )

    help_ = "set format of output (stylish, plain or json), default is stylish"
    parser.add_argument(
        "-f",
        "--format",
        default="stylish",
        help=help_,
        type=str,
    )
    return parser


def main():
    parser = make_parser()
    if len(sys.argv) == 1:
        parser.print_help(sys.stderr)
        sys.exit(0)

    args = parser.parse_args()
    print(generate_diff(args.first_file, args.second_file, args.format))


if __name__ == "__main__":
    main()
