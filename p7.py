import math_utils

primes = []
counter = 2
while len(primes) < 10001:
    if len(math_utils.get_factors(counter)) == 1:
        primes.append(counter)
    counter += 1

print(primes[-1])
