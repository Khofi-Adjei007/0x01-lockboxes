#!/usr/bin/python3

def canUnlockAll(boxes):

    """
    Determine if all the boxes can be opened.
    Parameters:
    boxes (list of lists): A list of lists where each
    list represents a box and contains keys to other boxes.
    Returns:
    bool: True if all boxes can be opened, otherwise False.
    """

    n = len(boxes)
    unlocked = set([0])
    stack = [0]

    while stack:
        current_box = stack.pop()
        for key in boxes[current_box]:
            if key not in unlocked and key < n:
                unlocked.add(key)
                stack.append(key)

    return len(unlocked) == n


if __name__ == "__main__":
    boxes = [[1], [2], [3], [4], []]
    print(canUnlockAll(boxes))  # True

    boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
    print(canUnlockAll(boxes))  # True

    boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
    print(canUnlockAll(boxes))  # False
