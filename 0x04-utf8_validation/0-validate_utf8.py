#!/usr/bin/python3
"""determines if a given data set represents a valid UTF-8 encoding"""


def validUTF8(data):
    """determines if a given data set represents a valid UTF-8 encoding"""
    if all(isinstance(x, int) for x in data) and isinstance(data, list):
        if len(data):
            for val in data:
                if not (val >= 0 and val <= 127):
                    return False
            return True
