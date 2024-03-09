import timeit
from functools import reduce


def fibonacci_functional(n):
    return reduce(lambda x, _: x+[x[-1]+x[-2]], range(n-2), [0, 1])

n = 30
fibonacci_sequence = fibonacci_functional(n)
print(fibonacci_sequence)

time_taken = timeit.timeit(lambda: fibonacci_functional(n), number=1)
print("Czas wykonania:", time_taken, "sekundy")