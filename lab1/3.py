from functools import reduce

def fibonacci_functional(n):
    return reduce(lambda x, _: x+[x[-1]+x[-2]], range(n-2), [0, 1])

# Przykład użycia:
n = 10
fibonacci_sequence = fibonacci_functional(n)
print(fibonacci_sequence)
