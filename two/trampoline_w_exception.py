#!/usr/bin/env python2


def solution(l):
    '''
    Recursion is neither necessary nor beneficial in this case; I chose to
    go with it only because I suppose it's more impressive and impression is
    what this challenge is all about.
    I know that python does not optimize tail recursion, so there is no
    performance benefit to using it and it eliminates the stack frame as well,
    making debugging harder. To that end I utilized a structure called
    trampoline at the end of this function, instead of just writing
    "return inner(digits)".
    '''
    import functools
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
        '''
        If correct, return the number created from the list, else remove
        a number or two from the list based on the remainder and repeat.
        '''
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
        return inner, digits

    func, args = inner, digits

    while True:
        try:
            func, args = func(args)
        except TypeError:
            return func(args)
