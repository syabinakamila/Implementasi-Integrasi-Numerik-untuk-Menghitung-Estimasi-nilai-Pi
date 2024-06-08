import time
import numpy as np
import pandas as pd

# Nilai referensi pi
reference_pi = 3.14159265358979323846

# Berbagai nilai N untuk diuji
N_values = [10, 100, 1000, 10000]

# Daftar untuk menyimpan hasil
results_simpson = []

# Lakukan pengujian untuk setiap N
for N in N_values:
    start_time = time.time()
    approx_pi = simpson_integral(f, 0, 1, N)
    elapsed_time = time.time() - start_time
    rms_error = np.sqrt((approx_pi - reference_pi) ** 2)
    results_simpson.append((N, approx_pi, rms_error, elapsed_time))

# Tampilkan hasil
df_simpson = pd.DataFrame(results_simpson, columns=['N', 'Approximation', 'RMS Error', 'Execution Time'])
print(df_simpson)
