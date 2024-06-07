# Nama  : Femas Arianda Rizki
# NIM   : 21120122130080
# Kelas : Metode Numerik - B

# Dua digit NIM terakhir % 3 = 80 % 3 = 2
# Jadi mengerjakan dengan Metode 3 (Integrasi Simpson 1/3)

# Kode sumber
import numpy as np
import time
from decimal import Decimal, getcontext

# Menetapkan presisi ke 24 untuk memastikan kita mendapatkan 20 digit setelah titik desimal dan hasil yang lebih presisi
getcontext().prec = 24

# Fungsi yang akan diintegrasikan, f(x) = 4 / (1 + x^2)
def f(x):
    return Decimal(4) / (Decimal(1) + x**2)

# Metode integrasi Simpson 1/3 untuk menghitung integral fungsi f dari a ke b dengan N partisi
def simpson_13(a, b, N):
    if N % 2 == 1:
        N += 1  # Make N even if it is odd
    h = (b - a) / N
    integral = f(Decimal(a)) + f(Decimal(b)) # Menghitung nilai f pada batas integrasi
    for i in range(1, N):
        k = Decimal(a) + i * Decimal(h) # Menghitung nilai k pada partisi ke-i
        if i % 2 == 0:
            integral += 2 * f(k) # Jika i genap, kalikan dengan 2
        else:
            integral += 4 * f(k) # Jika i ganjil, kalikan dengan 4
    integral *= Decimal(h) / Decimal(3) # Kalikan hasil dengan h/3 sesuai dengan rumus Simpson 1/3
    return integral

# Fungsi untuk menghitung nilai pi untuk berbagai nilai N
def calculate_pi(N_values):
    pi_ref = Decimal('3.14159265358979323846') # Nilai referensi pi dengan 20 digit setelah titik desimal
    results = []

    for N in N_values:
        start_time = time.time() # Catat waktu mulai
        pi_est = simpson_13(Decimal(0), Decimal(1), N) # Hitung estimasi pi menggunakan metode Simpson 1/3
        end_time = time.time() # Catat waktu selesai
        elapsed_time = end_time - start_time # Hitung waktu yang diperlukan
        rms_error = np.sqrt((pi_ref - pi_est) ** 2) # Hitung galat RMS (Root Mean Square Error)
        results.append((N, pi_est, rms_error, elapsed_time)) # Simpan hasil dalam daftar

    return results

# Kode testing
N_values = [10, 100, 1000, 10000] # Variasi nilai N
results = calculate_pi(N_values) # Hitung nilai pi untuk masing-masing N

for result in results:
    N, pi_est, rms_error, elapsed_time = result
    print(f"N = {N}: Pi Estimate = {pi_est}, RMS Error = {rms_error}, Time Elapsed = {elapsed_time} seconds")