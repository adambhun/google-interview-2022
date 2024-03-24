#!/usr/bin/env python2

def solution(l):
    import functools
    digits = sorted(l, reverse=True)
    res = functools.reduce(lambda total, d: 10 * total + d, digits, 0)
    remainder = res % 3
    if remainder == 0:
        return res
    elif len(digits) == 1:
        return 0
    has_remainder = {
        1: [],
        2: []
    }
    for i in digits:
        if i % 3 == 1:
            has_remainder[1].append(i)
        elif i % 3 == 2:
            has_remainder[2].append(i)

    while digits:
        res = functools.reduce(lambda total, d: 10 * total + d, digits, 0)
        remainder = res % 3
        if remainder == 0:
            return res
        elif len(digits) == 1:
            return 0
        else:
            if remainder == 1:
                if not has_remainder[1]:
                    has_remainder[2] = sorted(has_remainder[2])
                    digits.remove(has_remainder[2][0])
                    digits.remove(has_remainder[2][0])
                else:
                    has_remainder[1] = sorted(has_remainder[1])
                    digits.remove(has_remainder[1][0])
            else:
                if not has_remainder[2]:
                    has_remainder[1] = sorted(has_remainder[1])
                    digits.remove(has_remainder[1][0])
                    digits.remove(has_remainder[1][0])
                else:
                    has_remainder[2] = sorted(has_remainder[2])
                    digits.remove(has_remainder[2][0])

