"""
Backwards Read Primes are primes that when read backwards in base 10 
(from right to left) are a different prime. (This rules out primes which are palindromes.)

Examples:
13 17 31 37 71 73 are Backwards Read Primes
13 is such because it's prime and read from right to left writes 31 which is prime too. 
Same for the others.

Task
Find all Backwards Read Primes between two positive given numbers (both inclusive), 
the second one always being greater than or equal to the first one. 
The resulting array or the resulting string will be ordered following the natural order of the prime numbers.

Examples (in general form):
backwardsPrime(2, 100) => [13, 17, 31, 37, 71, 73, 79, 97] 
backwardsPrime(9900, 10000) => [9923, 9931, 9941, 9967] 
backwardsPrime(501, 599) => []
"""
def backwards_prime(start: int, stop: int) -> list | None:

    # creating range of odd only prime candidates within given start/stop inclusive   
    all_nums = range(start + 1, stop + 1, 2) if start % 2 == 0 else range(start, stop + 1, 2)

    def find_primes(candidates):

        num_of_candidates = len(candidates)
        candidate_idx = 0
        primes_found = []

        while candidate_idx < num_of_candidates:
            
            candidate_sqrt = int(candidates[candidate_idx] ** .5) + 1
            
            # checking if prime by iterating only to its squareroot
            for i in range(2, candidate_sqrt):
                if candidates[candidate_idx] % i == 0:
                    break
            else:
                primes_found.append(candidates[candidate_idx])
            
            candidate_idx += 1

        return primes_found
    
    # removing palindrones 
    result1 = find_primes(all_nums)
    reversed_the_nums = [int(str(a)[-1::-1]) for a in result1 if a != int(str(a)[-1::-1])]

    result2 = find_primes(reversed_the_nums)
    return 0 if [] else [int(str(a)[-1::-1]) for a in result2]


print(backwards_prime(109500, 109700))
