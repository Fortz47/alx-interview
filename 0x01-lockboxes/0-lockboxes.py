#!/usr/bin/python3
""" a method that determines if all the boxes can be opened"""


def canUnlockAll(boxes):
    """ a method that determines if all the boxes can be opened"""
    # Keep track of visited boxes
    visited = set()
    visited.add(0)  # Starting box is always unlocked
    queue = [0]  # Initialize the queue with the first box

    while queue:
        current_box = queue.pop(0)
        for key in boxes[current_box]:
            if key not in visited and key < len(boxes):
                visited.add(key)
                queue.append(key)

    # Check if all boxes have been visited
    return len(visited) == len(boxes)
