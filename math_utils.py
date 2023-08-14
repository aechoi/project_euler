import numpy as np

def get_factors(num):
    """get a list of the prime factorization of num"""
    for divisor in range(2, int(num**0.5)+1):
        if num%divisor == 0:
            factors = [divisor]
            factors.extend(get_factors(num/divisor))
            return factors
    return [num]

def get_primes(num: int):
    """get all prime numbers up to the num'th prime"""
    primes = []
    counter = 2
    while len(primes) < num:
        if len(get_factors(counter)) == 1:
            primes.append(counter)
        counter += 1
    return primes