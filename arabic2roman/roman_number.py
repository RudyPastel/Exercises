#Roman characters for units
units = ['', 'I', 'II', 'III', 'IV', 'V','VI','VII','VIII','IX']

#Roman characters for tens
tens = ['', 'X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC']

#Roman characters for hundreds
hundreds = ['', 'C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM']

#Roman characters for thousands
thousands = ['', 'M', 'MM', 'MMM']

#List of the small number conversion table
conversion_table = [units, tens, hundreds, thousands]


def arabic2roman(arabic_number, table=conversion_table, sep='-'):
    #For small number the 'M' convention is used. For bigger number the '-' convention is used.
    if arabic_number <= 3999:
        number_list = 4
    else:
        number_list = 3

    #List of the arabic equivalent of each digit in arabic_number
    roman_number = []

    #Counts the current power of ten represented by the last digit
    power_of_10 = 0

    #arabic_number is integer divided by ten at each steps until it equals zero and we step out of the loop
    while arabic_number:
        #Extract the number of units
        digit = arabic_number % 10

        #Add a separation mark for each power of 10**3
        if not(power_of_10 % number_list):
            roman_number[:0] = [sep]
        #Add the new digit conversion to the list as the new first element
        roman_number[:0] = [table[power_of_10 % number_list][digit]]

        #Interger divide by ten to pop the digits of units
        arabic_number /= 10

        #Counts the current power of ten represented by the last digit
        power_of_10 += 1

    return ''.join(roman_number[:-1])