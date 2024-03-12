#!/usr/bin/python3
""" a method that determines if all the boxes can be opened"""


def canUnlockAll(boxes):
    """ a method that determines if all the boxes can be opened"""
    checked = set()
    for i in range(len(boxes)):
        checked = checked | set(boxes[i])
    # print(checked, set(range(1, len(boxes))), len(boxes) - 1)
    if checked >= set(range(1, len(boxes))):
        return True
    return False
