#!/usr/bin/python3
""" a function that unlock boxes """


def canUnlockAll(boxes):
    """
    A function that unlock boxes
    """

    if len(boxes) < 1:
        return False
    # Create a listofKeys
    keys = [0]
    # Set of unlocked boxes
    index = 0
    # if we have a key
    while index < len(keys):
        # Open the box with the key
        if len(boxes[keys[index]]) < 1:
            index += 1
            continue
        for element in boxes[keys[index]]:
            if element not in keys:
                if element < len(boxes):
                    keys.append(element)
        index += 1
    # Check the keys
    if len(keys) == len(boxes):
        return True
    return False
