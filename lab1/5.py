import timeit

class Fibonacci:
    def __init__(self, n):
        self.n = n
    def calculate(self):
        fib_num = [0, 1]
        for i in range(2, self.n):
            fib_num.append(fib_num[-1] + fib_num[-2])
        return fib_num

n = 30
fib = Fibonacci(n)
fibonacci_num = fib.calculate()
print(fibonacci_num)

time_taken = timeit.timeit(lambda: fib.calculate(), number=1)
print("Czas wykonania:", time_taken, "sekundy")