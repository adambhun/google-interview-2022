#!/usr/bin/env python3


def solution(x):
    '''
    'hashmap' is a dictionary, whose keys are the characters of the alphabet
    in alphabetical order and whose values are the characters of the alphabet
    in reverse order.
    If a character from the input string is a key of 'hashmap',
    then it is replaced by the value character of that key.
    The sum of 'nth_letter' and 'make_it_122' is always 122.
    '''
    hashmap = {}
    for nth_letter, make_it_122 in zip(
        range(97, 123), reversed(range(0, 123-97))
    ):
        hashmap[chr(nth_letter)] = chr(97+make_it_122)
    result = ''
    for char in x:
        if char in hashmap:
            result += (hashmap[char])
        else:
            result += char
    return result
