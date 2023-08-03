#!/bin/python3
"""LOCKBOXES"""
def canUnlockAll(boxes):
    """LOCKBOXES CLASS"""
    # if the list is empty
    if not boxes:
        return False
    # When only one box is present it is always unlocked
    if len(boxes) == 1:
        return True
    # Initialize a list of keys with the first key
    keys = [0]
    # Loop through the keys list and append the new keys
    for key in keys:
        # Loop through the boxes list and append the new keys
        for box in boxes[key]:
            if box not in keys and box < len(boxes):
                keys.append(box)
    # Check if the number of keys is equal to the number of boxes
    if len(keys) == len(boxes):
        return True
    return False