# determine how many laps need to be completed by both 'runners' to return to the same origin point, on different sized tracks,
# at the same time. the runners are running the exact same speed

def nbr_of_laps(x, y):
    
    # if the track sizes are the same, return 1 lap for each runner
    if x == y:
        return 1, 1
    
    else:
        # determine the max multiple
        product = x * y
        # determine each runner's quotient if running the max multiple distance
        max_x, max_y = product / x, product / y
        # determine the larger divisor of the two and subtract 1 as a starting point to decend from to find the least common multiple
        divisor = max([max_x, max_y]) - 1
        
        # loop while the divisor is greater than 1
        while divisor > 1:
            # if modulus returns 0 on both tracks, return the LCM
            if not max_x % divisor and not max_y % divisor:
                return max_x / divisor, max_y / divisor
            else:
                # reduce divisor and repeat
                divisor -= 1
        # return the initial quotient if no smaller common multiple is found
        return max_x, max_y
