"""
Problem:
A palindromic number reads the same both ways. The largest
palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

"""
Solution Reasoning:

998001 is 999*999, so the largest possible number that this palindrome could
theoritically be. Then we check each number to see first if it is a palindrome.
Once we are done with that, we can check if there are two 3 digit factors.
"""

import math


def find_largest_palindrome():
    current_check = 998001
    while True:
        if is_palindrome(current_check):
            if is_double_three_digit_multiple(current_check):
                return current_check
        current_check-=1

def is_palindrome(number):
    str = '%s' % number
    number_length = len(str)
    for i in range(0, math.floor(number_length/2)):
        if str[i] != str[len(str)-1-i]:
            return False
    return True


def is_double_three_digit_multiple(number):
    for current in range(100, math.floor(math.sqrt(number))):
        if number%current==0:
            if len('%s' % (number//current))==3:
                print(number, current, number//current)
                return True
    return False

find_largest_palindrome()
