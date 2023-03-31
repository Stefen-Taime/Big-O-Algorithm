def naive_fibonacci(n):
    if n <= 1:
        return n
    else:
        return naive_fibonacci(n - 1) + naive_fibonacci(n - 2)

n = 10
result = naive_fibonacci(n)
print(result)
