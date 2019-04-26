#!/usr/bin/python
# -*- coding: utf-8 -*-

import pytest
from Split.main import generate
from Split.main import check
from Split.main import add

def example1():
    res = generate()
    assert (res == 0)


def example2():
    res = check()
    assert (res == 0)


def example3():
    res = add(1)
    assert (res == 1)