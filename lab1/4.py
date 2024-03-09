import timeit

def fibonacci_len(n):
    fib_num = [0, 1]
    for i in range(2, n):
        fib_num.append(fib_num[-1] + fib_num[-2])
    return fib_num

print(fibonacci_len(30))

time_taken = timeit.timeit(lambda: fibonacci_len(30), number=1)
print("Czas wykonania:", time_taken, "sekundy")