import numpy as np

def FizzBuzz(start, finish):
    nums = np.arange(start, finish+1)
    out = nums.astype(object)
    mask3 = nums % 3 == 0
    mask5 = nums % 5 == 0

    out[mask3 & mask5] = "fizzbuzz"
    out[mask3 & ~mask5] = "fizz"
    out[mask5 & ~mask3] = "buzz"

    return out
