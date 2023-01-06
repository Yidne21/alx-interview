# 0x01. Lockboxes
<p>Alx interview preparation question which focus's on how to solve algorthimic questions</p>

# Tasks

You have n number of locked boxes in front of you. Each box is numbered sequentially from 0 to n - 1 and each box may contain keys to the other boxes.

Write a method that determines if all the boxes can be opened.

- Prototype: `def canUnlockAll(boxes)`
- boxes is a list of lists
- A key with the same number as a box opens that box
- You can assume all keys will be positive integers
- There can be keys that do not have boxes
- The first box `boxes[0]` is unlocked
- Return True if all boxes can be opened, else return False

## Examples
### Example 1
- Input:  ```[[1], [2], [3], [4], []]```
- Output: ```True```
### Example 2
- Input:  ```[[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]```
- Output: ```True```
### Example 3
- Input:  `[[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]`
- Output: `False`

