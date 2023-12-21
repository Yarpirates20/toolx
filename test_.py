#!/usr/bin/env python3
"""Tests for tbox.py"""

import os
import re
from subprocess import getstatusoutput
from Cryptography import *

prg = "./tbox.py"


# --------------------------------------------------
def test_exists():
    """Program exists"""

    assert os.path.isfile(prg)


# --------------------------------------------------
def test_usage():
    """usage"""

    for flag in ["-h", "--help"]:
        rv, out = getstatusoutput(f"{prg} {flag}")
        assert rv == 0
        assert re.match("usage", out, re.IGNORECASE)


# --------------------------------------------------
def test_rot13():
    """Test rot13"""

    assert rot13("a") == "n"
    assert rot13("A") == "N"
    assert rot13("Rob") == "Ebo"
    assert (
        rot13("Jul qvq gur puvpxra pebff gur ebnq?")
        == "Why did the chicken cross the road?"
    )


# --------------------------------------------------
# def test_decode_binary():
#     """Test decode binary subparser functionality"""

#     rv, out = getstatusoutput(f'{prg} decode -b 01101000 01100101 01101100 01101100 01101111')
#     assert rv == 0
#     assert out == 'hello'


# --------------------------------------------------
def test_binary_decode(capsys):
    binary_decode("01101000 01100101 01101100 01101100 01101111")
    out, err = capsys.readouterr()
    assert out.strip('\n') == "hello"


# --------------------------------------------------
def test_hex_decode(capsys):
    hex_decode("68656c6c6f")
    out, err = capsys.readouterr()
    assert out.strip('\n') == "hello"

# --------------------------------------------------
def test_base64_decode(capsys):
    base64_decode("aGVsbG8=")
    out, err = capsys.readouterr()
    assert out.strip('\n') == "hello"
