def fib(n):
    fib_list = [1, 1]
    for i in range(n - 2):
        fib_list.append(fib_list[-1] + fib_list[-2])
    return fib_list[-1]

print(fib(12468))