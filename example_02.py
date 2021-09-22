'''
Find an efficient algorithm to find the smallest distance (measured in number of words) between any two given words in a string.

For example, given words "hello", and "world" and a text content of "dog cat hello cat dog dog hello cat world", 
return 1 because there's only one word "cat" in between the two words.


'''

import pytest


def sm_distance(frase, word_1, word_2):
    sequence = str(frase).split(' ')
    min = len(sequence)

    for index, value in enumerate(sequence):
        if value == word_1:
            if sequence.index(word_2, index) - index < min :
                min = (sequence.index(word_2, index) - index) - 1
    
    return min



def test_sm_distance():
    assert sm_distance("dog cat hello cat dog dog hello cat world", "hello", "world") == 1
