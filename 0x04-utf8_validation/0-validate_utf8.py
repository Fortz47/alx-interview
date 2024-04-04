#!/usr/bin/python3
"""determines if a given data set represents a valid UTF-8 encoding"""


def validUTF8(data):
    """determines if a given data set represents a valid UTF-8 encoding"""
    if all(isinstance(x, int) for x in data) and isinstance(data, list):
        if len(data):
            if not (data[0] >= 0 and data[0] <= 127):
                return False
            return True
    return False
