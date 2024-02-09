def fibonacci(n):
    fib_series = [0, 1]
    while len(fib_series) < n:
        fib_series.append(fib_series[-1] + fib_series[-2])
    return fib_series

terms = int(input("Enter the number of terms for Fibonacci series: "))
result = fibonacci(terms)
print(f"Fibonacci Series: {result}")