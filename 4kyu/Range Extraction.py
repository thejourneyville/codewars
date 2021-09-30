"""
A format for expressing an ordered list of integers is to use a comma separated list of either

- individual integers
- or a range of integers denoted by the starting integer separated from the end integer in the range by a dash, '-'.

The range includes all integers in the interval including both endpoints.
It is not considered a range unless it spans at least 3 numbers. For example "12,13,15-17"
Complete the solution so that it takes a list of integers in increasing order,
and returns a correctly formatted string in the range format.

Example:

solution([-6, -3, -2, -1, 0, 1, 3, 4, 5, 7, 8, 9, 10, 11, 14, 15, 17, 18, 19, 20])
# returns "-6,-3-1,3-5,7-11,14,15,17-20"
'-3--1,2,10,15,16,18-20'
"""
# len 20


def solution(d):

    current = 0
    differences = {}
    consecutives = 0
    new_range = ""
    output = ""
    potential = []

    for ele in d[1::]:
        differences[d[current], ele] = abs(d[current] - ele)

        if abs(d[current] - ele) == 1:
            consecutives += 1
            if consecutives == 1:
                potential.append(d[current])

            elif consecutives == 2:
                potential.clear()
                new_range = f"{d[current - 1]}-"

        else:
            consecutives = 0
            if new_range:
                new_range += f"{d[current]},"
                output += new_range
                new_range = ""
                potential.clear()
            elif potential:
                output += f"{potential[0]},{d[current]},"
                potential.clear()
            else:
                output += f"{d[current]},"

        current += 1
    if new_range:
        new_range += f"{d[current]}"
        output += new_range
    elif potential:
        output += f"{potential[0]},{d[current]}"
    else:
        output += f"{d[current]}"


    return output


data = [-6,-3,-2,-1,0,1,3,4,5,7,8,9,10,11,14,15,17,18,19,20]
print(solution(data))
