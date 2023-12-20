#!/usr/bin/env python3
"""Tests for tbox.py"""

import os

prg = './tbox.py'

# --------------------------------------------------


def test_exists():
    """Program exists"""

    assert os.path.isfile(prg)
