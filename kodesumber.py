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
    
#Dataset yang digunakan adalah nilai-nilai N yang berbeda yaitu [10, 100, 1000, 10000]. Hasil dari pengujian ini menghasilkan sebuah DataFrame
 #      N  Approximation       RMS Error  Execution Time
#0     10       3.142425  8.325377e-04        0.000098
#1    100       3.141593  3.430682e-07        0.000199
#2   1000       3.141593  3.424119e-11        0.002071
#3  10000       3.141593  2.691930e-15        0.019881
