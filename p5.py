import math
import numpy as np
from collections import defaultdict
from tqdm import tqdm

def get_factors(num):
    for divisor in range(2, int(num**0.5)+1):
        if num%divisor == 0:
            factors = [divisor]
            factors.extend(get_factors(num/divisor))
            return factors
    return [int(num)]

def divisible_by_all(num):
    divisors = np.arange(1, 21)
    if np.all(num%divisors == 0):
        return True
    return False


divisors = np.arange(1, 21)
total_factors = defaultdict(int)
for divisor in divisors:
    factors = get_factors(divisor)
    for factor in set(factors):
        if total_factors[factor] < factors.count(factor):
            total_factors[factor] = factors.count(factor)

answer = 1
for factor, count in total_factors.items():
    answer *= factor**count
print(answer)

