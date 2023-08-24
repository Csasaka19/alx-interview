#!/usr/bin/python3
"""UTF-8 encoding validation module"""
from typing import List


def validUTF8(data: List[int]) -> bool:
    """Function checks whether given data is a valid utf-8 encoded data"""
    # Keep track of number of bytes in current character which is set to MSB
    num_bytes: int = 0
    # Keep track of number of bytes left to validate in the character
    counter: int = 0

    # loop through the data
    for number in data:
        if counter == 0:
            # Right-shift bitwise operator used to validate current data
            if number >> 7 == 0b0:
                num_bytes = 1
            elif number >> 5 == 0b110:
                num_bytes = 2
            elif number >> 4 == 0b1110:
                num_bytes = 3
            elif number >> 3 == 0b11110:
                num_bytes = 4
            else:
                return False
            counter = num_bytes - 1
        else:
            if number >> 6 != 0b10:
                return False
            counter -= 1
        return counter == 0
