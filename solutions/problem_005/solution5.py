#!/usr/bin/env python3
"""
Problem:
2520 is the smallest number that can be divided by each of the numbers from
1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of
the numbers from 1 to 20?
"""

"""
Solution Reasoning:
The way this solution works is it starts with 1, and it tries to divide by every
prime factor, then multiplying by the number itself. The reason this works is
because it removes any duplicate factors, and if the number is already divisible
by the entire number, it will merely divide by it then multiply by it.

"""

import math


def get_GCD_of_sequence(number):
    product = 1
    for i in range(2, number+1):
        for factor in prime_factors(i):
            if product%factor==0:
                product/=factor
        product*=i
    return product


def prime_factors(n):
  for i in range(2,math.floor(math.sqrt(n))+1):
    if n % i == 0:
      return [i] + prime_factors(n / i)
  return [n]

print(get_GCD_of_sequence(20))
