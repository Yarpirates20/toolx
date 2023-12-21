#!/usr/bin/env python3
"""
Author : Rob Samoraj <rsamoraj@vivaldi.net>
Date   : 2023-12-19
Purpose: Hacking Toolbox Command Line Program
"""

import argparse
from Cryptography import rot13, binary_decode

# --------------------------------------------------


def get_args():
    """Get command-line arguments"""

    # Global parser
    global_parser = argparse.ArgumentParser(
        prog="tbox",
        description='Hacking Toolbox',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    
    subparsers = global_parser.add_subparsers(title='command', help='sub-command help', dest='command')
    
    """ # global_parser.add_argument('text',
    #                     metavar='str',
    #                     help='Input text or file',
    #                     type=str,
    #                     default='') """

    # Decode subparser
    decode_args_template = {
        'dest': 'cipher',
        'type': 'str',
        'metavar': 'str',
        'help': 'A ciphered string',
    }

    decode_parser = subparsers.add_parser('decode', help='Decode a string from several common encodings')

    # decode_parser.add_argument('text',
    #                     metavar='str',
    #                     help='Input text or file',
    #                     type=str)
    decode_parser.add_argument('-b',
                        '--bin',
                        help='Decodes a binary string',
                        metavar='str',
                        type=str)
    
    decode_parser.set_defaults(func=binary_decode)
                               
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

    """ global_parser.add_argument('-i',
                        '--int',
                        help='A named integer argument',
                        metavar='int',
                        type=int,
                        default=0)

    global_parser.add_argument('-f',
                        '--file',
                        help='A readable file',
                        metavar='FILE',
                        type=argparse.FileType('rt'),
                        default=None)

    global_parser.add_argument('-o',
                        '--on',
                        help='A boolean flag',
                        action='store_true') """

    return global_parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()

    
    if args.command == 'decode':
        print(args.func(args.bin))
    

    


# --------------------------------------------------
if __name__ == '__main__':
    main()
