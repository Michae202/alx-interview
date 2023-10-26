#!/usr/bin/python3
''' UTF-8 Validation'''


def validUTF8(data):
    ''' a function that validates utf'''
    for byte in data:
        bit_char = format(byte, '08b')
        if bit_char.startswith('0'):
            continue
        elif bit_char.startswith('110'):
            continue
        elif bit_char.startswith('1110'):
            continue
        elif bit_char.startswith('11110'):
            continue
        else:
            return False
    return True
