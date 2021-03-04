

# %% Approach 1
import math


def factors(number):
    square_root = math.sqrt(number)
    factors = {1}

    for i in range(2, int(square_root) + 1):
        if number % i == 0:
            factors = factors.union([i, number // i])

    return sum(factors)


factors(24)

# %% Approach 2


def factors(n):
    for i in range(2, int(pow(n, 0.5) + 1)):
        if n % i == 0:
            yield i
            if i * i != n:
                yield n // i


# %% My approach
def factors(number):
    factor = 1
    all_nums = []
    while factor < number:
        if number % factor == 0:
            all_nums.append(factor)
        factor += 1
