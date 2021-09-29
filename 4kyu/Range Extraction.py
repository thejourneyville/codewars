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
"""


# len 20
def range_master(d):

    output = ""
    potential = []
    range_found = False

    for current in range(len(d)):
        after = current + 1
        if current < len(d) - 1:
            if abs(d[current]) - abs(d[after]) == 1:
                if not potential:
                    output += str(d[current])
                potential.append(d[current])
            if len(potential) >= 3:
                range_found = True
            if abs(d[current]) - abs(d[after]) != 1 and range_found:
                potential.append(d[current])
                for item in potential:
                    output += str(item)
                potential = []
            if abs(d[current]) - abs(d[after]) != 1:
                output += str(d[current])
    print(output)







data = [-6, -3, -2, -1, 0, 1, 3, 4, 5, 7, 8, 9, 10, 11, 14, 15, 17, 18, 19, 20]
range_master(data)
