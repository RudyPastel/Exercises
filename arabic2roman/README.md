# Arabic to roman number converter

The function arabic2roman returns a Roman numeral string representation of a given Arabic number. Specifically, it takes a non negative integer in arabic and base 10 format as input and returns its Roman numeral string representation.

## Roman numeral string representation convention
Among the various existing conventions, the following were chosen.
- If the input is less than 3999, the 'M' standard convention from wikipedia is used.
    - The symbols I, X, C, and M can be repeated three times in succession, but no more. (They may appear more than three times if they appear non-sequentially, such as XXXIX.) D, L, and V can never be repeated.
    - I can be subtracted from V and X only. X can be subtracted from L and C only. C can be subtracted from D and M only. V, L, and D can never be subtracted
    - Only one small-value symbol may be subtracted from any large-value symbol.
    - Exemple : 1903 = MCMIII.
- If the input is greater or equal to 4000, the following '-' convention is used.
    - Units, tens and hundreds are grouped togather for each power of 1000.
    - A dash '-' represents a power of 1000.
    - Exemple : 656 980 = DCLVI-CMLXXX and 245 000 500 963 = CCXLV- -D-CMLXIII. 
    
## Usage

1. Import roman_number
2. Call roman_number.arabic2roman on an integer. 