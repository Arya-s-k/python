def integer_to_roman(num):
    
    symbols = [
        (1000, 'M'),
        (900, 'CM'),
        (500, 'D'),
        (400, 'CD'),
        (100, 'C'),
        (90, 'XC'),
        (50, 'L'),
        (40, 'XL'),
        (10, 'X'),
        (9, 'IX'),
        (5, 'V'),
        (4, 'IV'),
        (1, 'I')
    ]

    roman_numeral = ''
    for value, symbol in symbols:
        while num >= value:
            roman_numeral += symbol
            num -= value
    
    return roman_numeral

number = 100
print(f"Input integer number: {number}")
roman_numeral = integer_to_roman(number)
print(f"The Roman numeral representation of {number} is: {roman_numeral}")