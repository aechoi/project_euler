def get_factors(num):
    for divisor in range(2, int(num**0.5)+1):
        if num%divisor == 0:
            factors = [divisor]
            factors.extend(get_factors(num/divisor))
            return factors
    return [num]

print(get_factors(600851475143))  
