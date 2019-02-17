#!/usr/bin/env python3
"""
Problem:
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get
3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.

"""

"""
Solution Reasoning:

Conditions:
(a) 333 Multiples of 3, 199 Multiples of 5 and 66 multiples of 15
(b) Multiples of 3 and 5 overlap at 15
(c) For a series, n(n-1)/2 is equal to the sum of all numbers in the sequence

Therefore, adding up the first 333 numbers and multiplying by 3, adding up the
first 199 numbers and multiplying by 5 and subtracting the 66 multiples of 15
should give us our desired output
"""


def natural_number_sum(num):
    return num * (num+1)/2


print(3*natural_number_sum(333) +
                 5*natural_number_sum(199) - 15*natural_number_sum(66))
