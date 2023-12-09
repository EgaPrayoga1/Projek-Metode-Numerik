import numpy as np

def simpsons_rule(func, a, b, n):
    h = (b - a) / n
    x_values = np.linspace(a, b, n+1)
    integral_sum = func(a) + func(b)
    
    for i in range(1, n, 2):
        integral_sum += 4 * func(x_values[i])

    for i in range(2, n-1, 2):
        integral_sum += 2 * func(x_values[i])

    return h / 3 * integral_sum

# Fungsi yang diintegralkan
def integrand(x):
    return 3*x**2 + 2*x + 12  # Perhatikan perbaikan pada operasi perkalian, 2*x

# Batas integrasi
a = 0
b = 2

# Jumlah subinterval
n = 2

# Hitung integral menggunakan metode Simpson
result = simpsons_rule(integrand, a, b, n)

print(f"Hasil integral menggunakan metode Simpson: {result}")
