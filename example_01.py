'''
Write a function that takes an integer as input, and returns the number of bits that are equal to one in the binary representation of that number. 
You can guarantee that input is non-negative.
Example: The binary representation of 1234 is 10011010010, so the function should return 5 in this case

4|__2
0   2|__2     
    0   1

4//2 = 2 -- 4 % 2 = 0
2//2 = 1 -- 2 % 2 = 0

7//

'''
import pytest

def count_bits_module(n):
    if n > 0 : return bin(n).count('1')
    return 0


def count_bits(n):
    remainder = 1
    if n > 0:
        while (n // 2) > 0:
            if n % 2 == 1:
                remainder += 1
            n = n // 2 
        return remainder
    else:
        return 0


def test_count_bits():
    assert count_bits(0) == 0
    assert count_bits(4) == 1
    assert count_bits(6) == 2
    assert count_bits(7) == 3
    assert count_bits(9) == 2
    assert count_bits(10) == 2


def test_count_bits_module():
    assert count_bits(0) == 0
    assert count_bits(4) == 1
    assert count_bits(6) == 2
    assert count_bits(7) == 3
    assert count_bits(9) == 2
    assert count_bits(10) == 2
