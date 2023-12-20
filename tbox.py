#!/usr/bin/env python3
"""
Author : Rob Samoraj <rsamoraj@vivaldi.net>
Date   : 2023-12-19
Purpose: Hacking Toolbox Command Line Program
"""

import argparse
from Cryptography import rot13

# --------------------------------------------------


def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Hacking Toolbox',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    
    # parser.add_argument('text',
    #                     metavar='str',
    #                     help='Input text or file',
    #                     type=str,
    #                     default='')

    parser.add_argument('-r',
                        '--rot13',
                        metavar='str',
                        help='Decipher a ROT13 encrypted text',
                        type=str)

    parser.add_argument('-d',
                        '--decode',
                        help='Decodes a string from binary, hex, or base64',
                        metavar='str',
                        type=str,
                        choices=['bin', 'hex', 'b64'],)

    parser.add_argument('-i',
                        '--int',
                        help='A named integer argument',
                        metavar='int',
                        type=int,
                        default=0)

    parser.add_argument('-f',
                        '--file',
                        help='A readable file',
                        metavar='FILE',
                        type=argparse.FileType('rt'),
                        default=None)

    parser.add_argument('-o',
                        '--on',
                        help='A boolean flag',
                        action='store_true')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()

    
    print(rot13(args.rot13))


# --------------------------------------------------
if __name__ == '__main__':
    main()
