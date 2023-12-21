#!/usr/bin/env python3
"""
Author : Rob Samoraj <rsamoraj@vivaldi.net>
Date   : 2023-12-19
Purpose: Hacking Toolbox Command Line Program
"""

import argparse
from Cryptography import *


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    # Global parser
    global_parser = argparse.ArgumentParser(
        prog="tbox",
        description="Hacking Toolbox",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    # Subparsers
    subparsers = global_parser.add_subparsers(
        title="command",
        help="sub-command help",
        dest="command",
        metavar="COMMAND",
    )

    # Decode subparser
    """ decode_args_template = {
        "dest": "cipher",
        "type": "str",
        "metavar": "str",
        "help": "A ciphered string",
    } """

    decode_parser = subparsers.add_parser(
        "decode",
        help="Decode a string from several common encodings",
    )

    decode_parser.add_argument("-b",
                               "--bin",
                               help="Decodes a binary string",
                               metavar="str",
                               type=str)
    decode_parser.set_defaults(func=binary_decode)

    decode_parser.add_argument("-x",
                               "--hex",
                               help="Decodes a hex string",
                               metavar="str",
                               type=str)
    decode_parser.set_defaults(func=hex_decode)

    decode_parser.add_argument("-b64",
                                 "--base64",
                                 help="Decodes a base64 string",
                                 metavar="str",
                                 type=str)
    decode_parser.set_defaults(func=base64_decode)

    """ global_parser.add_argument('-r',
                        '--rot13',
                        metavar='str',
                        help='Decipher a ROT13 encrypted text',
                        type=str)

    global_parser.add_argument('-d',
                        '--decode',
                        help='Decodes a string from binary, hex, or base64',
                        metavar='str',
                        type=str,
                        choices=['bin', 'hex', 'b64'],) """

    return global_parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()

    if args.command == "decode":
        args.func(args)


# --------------------------------------------------
if __name__ == "__main__":
    main()
