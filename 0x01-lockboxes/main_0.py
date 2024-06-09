#!/usr/bin/python3
"""
This script tests the functionality of
the canUnlockAll function,
which checks if all boxes can be unlocked given a
list of lists where each sublist
contains keys to other boxes.

The script imports the canUnlockAll function from the
module '0-lockboxes' and tests it
with three different sets of boxes.
"""

canUnlockAll = __import__('0-lockboxes').canUnlockAll

# Test case 1: Sequential keys
boxes = [[1], [2], [3], [4], []]
print(canUnlockAll(boxes))  # Expected output: True

# Test case 2: Multiple keys and cycles
boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
print(canUnlockAll(boxes))  # Expected output: True

# Test case 3: Disconnected keys
boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
print(canUnlockAll(boxes))  # Expected output: False
