import numpy as np

def simpson_integral(f, a, b, N):
    if N % 2 == 1: 
        N += 1
    # N harus genap untuk Simpson 1/3
    dx = (b - a) / N
    total = f(a) + f(b)
    for i in range(1, N, 2):
        total += 4 * f(a + i * dx)
    for i in range(2, N-1, 2):
        total += 2 * f(a + i * dx)
    return total * dx / 3

def f(x):
    return 4 / (1 + x**2)
