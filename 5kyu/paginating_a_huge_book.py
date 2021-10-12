"""
Johnny is working as an intern for a publishing company, and was tasked with cleaning up old code. 
He is working on a program that determines how many digits are in all of the page nbers in a 
book with pages from 1 to n (inclusive).
For example, a book with 4 pages has 4 digits (one for each page) while a 12-page book has 15 
(9 for 1-9, plus 2 each for 10, 11, 12).
Johnny's boss, looking to futureproof, demanded that the new program be able to handle books up to 
400,000,000,000,000,000 pages.

examples:
test.assert_equals(page_digits(4), 4)
test.assert_equals(page_digits(12), 15)
test.assert_equals(page_digits(100), 192)
"""

def page_digits(n):

    digits = 0

    if n > 9:
        digits += 9
    else:
        digits += n
        return digits
    if n > 99:
        digits += (99-9) * 2
    else:
        digits += (n-9) * 2
        return digits
    if n > 999:
        digits += (999-99) * 3
    else:
        digits += (n-99) * 3
        return digits
    if n > 9999:
        digits += (9999-999) * 4
    else:
        digits += (n-999) * 4
        return digits
    if n > 99999:
        digits += (99999-9999) * 5
    else:
        digits += (n-9999) * 5
        return digits
    if n > 999999:
        digits += (999999-99999) * 6
    else:
        digits += (n-99999) * 6
        return digits
    if n > 9999999:
        digits += (9999999-999999) * 7
    else:
        digits += (n-999999) * 7
        return digits
    if n > 99999999:
        digits += (99999999-9999999) * 8
    else:
        digits += (n-9999999) * 8
        return digits
    if n > 999999999:
        digits += (999999999-99999999) * 9
    else:
        digits += (n-99999999) * 9
        return digits
    if n > 9999999999:
        digits += (9999999999-999999999) * 10
    else:
        digits += (n-999999999) * 10
        return digits
    if n > 99999999999:
        digits += (99999999999-9999999999) * 11
    else:
        digits += (n-9999999999) * 11
        return digits
    if n > 999999999999:
        digits += (999999999999-99999999999) * 12
    else:
        digits += (n-99999999999) * 12
        return digits
    if n > 9999999999999:
        digits += (9999999999999-999999999999) * 13
    else:
        digits += (n-999999999999) * 13
        return digits
    if n > 99999999999999:
        digits += (99999999999999-9999999999999) * 14
    else:
        digits += (n-9999999999999) * 14
        return digits
    if n > 999999999999999:
        digits += (999999999999999-99999999999999) * 15
    else:
        digits += (n-99999999999999) * 15
        return digits
    if n > 9999999999999999:
        digits += (9999999999999999-999999999999999) * 16
    else:
        digits += (n-999999999999999) * 16
        return digits
    if n > 99999999999999999:
        digits += (99999999999999999-9999999999999999) * 17
    else:
        digits += (n-9999999999999999) * 17
        return digits
    if n > 999999999999999999:
        digits += (999999999999999999-99999999999999999) * 18
    else:
        digits += (n-99999999999999999) * 18
        return digits
    
    return digits

print(page_digits(100))
