def nbr_of_laps(x, y):
    
    if x == y:
        return 1, 1
    
    else:
        
        product = x * y
        max_x, max_y = product / x, product / y
        divisor = max([max_x, max_y]) - 1
        
        while divisor > 1:
            if not max_x % divisor and not max_y % divisor:
                return max_x / divisor, max_y / divisor
            else:
                divisor -= 1
        
        return max_x, max_y
