#!/usr/bin/python3
"""UTF-8 Validation module."""


def get_leading_set_bits(num):

    """Return the number of leading
    set bits (1) in a byte.
    """
    set_bits = 0
    helper = 1 << 7
    while helper & num:
        set_bits += 1
        helper = helper >> 1
    return set_bits


def validUTF8(data):

    """Determine if a given data set
    represents a valid UTF-8 encoding.
    """
    bits_count = 0
    for byte in data:
        if bits_count == 0:
            bits_count = get_leading_set_bits(byte)
            # 1-byte (format: 0xxxxxxx)
            if bits_count == 0:
                continue
            # A character in UTF-8 can be 1 to 4 bytes long
            if bits_count == 1 or bits_count > 4:
                return False
        else:
            # Check if the current byte has the format 10xxxxxx
            if not (byte & (1 << 7) and not (byte & (1 << 6))):
                return False
        bits_count -= 1
    return bits_count == 0
