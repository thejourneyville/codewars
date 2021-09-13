# https://www.codewars.com/kata/521c2db8ddc89b9b7a0000c1
"""
Snail Sort
Given an n x n array, return the array elements arranged from outermost elements to the middle element, traveling clockwise.

array = [[1,2,3],
         [4,5,6],
         [7,8,9]]
snail(array) #=> [1,2,3,6,9,8,7,4,5]
For better understanding, please follow the numbers of the next array consecutively:

array = [[1,2,3],
         [8,9,4],
         [7,6,5]]
snail(array) #=> [1,2,3,4,5,6,7,8,9]

NOTE: The idea is not sort the elements from the lowest value to the highest; the idea is to traverse the 2-d array in a clockwise snailshell pattern.

NOTE 2: The 0x0 (empty matrix) is represented as en empty array inside an array [[]].
"""

def snail(snail_map):
    
    if snail_map == [[]]:
        return []
    
    n = len(snail_map)
    
    flat = []
    top, left = 0, 0
    bottom, right = n, n
    
    while top < bottom:
        for c in range(left, right):
            flat.append(snail_map[top][c])
        top += 1

        for r in range(top, bottom):
            flat.append(snail_map[r][right - 1])
        right -= 1

        for c in range(right - 1, left - 1, -1):
            flat.append(snail_map[bottom - 1][c])
        bottom -= 1

        for r in range(bottom - 1, top - 1, -1):
            flat.append(snail_map[r][left])
        left += 1

    return flat
