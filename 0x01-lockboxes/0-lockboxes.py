#!/usr/bin/python3

def canUnlockAll(boxes):
    n = len(boxes)
    visited = set()
    stack = [0]  # Start with box 0, which is already unlocked

    while stack:
        box = stack.pop()
        visited.add(box)

        for key in boxes[box]:
            if key not in visited and key < n:
                stack.append(key)

    return len(visited) == n

    boxes = [[1], [2], [3], [4], []]
    print(canUnlockAll(boxes))  # Output: True

    boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
    print(canUnlockAll(boxes))  # Output: True

    boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
    print(canUnlockAll(boxes))  # Output: False
