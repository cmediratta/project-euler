#!/usr/bin/env python3
"""
Problem:
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""

"""
Solution Reasoning:

The goal is to iterate and find the first prime each time and divide by that
number to simplify the problem until the remaining number is prime, which will
be the largest prime.


This solution will likely not work for really massive numbers, but for the
number we are dealing with here it should work fine.

I am also using this to learn to set up an environment to optimize code.
"""

import math


def find_largest_prime(number):
    while(number%2==0): #This part removes all the multiples of
        number//=2       #two, which allows for only comparing odds
    if number==1:  #This checks if there is only multiples of 2
        return 2

    return (recursive_primefinder(number, 3))


def recursive_primefinder(current, min):
    max = math.sqrt(current) #Only compares what it needs to
    while min <= max:
        if (current%min==0):
            return recursive_primefinder(current//min, min)
        min+=2 #We already checked for even factors so this only compares odds
    return current

assert(find_largest_prime(600851475143)==6857)
assert(find_largest_prime(142862533044391160)==16769023)
assert(find_largest_prime(1304156376184614245589968752280200)==16769023)
assert(find_largest_prime(515377520732011331036461129765621272702107522001)==3)
