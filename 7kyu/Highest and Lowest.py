def high_and_low(numbers):
    numbers = [int(num) for num in numbers.split()]
    return f"{str(max(numbers))} {str(min(numbers))}"