import numpy as np
import time

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

# Testing
reference_pi = 3.14159265358979323846
N_values = [10, 100, 1000, 10000]

results_simpson = []
for N in N_values:
    start_time = time.time()
    approx_pi = simpson_integral(f, 0, 1, N)
    elapsed_time = time.time() - start_time
    rms_error = np.sqrt((approx_pi - reference_pi) ** 2)
    results_simpson.append((N, approx_pi, rms_error, elapsed_time))

# Display results
import pandas as pd
df_simpson = pd.DataFrame(results_simpson, columns=['N', 'Approximation', 'RMS Error', 'Execution Time'])
print(df_simpson)
