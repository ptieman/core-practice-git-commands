import re
import pytest


def always_returns_true():
    return True


def test_always_returns_true():
    assert always_returns_true()

def test_bukunmi():
    return True