#!/usr/bin/env python2


def solution(l):
    import functools
    from types import FunctionType
    digits = sorted(l, reverse=True)
    number = functools.reduce(lambda total, d: 10 * total + d, digits, 0)
    remainder = number % 3
    if remainder == 0:
        return number
    elif len(str(number)) == 1:
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

    def inner(digits):
        digits = sorted(digits, reverse=True)
        number = functools.reduce(lambda total, d: 10 * total + d, digits, 0)
        remainder = number % 3
        if remainder == 0:
            return number
        elif len(str(number)) == 1:
            return 0
        else:
            the_other = 2 if remainder == 1 else 1
            if not has_remainder[remainder]:
                has_remainder[the_other] = sorted(has_remainder[the_other])
                digits.remove(has_remainder[the_other][0])
                has_remainder[the_other].pop(0)
                digits.remove(has_remainder[the_other][0])
                has_remainder[the_other].pop(0)
            else:
                has_remainder[remainder] = sorted(has_remainder[remainder])
                digits.remove(has_remainder[remainder][0])
                has_remainder[remainder].pop(0)
        return lambda: inner(digits)

    def do(digits):
        fn = inner(digits)
        while fn.__class__ == FunctionType:
            fn = fn()
        return fn

    return do(digits)


print(solution([2, 0, 0]))
print('')
print(solution([0, 0, 1]))
print('')
print(solution([5, 5, 5, 7]))
print('')
print(solution([4, 3, 1, 1]))
print('')
print(solution([3, 9, 8, 0, 5, 3]))
print('')