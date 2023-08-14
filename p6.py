import numpy as np

nat_nums = np.arange(1, 101)
sum_of_squares = np.sum(nat_nums**2)
square_of_sum = np.sum(nat_nums)**2

print(sum_of_squares - square_of_sum)