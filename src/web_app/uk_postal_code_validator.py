def uk_postal_code_validator(code):
        """
        Input: code <string>
        Output: 'Y' or 'N' <string>
        'Y' indicates that the given UK postal code pattern is valid
        'N' indicates that the given UK postal code pattern is invalid
        Usage Example: 
        validate_postal_code('SW1W 0NY')

        Description: This function validates the UK postal code format given in 
        https://en.wikipedia.org/wiki/Postcodes_in_the_United_Kingdom#formatting

        This also includes special cases given in the table - 
        url - https://en.wikipedia.org/wiki/Postcodes_in_the_United_Kingdom#Special_cases   

        Regex pattern match is used to validate the UK postal code. 

        Note: The REGEX Pattern - [A-Z]{1,2}[0-9][A-Z0-9]? ?[0-9][A-Z]{2} can accomodate most of the postal codes, 
        However, the below REGEX code is used to accomodate the special cases as well.    

        (([A-Z]{1,2}[0-9][A-Z0-9]?|ASCN|STHL|TDCU|BBND|[BFS]IQQ|PCRN|TKCA) ?[0-9][A-Z]{2}|BFPO ?[0-9]{1,4}|(KY[0-9]|MSR|VG|AI)[ -]?[0-9]{4}|[A-Z]{2} ?[0-9]{2}|GE ?CX|GIR ?0A{2}|SAN ?TA1)


        Meaning of Each pattern from the above code: 

        PATTERN 1: ([A-Z]{1,2}[0-9][A-Z0-9]?|ASCN|STHL|TDCU|BBND|[BFS]IQQ|PCRN|TKCA)
        [A-Z]{1,2} -> should contain letters A to Z. It can either be 1 or 2 characters.
        [0-9] -> single digit number (0 to 9)
        [A-Z0-9]? -> Can be optional. It can contain a letter (A to Z) or a number (0 to 9).
        OR 
        ASCN|STHL|TDCU|BBND|[BFS]IQQ|PCRN|TKCA -> It should have the below 4 characters:
        ASCN or STHL or TDCU or BBND or BIQQ OR FIQQ or SIQQ or PCRN or TKCA

        PATTERN 2: ?[0-9][A-Z]{2}|BFPO -> Can be Optional. 
        [0-9][A-Z]{2} -> Contain one number (0 to 9) and Contains two letters (A to Z)
        OR 
        BFPO -> Can contain the letters - BFPO

        PATTERN 3: ?[0-9]{1,4}|(KY[0-9]|MSR|VG|AI)[ -] -> Can be Optional. 
        Contain 1 to 4 numbers (0 to 9)    
        OR 
        (KY[0-9]|MSR|VG|AI)[ -] -> contains characters 'KY' followed by a digit (0 to 9) or contains MSR or VG or AI followed by '-'

        PATTERN 4: ?[0-9]{4}|[A-Z]{2} - Can be Optional.
        [0-9]{4}|[A-Z]{2} -> contains 4 digits OR 2 letters

        PATTERN 5: ?[0-9]{2}|GE  - Can be Optional.
        [0-9]{2}|GE -> contains 2 digits OR 'GE'

        PATTERN 6: ?CX|GIR - Can be Optional.
        CX|GIR -> contains letters 'CX' or 'GIR'

        PATTERN 7: ?0A{2}|SAN - Can be Optional.
        0A{2}|SAN - Can start with 0AA OR 'SAN'

        PATTERN 8:?TA1 - Can be Optional.
        TA1 - Can start with TA1

        """

        import re
        return 'Y' if re.compile('(([A-Z]{1,2}[0-9][A-Z0-9]?|ASCN|STHL|TDCU|BBND|[BFS]IQQ|PCRN|TKCA) ?[0-9][A-Z]{2}|BFPO ?[0-9]{1,4}|(KY[0-9]|MSR|VG|AI)[ -]?[0-9]{4}|[A-Z]{2} ?[0-9]{2}|GE ?CX|GIR ?0A{2}|SAN ?TA1)').match(code) else 'N'