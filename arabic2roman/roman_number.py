#Roman characters for units
units = ['', 'I', 'II', 'III', 'IV', 'V','VI','VII','VIII','IX']

#Roman characters for tens
tens = ['', 'X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC']

#Roman characters for hundreds
hundreds = ['', 'C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM']

#Roman characters for thousands
thousands = ['', 'M', 'MM', 'MMM']

#Conversion table
conversion_table = [units, tens, hundreds, thousands]


def arabic2roman(arabic_number, table=conversion_table, sep='-'):

    #Roman representation convention
    if arabic_number <= 3999:
        number_list = 4
    else:
        number_list = 3

    #Roman equivalent digit per digit
    roman_number = []

    #Power of ten represented by the last digit
    power_of_10 = 0

    #arabic_number is converted digit by digit from right to left
    while arabic_number:

        #Extract the digits of units
        digit = arabic_number % 10

        #Add a separation mark for each power of 10**3
        if not(power_of_10 % number_list):
            roman_number[:0] = [sep]

        #Add new digit
        roman_number[:0] = [table[power_of_10 % number_list][digit]]

        #Pop the digits of units
        arabic_number /= 10
        power_of_10 += 1

    return ''.join(roman_number[:-1])