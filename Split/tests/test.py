#!/usr/bin/python
# -*- coding: utf-8 -*-

import pytest
from Split.main import produce_l1


def example():
    res = produce_l1()
    assert (res == 0)

