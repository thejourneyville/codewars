class RomanNumerals:

    def to_roman(val):
        
        calculate = val
        roman_str = ""
        
        thousands = calculate // 1000
        calculate -= (1000 * thousands)
        roman_str += "M" * thousands

        nine_hundreds = calculate // 900
        calculate -= (900 * nine_hundreds)
        roman_str += "CM" * nine_hundreds
        
        five_hundreds = (calculate // 500)
        calculate -= (500 * five_hundreds)
        roman_str += "D" * five_hundreds
        
        four_hundreds = (calculate // 400)
        calculate -= (400 * four_hundreds)
        roman_str += "CD" * four_hundreds

        hundreds = calculate // 100
        calculate -= (100 * hundreds)
        roman_str += "C" * hundreds

        nineties = calculate // 90
        calculate -= (90 * nineties)
        roman_str += "XC" * nineties
        
        fifties = calculate // 50
        calculate -= (50 * fifties)
        roman_str += "L" * fifties

        fourties = calculate // 40
        calculate -= (40 * fourties)
        roman_str += "XL" * fourties
        
        tens = calculate // 10
        calculate -= (10 * tens)
        roman_str += "X" * tens

        nines = calculate // 9
        calculate -= (9 * nines)
        roman_str += "IX" * nines

        fives = calculate // 5
        calculate -= (5 * fives)
        roman_str += "V" * fives

        fours = calculate // 4
        calculate -= (4 * fours)
        roman_str += "IV" * fours

        ones = calculate // 1
        calculate -= (1 * ones)
        roman_str += "I" * ones

        return roman_str

    def from_roman(roman_num):
        components = ["CM", "M", "CD", "D", "XC", "C", "XL", "L", "IX", "X", "IV", "V", "I"]
        copy_ = roman_num
        reference = [900, 1000, 400, 500, 90, 100, 40, 50, 9, 10, 4, 5, 1]
        values = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

        while copy_:
            for idx, numeral in enumerate(components):
                if numeral in copy_:

                    values[idx] += reference[idx]
                    numeral_len = len(numeral)
                    place = copy_.index(numeral)

                    if numeral_len == 1:
                        copy_ = copy_[:place] + copy_[place+1:]
                        break
                    else:
                        copy_ = copy_[:place] + copy_[place+2:]
                        break
               
        return sum(values)

print(RomanNumerals.from_roman('MMMDCCXCVI'))
