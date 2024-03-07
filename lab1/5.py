class Fibonacci:
    def __init__(self, n):
        self.n = n

    def calculate(self):
        fib_sequence = [0, 1]
        for i in range(2, self.n):
            fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
        return fib_sequence

# Przykład użycia:
n = 10
fib = Fibonacci(n)
fibonacci_sequence = fib.calculate()
print(fibonacci_sequence)
