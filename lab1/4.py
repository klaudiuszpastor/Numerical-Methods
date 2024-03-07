def fibonacci_procedural(n):
    fib_sequence = [0, 1]
    for i in range(2, n):
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence

# Przykład użycia:
n = 10
fibonacci_sequence = fibonacci_procedural(n)
print(fibonacci_sequence)
