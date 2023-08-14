import numpy as np

def generate_fibonacci(max_num):
    fibs = [1,2]
    while fibs[-1] < max_num:
        fibs.append(fibs[-1]+fibs[-2])
    return fibs

fibs = generate_fibonacci(4000000)
fibs = np.array(fibs)
fibs_even = fibs[fibs%2==0]
print(np.sum(fibs_even))
