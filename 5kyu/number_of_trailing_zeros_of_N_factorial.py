def zeros(n):
    
    print(n)
    
    counter = 1
    result = 1
    
    while counter <= n:

        result *= counter
        counter += 1
    
    zero_count = 0
    print(result)
    for checker in str(result)[::-1]:
        if checker == "0":
            zero_count += 1
        else:
            return zero_count
        

print(zeros(100000))
