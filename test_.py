#!/usr/bin/env python3
"""Tests for tbox.py"""

import os
import re
from subprocess import getstatusoutput
from Cryptography import rot13

prg = './tbox.py'

# --------------------------------------------------
def test_exists():
    """Program exists"""

    assert os.path.isfile(prg)

# --------------------------------------------------
def test_usage():
    """usage"""

    for flag in ['-h', '--help']:
        rv, out = getstatusoutput(f'{prg} {flag}')
        assert rv == 0
        assert re.match("usage", out, re.IGNORECASE)

# --------------------------------------------------
def test_rot13():
    """Test rot13"""

    assert rot13('a') == 'n'
    assert rot13('A') == 'N'
    assert rot13('Rob') == 'Ebo'
    assert rot13('Jul qvq gur puvpxra pebff gur ebnq?') == \
        'Why did the chicken cross the road?'
    
