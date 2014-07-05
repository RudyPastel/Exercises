#Roman characters for units
units = ['', 'I', 'II', 'III', 'IV','V','VI','VII','VIII','IX']

#Roman characters for tens
tens = ['', 'X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC']

#Roman characters for hundreds
hundreds = ['', 'C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC','CM']

#Roman characters for thousands
thousands = ['', 'M', 'MM', 'MMM']

#List of the small number conversion table
smallNumberTable = [units, tens, hundreds, thousands]


#Conversion for number less than or equal to 3999
def romanNumberSmall(arabic_number, table=smallNumberTable):
    #List of the arabic equivalent of each digit in arabic_number
    roman_number = []

    #Counts the current power of ten represented by the last digit
    powerOf10 = 0

    #arabic_number is integer divided by ten at each steps until it equals zero and we step out of the loop
    while arabic_number:
        #Extract the number of units
        digit = arabic_number % 10

        #Add the new digit conversion to the list as the new first element
        roman_number[:0] = [table[powerOf10][digit]]

        #Interger divide by ten to pop the digits of units
        arabic_number /= 10

        #Counts the current power of ten represented by the last digit
        powerOf10 += 1
    return ''.join(roman_number)


#Conversion for numbers greater than 3999
def romanNumberBig(arabic_number, table=smallNumberTable, sep='-'):
    #List of the arabic equivalent of each digit in arabic_number
    roman_number = []

    #Counts the current power of ten represented by the last digit
    powerOf10 = 0

    #arabic_number is integer divided by ten at each steps until it equals zero and we step out of the loop
    while arabic_number:
        #Extract the number of units
        digit = arabic_number % 10

        #Add a separation mark for each power of 10**3
        if not(powerOf10 % 3):
            roman_number[:0] = [sep]
        #Add the new digit conversion to the list as the new first element
        roman_number[:0] = [table[powerOf10 % 3][digit]]

        #Interger divide by ten to pop the digits of units
        arabic_number /= 10

        #Counts the current power of ten represented by the last digit
        powerOf10 += 1
    return ''.join(roman_number[:-1])

def arabic2roman(arabic_number):
    if arabic_number <= 3999:
        return romanNumberSmall(arabic_number)
    return romanNumberBig(arabic_number)