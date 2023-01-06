#!/usr/bin/python3
'''task's 0 Module
'''


def canUnlockAll(boxes):
    key = set()
    for i in range(len(boxes) - 1):
        if i == 0 or i in key:
            for k in boxes[i]:
                for j in boxes[k]:
                    key.add(k)
                    key.add(j)
    key.add(0)
    if len(key) == len(boxes):
        return True
    else:
        return False