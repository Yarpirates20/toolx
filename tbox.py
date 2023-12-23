#!/usr/bin/env python3
"""
Author : Rob Samoraj <rsamoraj@vivaldi.net>
Date   : 2023-12-19
Purpose: Hacking Toolbox Command Line Program
"""

import argparse
from ARP import *
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

    #----------------------------------------------
    # Subparsers
    subparsers = global_parser.add_subparsers(
        dest="command",
        help="Commands to run",
        required=True
    )

    #----------------------------------------------
    # Decode subparser
    decode_parser = subparsers.add_parser(
        "decode",
        help="Decode a string from binary, hex, or base64"
    )

    decode_parser.add_argument("-b",
                               "--bin",
                               help="Decodes a binary string",
                               action="store",)
    decode_parser.set_defaults(func=binary_decode)

    decode_parser.add_argument("-x",
                               "--hex",
                               help="Decodes a hex string",
                               action="store",)
    decode_parser.set_defaults(func=hex_decode)

    decode_parser.add_argument("-b64",
                                 "--base64",
                                 help="Decodes a base64 string",
                                 action="store",)
    decode_parser.set_defaults(func=base64_decode)

    decode_parser.add_argument("-r13",
                               "--rot13",
                               help="Decodes a ROT13 string",
                               action="store",)
    decode_parser.set_defaults(func=rot13)
    #----------------------------------------------
    # ARP subparser
    """ arp_parser = subparsers.add_parser(
        "arp",
        help="ARP Tools"
    )

    arp_parser.add_argument("-s",
                            "--scan",
                            help="Scans the network for hosts",
                            action="store",)
    arp_parser.set_defaults(func=arpScan) """
    

    #----------------------------------------------
    return global_parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()

    if args.command == "decode":
        if args.bin is not None:
            binary_decode(args.bin)
        if args.hex is not None:
            hex_decode(args.hex)
        if args.base64 is not None:
            base64_decode(args.base64)
        if args.rot13 is not None:
            rot13(args.rot13)

    # if args.command == "arp":
    #     if args.scan is not None:
    #         arpScan(args.scan)


# --------------------------------------------------
if __name__ == "__main__":
    main()
